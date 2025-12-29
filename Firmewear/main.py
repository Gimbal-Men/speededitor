from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# MATRIX

keyboard.col_pins = (keyboard.GP0, keyboard.GP1, keyboard.GP2)
keyboard.row_pins = (keyboard.GP3, keyboard.GP4, keyboard.GP6, keyboard.GP7)
keyboard.diode_orientation = keyboard.DIODE_COL2ROW

# ENCODERS


encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    ((keyboard.GP26, keyboard.GP27),), 
    ((keyboard.GP28, keyboard.GP29),), 
)

# Encoder behavior per layer
encoder_handler.map = (
    # ---------- Layer 0: NORMAL ----------
    (
        (KC.J, KC.L),      
        (KC.EQUAL, KC.MINUS),
    ),

    # ---------- Layer 1: FINE JOG ----------
    (
        (KC.LEFT, KC.RIGHT), 
        (KC.NO, KC.NO),
    ),

    # ---------- Layer 2: CLIP MOVE ----------
    (
        (KC.NO, KC.NO),
        (KC.COMMA, KC.DOT), 
    ),
)

# KEYMAPS

keyboard.keymap = [

    # ===== Layer 0: Normal =====
    [
        KC.Z,        KC.COMMA,   KC.DOT,        # Undo | Prev | Next
        KC.UP,       KC.MO(1),   KC.DOWN,       # Up | ENC1 Push | Down
        KC.I,        KC.O,       KC.MO(2),      # In | Out | ENC2 Push
        KC.X,        KC.BSPACE,  KC.V,          # Cut | Ripple | Append
    ],

    # ===== Layer 1: Fine Jog (ENC1 held) =====
    [
        KC.NO, KC.NO, KC.NO,
        KC.NO, KC.SPACE, KC.NO,
        KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO,
    ],

    # ===== Layer 2: Clip Move (ENC2 held) =====
    [
        KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.ENTER,
        KC.NO, KC.NO, KC.NO,
    ],
]

# START

if __name__ == '__main__':
    keyboard.go()
