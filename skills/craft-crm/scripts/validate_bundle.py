#!/usr/bin/env python3
"""Validate local bundle files and metadata; never fetch URLs or execute bundle code."""
import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

REQUIRED = (
    'SKILL.md', 'LICENSE', 'agents/openai.yaml', 'assets/icon.svg',
    'assets/direction-board.svg', 'assets/tokens.css',
    'assets/build-contract.md', 'assets/audit-template.json',
    'scripts/validate_bundle.py', 'scripts/score_audit.py',
    *(f'references/{name}.md' for name in (
        'foundations', 'component-specs', 'domain-adapters', 'directions',
        'patterns', 'anti-slop', 'revamp', 'implementation', 'quality-gates',
        'examples', 'sources', 'research-method', 'search-results', 'popovers')),
    'references/sources.json',
)
WEIGHTS = dict(workflow=25, architecture=15, composition=20,
               consistency=15, accessibility=15, resilience=10)


def validate(root):
    root = Path(root).resolve()
    errors = []

    def read(relative):
        path = root / relative
        if not path.resolve().is_relative_to(root) or path.is_symlink():
            errors.append(f'{relative}: must be a local regular file')
            return ''
        try:
            return path.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as error:
            errors.append(f'{relative}: {error}')
            return ''

    def read_json(relative):
        content = read(relative)
        if not content:
            return None
        try:
            return json.loads(content)
        except ValueError as error:
            errors.append(f'{relative}: invalid JSON: {error}')
            return None

    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f'missing {relative}')
    skill = read('SKILL.md')
    front = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', skill, re.S)
    if not front:
        errors.append('SKILL.md: missing YAML frontmatter')
    else:
        # This bundle uses plain scalar fields, not arbitrary YAML constructs.
        fields = dict(re.findall(r'^(name|description):\s*(\S[^\n]*)$', front[1], re.M))
        if fields.get('name', '').strip('\"\'') != 'craft-crm':
            errors.append('SKILL.md: name must be craft-crm')
        if not fields.get('description', '').strip('\"\' '):
            errors.append('SKILL.md: description is required')
    if len(skill.splitlines()) >= 500:
        errors.append('SKILL.md must remain below 500 lines')

    corpus = read_json('references/sources.json')
    records = corpus.get('sources') if isinstance(corpus, dict) else None
    if not isinstance(records, list) or not records:
        errors.append('sources.json: sources must be a nonempty list')
        records = []
    ids, urls = set(), set()
    for index, record in enumerate(records):
        label = f'sources[{index}]'
        if not isinstance(record, dict):
            errors.append(f'{label}: must be an object')
            continue
        for field in ('id', 'title', 'url', 'category', 'evidence', 'reviewed_at',
                      'status', 'observation', 'application', 'limitation'):
            if not isinstance(record.get(field), str) or not record[field].strip():
                errors.append(f'{label}: missing or invalid {field}')
        source_id = record.get('id')
        if not isinstance(source_id, str) or not re.fullmatch(r'S\d{2,}', source_id):
            errors.append(f'{label}: invalid source ID')
        elif source_id in ids:
            errors.append(f'{label}: duplicate source ID {source_id}')
        else:
            ids.add(source_id)
        url = record.get('url')
        if isinstance(url, str):
            try:
                parsed = urlsplit(url)
                valid_url = parsed.scheme == 'https' and bool(parsed.hostname)
            except ValueError:
                valid_url = False
            if not valid_url:
                errors.append(f'{label}: source must have an absolute HTTPS URL')
            canonical = url.rstrip('/')
            if canonical in urls:
                errors.append(f'{label}: duplicate source URL {url}')
            urls.add(canonical)
        try:
            date.fromisoformat(record.get('reviewed_at', ''))
        except (TypeError, ValueError):
            errors.append(f'{label}: reviewed_at must be an ISO date')

    for file in sorted(root.rglob('*.md')):
        relative = str(file.relative_to(root))
        content = read(relative)
        if '[TODO' in content:
            errors.append(f'{relative}: scaffold TODO')
        for ref in re.findall(r'\bS\d{2,}\b', content):
            if ref not in ids:
                errors.append(f'{relative}: unknown source {ref}')
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if target.startswith(('https://', 'http://', '#')):
                continue
            path = (file.parent / unquote(target.split('#')[0])).resolve()
            if not path.is_relative_to(root):
                errors.append(f'{relative}: local link escapes skill: {target}')
            elif not path.exists():
                errors.append(f'{relative}: broken local link {target}')

    audit = read_json('assets/audit-template.json')
    if not isinstance(audit, dict):
        errors.append('audit-template.json: must be an object')
    else:
        gates, dimensions = audit.get('gates'), audit.get('dimensions')
        if not isinstance(gates, list) or not all(isinstance(g, dict) for g in gates):
            errors.append('audit-template.json: invalid gates')
        elif sorted(str(g.get('id')) for g in gates) != [f'G{i:02}' for i in range(1, 8)]:
            errors.append('audit-template.json: exactly G01–G07 are required')
        elif any(g.get('status') != 'unknown' for g in gates):
            errors.append('audit-template.json: blank gates must be unknown')
        if not isinstance(dimensions, list) or not all(isinstance(d, dict) for d in dimensions):
            errors.append('audit-template.json: invalid dimensions')
        elif sorted(str(d.get('id')) for d in dimensions) != sorted(WEIGHTS):
            errors.append('audit-template.json: exactly six scoring dimensions are required')
        elif any(d.get('weight') != WEIGHTS[d['id']] or d.get('score') is not None
                 for d in dimensions):
            errors.append('audit-template.json: incorrect weights or prefilled scores')

    # JSON is a YAML subset: validate exact syntax/parents without a YAML dependency.
    metadata = read_json('agents/openai.yaml')
    interface = metadata.get('interface') if isinstance(metadata, dict) else None
    if not isinstance(interface, dict):
        errors.append('agents/openai.yaml: interface must be an object')
        interface = {}
    for field in ('display_name', 'short_description', 'default_prompt', 'icon_small', 'icon_large'):
        if not isinstance(interface.get(field), str) or not interface[field].strip():
            errors.append(f'agents/openai.yaml: {field} must be a nonempty string')
    short = interface.get('short_description')
    if isinstance(short, str) and not 25 <= len(short) <= 64:
        errors.append('agents/openai.yaml: short_description must contain 25–64 characters')
    prompt = interface.get('default_prompt')
    if isinstance(prompt, str) and '$craft-crm' not in prompt:
        errors.append('agents/openai.yaml: default_prompt must mention $craft-crm')
    policy = metadata.get('policy') if isinstance(metadata, dict) else None
    if not isinstance(policy, dict) or type(policy.get('allow_implicit_invocation')) is not bool:
        errors.append('agents/openai.yaml: invocation policy must be boolean')
    for field in ('icon_small', 'icon_large'):
        icon = interface.get(field)
        if isinstance(icon, str):
            path = (root / icon).resolve()
            if not path.is_relative_to(root) or not path.is_file():
                errors.append(f'agents/openai.yaml: invalid icon path {icon}')
    for relative in ('assets/icon.svg', 'assets/direction-board.svg'):
        try:
            svg = ET.fromstring(read(relative))
            if svg.tag.rsplit('}', 1)[-1] != 'svg':
                errors.append(f'{relative}: root must be svg')
            for element in svg.iter():
                if element.tag.rsplit('}', 1)[-1].lower() == 'script':
                    errors.append(f'{relative}: embedded script')
                for attr, value in element.attrib.items():
                    if attr.rsplit('}', 1)[-1].lower().startswith('on') or value.strip().lower().startswith('javascript:'):
                        errors.append(f'{relative}: executable SVG attribute')
        except ET.ParseError as error:
            errors.append(f'{relative}: invalid SVG: {error}')
    return dict(valid=not errors, resources=len(records), errors=errors)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    result = validate(parser.parse_args(argv).root)
    print(json.dumps(result, indent=2))
    return 0 if result['valid'] else 1


if __name__ == '__main__':
    sys.exit(main())
