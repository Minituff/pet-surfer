## Main design
This is a "shark tank" style product designed to keep your pets from getting on your counter-tops.
There currently are very few products that can do this with a clean user experience and high amount of customization.

This repo serves as a *Proof of Concept* to demonstrate that such a product could exist.

It would work like this:
* Use a under cabinet mounted device with a camera facing the counter-tops
* Use AI to determine if a pet is on the counter
	* Hopefully AI can also tell the color of the pet just in case there are multiple dogs
* Use a collar mounted device which can be shocked/buzzed/noisy if the AI finds they are on the counter
* Use bleutooth Low Energy beacons to detect presense which also helps with false positives


## Architecture
There are currently 3 linux services which are set to run at boot:
1. **noble.service** - Uses the Node.js [noble package](https://github.com/noble/noble) to detect Bluetooth LE beacons. When a beacon is within a certain distance (configurable), turn on the **RED** light.
2. **detect.service** - Uses [Tensorflow Lite](https://www.tensorflow.org/lite) to detect the presence of a cat/dog. When a pet is detected for a certain amount of frames (configurable), turn on the **YELLOW** light. A [Flask](https://flask.palletsprojects.com/) server is also run to view a real-time camera feed plus the AI detection. To see, go here: **http://pi-ip-address:8000**
3. **led-ip.service** - Runs a python scrpt to *blink* the last octet of the Pi's IP address.
	- This is if you [pre-load the WiFi](https://raspberrypi.stackexchange.com/questions/11631/how-to-setup-multiple-wifi-networks) information on the Raspberry PI and take it to another location, you can quickly identify the IP address to view the PI Cam output. (Not morse code)
	- Example IP address: 192.168.1.**152**
		- **1** blink -> pause -> **5** blinks -> pause -> **2** blinks -> steady on -> *repeat*
	- Blinking on and off with no pauses/steady-on means the Pi has **no** IP address
	- Three quick flashes equals a "0"

## Hardware
- [Raspberry PI 4 (Bundle)](https://www.amazon.com/gp/product/B07TKFKKMP/)
	- Includes a basic case, power supply, and heatsinks. *Optional, but recommended*
	- Used as the main *hub*.
- [Raspberry PI Camera Module](https://www.amazon.com/gp/product/B07M9Q43MX/)
	- A [USB webcam](https://www.amazon.com/dp/B004FHO5Y6/) will also work for this project, but may require small tweaks in the code.
	- For Tensorflow Lite AI pet detection
- [Pi Traffic Light](https://www.amazon.com/gp/product/B00RIIGD30/)
	- Used to *simulate* a pet has been detected.
	- These are nice because they do not require a breadboard
- [Bluetooth Beacon](https://www.amazon.com/gp/product/B085XN9B7N/)
	- For pet presence detection
	- This particular beacon is highly customizable. Setting the broadcast frequency increases the speed of pet detection at the cost of higher battery consumption.
- [Micro SD Card](https://www.amazon.com/gp/product/B07XDCZ9J3)
	- These are the ones I used, but anything greater than 16gb should work fine

To View the AI pet detection visit:
http://your-pi-ip:8000

## Useful Links and other tutorials
* [Pet Detection YouTube Link](https://www.youtube.com/watch?v=gGqVNuYol6o&t=5s)
* [L1 Linux Guides](https://forum.level1techs.com/t/bluetooth-presence-detection-for-home-automation-the-level1-way/148516) and [YouTube Link](https://www.youtube.com/watch?v=7vm7oL4JDi8*)
* [Monitor](https://github.com/andrewjfreyer/monitor) - MQTT trigger of detection
* [BlyPy](https://github.com/IanHarvey/bluepy)
* Enable RDP [Video](https://www.youtube.com/watch?v=IfzBPi4FHpI)
* Sending Texts Free [Youtube](https://www.youtube.com/watch?v=4-ysecoraKo)   - [Python Script](https://www.reddit.com/r/Python/comments/8gb88e/free_alternatives_to_twilio_for_sending_text/)
* [Capstone](https://gitlab.com/mark-matura/ble-ips-rpi-client)
* [Beacons - nice video](https://www.youtube.com/watch?v=keruN9f92so)
* [iBeacon](https://www.hackster.io/memoryleakyu/diy-ibeacon-and-beacon-scanner-with-raspberry-pi-and-hm13-fe558a)

### A somewhat working BT LE Setep
Follow [this](https://www.thepolyglotdeveloper.com/2018/03/use-nodejs-raspberry-pi-zero-w-scan-ble-ibeacon-devices/) guide. (esure monitor is *not* running or this will break noble)
Fix for Raspberry PI [here](https://github.com/noble/node-bluetooth-hci-socket/issues/107)



## Run Node.js script as service
Stack Overflow [instructions](https://stackoverflow.com/questions/60100830/how-should-i-start-a-node-js-script-automatically)
