import time
import digitalio
import board
import busio
import adafruit_mpu6050
import math
import usb_hid
from adafruit_hid.mouse import Mouse

# Configurações I2C
i2c = busio.I2C(board.GP27, board.GP26)
mpu = adafruit_mpu6050.MPU6050(i2c)

# Configurações USB HID
mouse = Mouse(usb_hid.devices)

# Sensibilidade do mouse e resolução da tela
MOUSE_SENSITIVITY_X = 0.2
SCREEN_RESOLUTION_X = 1360
pos_x = SCREEN_RESOLUTION_X / 2

# Esperar 2 segundos antes de iniciar
time.sleep(2)

# Loop principal
while True:
    x = 0
    move_x = math.atan2(mpu.acceleration[1], mpu.acceleration[2]) * (180 / math.pi)
    if move_x > 20:
        x = SCREEN_RESOLUTION_X
    elif move_x < -20:
        x = -SCREEN_RESOLUTION_X
    
    pos_x += x
    pos_x = max(0, min(pos_x, SCREEN_RESOLUTION_X))
    
    if x == 0:
        mouse.move(int(((SCREEN_RESOLUTION_X / 2) - pos_x) / 2.4), 0)
        pos_x = SCREEN_RESOLUTION_X / 2
    else:
        mouse.move(int(x), 0)


