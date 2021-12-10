from time import sleep

from gpiozero import LED, Device
from gpiozero.pins.native import NativeFactory

Device.pin_factory = NativeFactory()

redLED = LED(9)
yellowLED = LED(10)
greenLED = LED(11)

while True:
    redLED.on()
    sleep(1)
    redLED.off()
    sleep(1)
