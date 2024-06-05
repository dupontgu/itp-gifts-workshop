import usb_midi
import usb_hid

USE_MIDI_INSTEAD_OF_HID = True

if (USE_MIDI_INSTEAD_OF_HID):
    usb_hid.disable() 
    usb_midi.enable() 
else:
    usb_hid.enable() 
    usb_midi.disable() 