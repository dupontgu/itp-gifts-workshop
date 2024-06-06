# Gifts workshop ft. CircuitPython & Val Town

## Goals
* Get CircuitPython installed on WiFi enabled microcontroller board.
* Explore/modify example CircuitPython apps
* Set up Val Town account and create a "val" (function) that can be accessed by a standard HTTPS web call
* Communicate between CircuitPython and Val Town apps

## Things You'll Need
1. LOLIN S2 Mini development board (see below)
1. Computer with Google Chrome installed
1. USB cable to connect development board and computer

## Hardware Introduction

#### LOLIN S2 Mini
An [ESP32-S2](https://www.espressif.com/en/products/socs/esp32-s2) WiFi development board

<img width="550" src=".docs/s2mini.jpeg">

Available on [Amazon](https://www.amazon.com/s?k=s2+mini)
and (even cheaper) on [AliExpress](https://www.aliexpress.us/w/wholesale-s2-mini.html?spm=a2g0o.home.search.0).

### Features
* Reset button (labeled `RST`, top right)
    * Restarts the code running on the ESP32
* "Boot" button (labeled `0`, top-left)
    * When held while reset is pressed/released, this will put the ESP32 into bootloader mode, which allows new code to be "flashed" to it from the computer.
    * **You can use this button to perform actions in your code!** It is attached to ESP32 pin 0.
* LED (white rectangle between boot button and USB port)
    * You can turn it on off from your code. It is attached to ESP32 pin 15.
* GPIO pins (32 silver lined holes on either side)
    * Can be used to hook up external components (sensors, displays, etc)
    * We won't be using these in this workshop

## Installing CircuitPython
1. **In Google Chrome** (other browsers don't work yet), navigate to the [CircuitPython installer page for for LOLIN S2 Mini](https://circuitpython.org/board/lolin_s2_mini/)
<img width="550" src=".docs/s2mini_cpy_landing.png">

2. Plug your S2 Mini into your computer using its USB-C port.
2. After it is plugged in, **hold the boot button (`0`) and -while holding- press and release the reset button (`RST`).** Release the boot button.
2. On the CircuitPython web page, click the `Open Installer` button.
<img width="550" src=".docs/s2mini_cpy_openInstall.png">

5. Click `Full CircuitPython 9.X.X Install`
5. Click `Next` then `Connect`
<img width="550" src=".docs/s2mini_cpy_connect.png">

7. Select your ESP32-S2 device from Chrome's drop down menu and click `Connect`.
7. When you are asked to "overwrite everything" on the device, click `Continue`.
7. Installation will begin:
<img width="550" src=".docs/s2mini_cpy_erase.png">
<img width="550" src=".docs/s2mini_cpy_flashing.png">

10. When flashing is done, hit the reset (`RST`) button.
10. Click `Select S2MINIBOOT Drive`, and find the the drive named `S2MINIBOOT` that should now be mounted to your computer. **DO NOT SELECT ANY OTHER DRIVE - IF YOU ARE UNSURE, BAIL!**
10. If prompted, allow the site to `Edit Files`
<img width="550" src=".docs/s2mini_cpy_allowEdit.png">

13. Observe that the `S2MINIBOOT` drive has been unmounted, and a new drive named `CIRCUITPY` has appeared (may take a minute, hit the reset button if it doesn't show).
13. **At this point, CircuitPython is installed and the rest of the Installer steps are optional. We're going to skip them for this workshop.**

## Using CircuitPython

### To update your CircuitPython application, all you need to do is modify the `code.py` file on the `CIRCUITPY` drive and save it. When saved, the app will restart and your new code will be executed.

You can use any code editor to modify the files on `CIRCUITPY` but in this tutorial, we'll use the web editor since it does not require any installation and has a built in terminal so we can see our logs in real time.

1. With your dev board still connected, avigate to [code.circuitpython.org](https://code.circuitpython.org/)
1. Select `USB` (this is how the web page communicates with the dev board).
<img width="550" src=".docs/s2mini_cpy_usb.png">

3. Click `Connect to Device` and select your ESP32-S2 from Chrome's dropdown menu.
3. Click `Select New Folder` and select the root directory of your `CIRCUITPY` drive. **DO NOT SELECT ANY OTHER DRIVE/FOLDER**
<img width="550" src=".docs/s2mini_cpy_cpydrive.png">

5. Click `Open` and select the file `code.py`. The file will open in the embedded editor.
<img width="550" src=".docs/s2mini_cpy_hellowld.png">

6. Click on the `Serial` tab at the bottom of the page, observe that a terminal opens on the right side of the page. this is where our logs will show up! Some text may already be there.
6. Edit the print statement in `code.py` to say something else, like:
```print("Hello ITP")```
6. Click `Save`. Observe that the app restarts (the LED will flash a few times), and look for your updated log message in the terminal. **Congrats, you're a CircuitPython developer!**
<img width="550" src=".docs/s2mini_cpy_logs.png">

