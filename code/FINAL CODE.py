from ble_keyboard import BLEKeyboard
from machine import Pin
import time

kb = BLEKeyboard("ESPMIDIMS")

# -------------------------
# LED
# -------------------------
led = Pin(2, Pin.OUT)

# -------------------------
# PERFORMANCE KEYS (A–L)
# -------------------------
key_map = {
    "a": Pin(18, Pin.IN, Pin.PULL_UP),
    "s": Pin(5, Pin.IN, Pin.PULL_UP),
    "d": Pin(4, Pin.IN, Pin.PULL_UP),
    "f": Pin(22, Pin.IN, Pin.PULL_UP),
    "g": Pin(21, Pin.IN, Pin.PULL_UP),
    "h": Pin(19, Pin.IN, Pin.PULL_UP),
    "j": Pin(26, Pin.IN, Pin.PULL_UP),
    "k": Pin(27, Pin.IN, Pin.PULL_UP),
    "l": Pin(14, Pin.IN, Pin.PULL_UP),
}

last_state = {k: 1 for k in key_map}

# -------------------------
# CONTROL BUTTONS
# -------------------------
control_pins = [
    Pin(12, Pin.IN, Pin.PULL_UP),
    Pin(13, Pin.IN, Pin.PULL_UP),
    Pin(32, Pin.IN, Pin.PULL_UP),j
    Pin(33, Pin.IN, Pin.PULL_UP),
]

last_ctrl = [1, 1, 1, 1]
ctrl_state = [0, 0, 0, 0]

# -------------------------
# ACTIONS
# -------------------------
CONTROL_ACTIONS = [
    ['q', 'n', 'm'],
    ['r', '2', '3'],
    ['i', '4', '5'],
    ['b', '6', '7'],
]

print("Ableton controller ready")

# -------------------------
# LED BLINK FUNCTION
# -------------------------
def blink_led():
    for _ in range(4):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
    led.on()  # stays ON always

# -------------------------
# MAIN LOOP
# -------------------------
while True:
    if kb.is_connected():

        # =====================
        # PERFORMANCE KEYS
        # =====================
        for k, pin in key_map.items():
            curr = pin.value()

            if curr == 0 and last_state[k] == 1:
                kb.type_text(k)
                time.sleep_ms(40)

            last_state[k] = curr

        # =====================
        # CONTROL BUTTONS
        # =====================
        for i, pin in enumerate(control_pins):
            curr = pin.value()

            if curr == 0 and last_ctrl[i] == 1:

                time.sleep_ms(50)
                if pin.value() == 0:

                    # 🔴 BLINK ONLY on 2nd step (step 1)
                    if ctrl_state[i] == 1:
                        blink_led()

                    # 🎹 send key
                    action = CONTROL_ACTIONS[i][ctrl_state[i]]
                    kb.type_text(action)

                    # 🔁 advance cycle (0 → 1 → 2 → 0)
                    ctrl_state[i] = (ctrl_state[i] + 1) % 3

                    print("Instrument", i+1, "Sent:", action)

                    time.sleep_ms(150)

            last_ctrl[i] = curr

    time.sleep_ms(20)