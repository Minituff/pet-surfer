import time

from beacontools import BeaconScanner, IBeaconFilter, IBeaconAdvertisement

def callback(bt_addr, rssi, packet, additional_info):
    print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))

while True:
	print("Scanning")
	scanner = BeaconScanner(callback)
	scanner.start()
	time.sleep(5)
	scanner.stop()
