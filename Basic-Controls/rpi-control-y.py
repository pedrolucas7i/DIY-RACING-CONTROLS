import time
import digitalio
import board
import usb_hid
from adafruit_hid.mouse import Mouse

# Configurações USB HID
mouse = Mouse(usb_hid.devices)

# Configurações dos pinos
w_pin = board.GP21
s_pin = board.GP2

w = digitalio.DigitalInOut(w_pin)
w.direction = digitalio.Direction.INPUT
w.pull = digitalio.Pull.UP

s = digitalio.DigitalInOut(s_pin)
s.direction = digitalio.Direction.INPUT
s.pull = digitalio.Pull.UP

# Resolução da tela
SCREEN_RESOLUTION_Y = 760

# Inicializar posição Y
pos_y = SCREEN_RESOLUTION_Y / 2

# Esperar 2 segundos antes de iniciar
time.sleep(2)

# Loop principal
while True:
    y = 0
    if not w.value:
        y = 1000
    if not s.value:
        y = -1000
    
    pos_y += y
    pos_y = max(0, min(pos_y, SCREEN_RESOLUTION_Y))
    
    if w.value and s.value:
        mouse.move(0, int(((SCREEN_RESOLUTION_Y / 2) - pos_y) / 2.4))
        pos_y = SCREEN_RESOLUTION_Y / 2
    else:
        mouse.move(0, int(y))
    
