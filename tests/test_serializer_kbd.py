from textwrap import dedent

from kalamine import KeyboardLayout
from kalamine.generators.kbd import kbd_keymap

from .util import get_layout_dict


def load_layout(filename: str) -> KeyboardLayout:
    return KeyboardLayout(get_layout_dict(filename))


def split(multiline_str: str):
    return dedent(multiline_str).lstrip().rstrip().splitlines()


def test_ansi():
    layout = load_layout("ansi")

    expected = ":)"
    kbdkeymap = kbd_keymap(layout)

    assert len(kbdkeymap) == len(expected)
    assert kbdkeymap == expected
