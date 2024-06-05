import time
import board
import digitalio
import pwmio
import usb_midi
import adafruit_midi
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_on import NoteOn

print("Running Web UI example")

MIDI_MSG_LED_TOGGLE = 0
MIDI_MSG_LED_BRIGHTNESS = 1

led = pwmio.PWMOut(board.LED, frequency=5000, duty_cycle=0)
midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], midi_out=usb_midi.ports[1], out_channel=0)

button = digitalio.DigitalInOut(board.BUTTON)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

led_state = False
brightness = 0.5
last_button_state = button.value

def enable_led(enable):
    global led_state
    led_state = enable
    if led_state:
        led.duty_cycle = int(brightness * brightness * 65535)
    else:
        led.duty_cycle = 0
    midi.send(ControlChange(MIDI_MSG_LED_TOGGLE, 127 if led_state else 0))

def handle_midi_message(message):
    global brightness
    if message is None or not isinstance(message, ControlChange):
        return
    if (message.control == MIDI_MSG_LED_BRIGHTNESS):
        brightness = message.value / 127.0
        enable_led(led_state)
    elif (message.control == MIDI_MSG_LED_TOGGLE):
        enable_led(message.value > 0)
    
enable_led(led_state)
midi.send(ControlChange(MIDI_MSG_LED_BRIGHTNESS, round(brightness * 127)))
while True:
    handle_midi_message(midi.receive())
    current_button_state = button.value
    if current_button_state != last_button_state:
        if not current_button_state:
            enable_led(not led_state)

    last_button_state = current_button_state
    time.sleep(0.01)  # Small delay to avoid excessive CPU usage
