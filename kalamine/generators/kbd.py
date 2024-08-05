"""
GNU/Linux: KBD
- keyboard table description for loadkeys and dumykeys
"""

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from ..layout import KeyboardLayout

from ..utils import LAYER_KEYS, ODK_ID, SCAN_CODES, Layer, upper_key

def kbd_keymap(layout: "KeyboardLayout") -> str:
    
    for key_name in LAYER_KEYS:
        if key_name.startswith("-"):
            continue

        chars = list("")
        for i in [Layer.BASE, Layer.SHIFT, Layer.ALTGR, Layer.ALTGR_SHIFT]:
            if key_name in layout.layers[i]:
                chars.append(layout.layers[i][key_name])

        print(chars)
    
    return ":)"
