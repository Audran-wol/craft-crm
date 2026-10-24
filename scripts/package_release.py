#!/usr/bin/env python3
"""Validate, test, and create a reproducible local release ZIP and checksum."""
import argparse
import hashlib
from pathlib import Path
import re
import runpy
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TOP_FILES = ('README.md', 'VERSION', 'CHANGELOG.md', 'RELEASE.md', 'TESTING.md', 'LICENSE', '.gitignore')
TREES = ('skills', 'tests', 'evaluations', 'scripts', 'examples', '.github')
EXCLUDED_PARTS = {'.git', 'dist', '__pycache__', 'node_modules', '.venv'}


def release_files(root):
    root = Path(root).resolve()
    selected = [root / name for name in TOP_FILES]
    for tree in TREES:
        selected.extend(path for path in (root / tree).rglob('*') if path.is_file())
    result = []
    for path in selected:
        relative = path.relative_to(root)
        if relative.parts[:2] == ('evaluations', 'results'):
            continue
        if EXCLUDED_PARTS.intersection(relative.parts) or path.suffix in ('.pyc', '.pyo') or path.name == '.DS_Store':
            continue
        if path.is_symlink() or not path.resolve().is_relative_to(root) or not path.is_file():
            raise ValueError(f'Not a local regular release file: {relative}')
        result.append(path)
    return sorted(result, key=lambda path: path.relative_to(root).as_posix())


def build_archive(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if any(output.is_relative_to(root / tree) for tree in TREES):
        raise ValueError('Release output must be outside all included source trees')
    version = (root / 'VERSION').read_text().strip()
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-z0-9.]+)?', version):
        raise ValueError('VERSION must contain a semantic release version')
    files = release_files(root)
    output.mkdir(parents=True, exist_ok=True)
    path = output / f'craft-crm-{version}.zip'
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for file in files:
            name = 'craft-crm/' + file.relative_to(root).as_posix()
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, file.read_bytes(), compresslevel=9)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    path.with_suffix('.zip.sha256').write_text(f'{digest}  {path.name}\n')
    return path, digest, len(files)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    validator = runpy.run_path(str(ROOT / 'skills/craft-crm/scripts/validate_bundle.py'))['validate']
    result = validator(ROOT / 'skills/craft-crm')
    if not result['valid']:
        print('\n'.join(result['errors']), file=sys.stderr)
        return 1
    check = subprocess.run([sys.executable, '-B', '-m', 'unittest', 'discover', '-s', str(ROOT / 'tests')])
    if check.returncode:
        return check.returncode
    try:
        path, digest, count = build_archive(ROOT, args.output)
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print(f'Created {path}\nFiles: {count}\nSHA-256: {digest}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
