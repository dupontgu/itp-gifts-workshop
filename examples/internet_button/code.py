from examples.internet_button.csv import CsvReader
import time
import board
import digitalio
import wifi
import adafruit_requests
import adafruit_connection_manager
import socketpool
import ssl

print("Running internet button example") 

ID = "Internet Button"
ENDPOINT = f"https://dupontgu-ambermollusk.web.val.run/?id={ID}"

button = digitalio.DigitalInOut(board.BUTTON)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

credentials_csv = CsvReader("examples/internet_button/credentials.csv")
# expecting credentials to be in the first row after the headers
wifi_creds = credentials_csv[0]
ssid = wifi_creds['WiFi SSID']
pwd = wifi_creds['WiFi Password']

def blink_led(times):
    for _ in range(times):
        led.value = True
        time.sleep(0.2)
        led.value = False
        time.sleep(0.2)

# Connect to WiFi
def connect_to_wifi():
    print("Connecting to WiFi...")
    wifi.radio.connect(ssid, pwd)
    print("Connected to WiFi")

blink_led(1)

while True:
    try:
        connect_to_wifi()
        break
    except Exception as e:
        blink_led(4)
        print("Failed to connect to WiFi, retrying in 5 seconds...")
        time.sleep(5)

blink_led(2)

pool = adafruit_connection_manager.get_radio_socketpool(wifi.radio)
ssl_context = adafruit_connection_manager.get_radio_ssl_context(wifi.radio)
requests = adafruit_requests.Session(pool, ssl_context)

def update_server():
    print("updating server")
    led.value = True
    try:
        response = requests.get(ENDPOINT)
        print("Response:", response.text)
    except Exception as e:
        print("Failed to update server:", e)
    led.value = False

print("Ready to detect button press.")

while True:
    if not button.value: # since the button has a pull-up, 'not' means pressed
        update_server()
        while not button.value:
            pass
    time.sleep(0.1)

