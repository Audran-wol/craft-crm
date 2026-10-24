"""Measure the shipped palette; this does not certify a rendered application."""
from pathlib import Path
import re
import unittest

CSS = (Path(__file__).resolve().parents[1] / 'skills/craft-crm/assets/tokens.css').read_text()


def luminance(hex_color):
    channels = [int(hex_color[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in channels]
    return sum(a*b for a, b in zip(linear, (.2126, .7152, .0722)))


def contrast(a, b):
    light, dark = sorted((luminance(a), luminance(b)), reverse=True)
    return (light + .05) / (dark + .05)


def palette(selector, inherited=None):
    block = re.search(re.escape(selector) + r'\s*\{([^}]+)\}', CSS).group(1)
    result = dict(inherited or {})
    result.update(re.findall(r'--crm-([\w-]+):\s*(#[0-9a-fA-F]{6})\s*;', block))
    return result


class TokenTests(unittest.TestCase):
    def test_contrast_formula_reference_points(self):
        self.assertEqual(contrast('#000000', '#ffffff'), 21)
        self.assertEqual(contrast('#ffffff', '#ffffff'), 1)

    def test_light_and_dark_palette_pairs(self):
        light = palette(':root')
        pairs = (
            ('text', 'surface', 4.5), ('text-muted', 'surface', 4.5),
            ('text', 'canvas', 4.5), ('text-muted', 'canvas', 4.5),
            ('on-accent', 'accent', 4.5), ('success', 'success-bg', 4.5),
            ('warning', 'warning-bg', 4.5), ('danger', 'danger-bg', 4.5),
            ('control-border', 'surface', 3), ('focus', 'surface', 3),
            ('focus', 'canvas', 3),
        )
        for theme, colors in (('light', light), ('dark', palette('[data-crm-theme="dark"]', light))):
            for foreground, background, minimum in pairs:
                with self.subTest(theme=theme, foreground=foreground, background=background):
                    ratio = contrast(colors[foreground], colors[background])
                    self.assertGreaterEqual(ratio, minimum, f'{theme} {foreground}/{background}: {ratio:.2f}:1')


if __name__ == '__main__':
    unittest.main()
