import board
import digitalio
import time

print("Running Blinky Toggle Example")

button = digitalio.DigitalInOut(board.BUTTON)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

last_button_state = button.value

while True:
    current_button_state = button.value
    if (current_button_state != last_button_state):
        if not current_button_state:
            led.value = not led.value
            print(f"Turned LED {'on' if led.value else 'off'}")
    last_button_state = current_button_state
    time.sleep(0.01)