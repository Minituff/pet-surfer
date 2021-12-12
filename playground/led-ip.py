import socket
from time import sleep

from gpiozero import LED, Device
from gpiozero.pins.native import NativeFactory
from netifaces import AF_INET, ifaddresses, interfaces

Device.pin_factory = NativeFactory()

greenLED = LED(11)


def blink_num(num):
    for int in range(0,num):
        greenLED.on()
        sleep(0.4)
        greenLED.off()
        sleep(0.4)

while True:
    for ifaceName in interfaces():
        if (ifaceName == "wlan0"): # eth0 for lan, wlan0 for wifi
            address = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':None}] )][0]
            if (address is None):
                greenLED.on()
                sleep(1.5)
                greenLED.off()
                sleep(1.5)
            else:
                print("Your IP is: " + address)
                sleep(0.5)
                last_octet = address.split('.')[3]
                if len(last_octet) == 1: 
                    blink_num(int(last_octet))
                elif len(last_octet) == 2:
                    blink_num(int(last_octet[0]))
                    sleep(3)
                    blink_num(int(last_octet[1]))
                else:
                    blink_num(int(last_octet[0]))
                    sleep(3)
                    blink_num(int(last_octet[1]))
                    sleep(3)
                    blink_num(int(last_octet[2]))
                
                greenLED.on()
                sleep(5)
                greenLED.off()
                sleep(0.7)
