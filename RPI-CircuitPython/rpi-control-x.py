import time
import board
import busio
import math
import usb_hid
import adafruit_mpu6050
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Configurações I2C
i2c = busio.I2C(board.GP27, board.GP26)
mpu = adafruit_mpu6050.MPU6050(i2c)

# Configurações USB HID
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# Esperar 2 segundos antes de iniciar
time.sleep(2)

# Loop principal
while True:
    x = 0
    move_x = math.atan2(mpu.acceleration[1], mpu.acceleration[2]) * (180 / math.pi)

    if move_x > 20:
        keyboard.press(Keycode.D)
    elif move_x < -20 :
        keyboard.press(Keycode.A)

    if move_x > 30:
        keyboard.press(Keycode.D)
        time.sleep(0.05)
    elif move_x < -30 :
        keyboard.press(Keycode.A)
        time.sleep(0.05)

    if move_x > 40:
        keyboard.press(Keycode.D)
        time.sleep(0.1)
    elif move_x < -40 :
        keyboard.press(Keycode.A)
        time.sleep(0.1)

    if move_x > 50:
        keyboard.press(Keycode.D)
        time.sleep(0.2)
    elif move_x < -50 :
        keyboard.press(Keycode.A)
        time.sleep(0.2)

    keyboard.release_all()

