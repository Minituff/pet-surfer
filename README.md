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

<br>

## Demo
<img title="detect.service" src="media/detect.gif" width="320" height="250"/>
<img title="led-ip.service" src="media/led-ip-demo.gif" width="250" height="250"/>


## Architecture
There are currently 3 linux services which are set to run at boot:
1. **noble.service** - Uses the Node.js [noble package](https://github.com/noble/noble) to detect Bluetooth LE beacons. When a beacon is within a certain distance (configurable), turn on the 🔴**RED** light.
2. **detect.service** - Uses [Tensorflow Lite](https://www.tensorflow.org/lite) to detect the presence of a cat/dog. When a pet is detected for a certain amount of frames (configurable), turn on the 🟡**YELLOW** light. A [Flask](https://flask.palletsprojects.com/) server is also run to view a real-time camera feed plus the AI detection. To see, go here: **http://pi-ip-address:8000**
3. **led-ip.service** - Runs a python scrpt to *blink* the last octet of the Pi's IP address with the 🟢**GREEN** light.
	- This is if you [pre-load the WiFi](https://raspberrypi.stackexchange.com/questions/11631/how-to-setup-multiple-wifi-networks) information on the Raspberry PI and take it to another location, you can quickly identify the IP address to view the PI Cam output. (Not morse code)
	- Example IP address: 192.168.1.**152**
		- **1** blink -> pause -> **5** blinks -> pause -> **2** blinks -> steady on -> *repeat*
	- Blinking on and off with no pauses/steady-on means the Pi has **no** IP address
	- Three quick flashes equals a "0"

<br>

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

<br>

## Setup
### Setup Raspberry Pi
- Use the [Raspberry PI Imager](https://www.raspberrypi.com/software/)
	- The version I used was: `Raspbian GNU/Linux 11 (bullseye) 32bit` which was the default at the time
- Ensure you are using the `pi` user, unless you want to change ALL the paths
- Clone this Repo to your `Documents` folder
	```bash
	cd /home/pi/Documents
	git clone https://github.com/Minituff/pet-surfer.git
	```

<br>

### Install **noble.service**
1. Install dependencies for the noble service:
	```bash
	sudo apt-get install node 		# Install node.js
	cd noble
	npm install 					# Install dependencies
	sudo node app.js 				# Just test if the app works, if it does, quit and proceed to next step
	```
	- Here you should see the 🔴**RED** light turn on if the BlueCharm is in range
	- Quit the script (`ctrl + c`) and move on to the next step
1. Install, enable and activate the **noble.service**:
	```bash
	sudo cp services/noble.service /etc/systemd/system/
	sudo systemctl enable noble            
	sudo systemctl start noble
	sudo systemctl --no-page status noble  # Ensure the status is active
	```

<br>

### Install **detect.service** & **led-ip.service** requirements
1. Create Python Virtual Enviornment ([venv](https://docs.python.org/3/library/venv.html))
	```bash
	cd playground
	python3 -m venv /home/pi/.virtualenvs/playground-flql 	# playground-flql is the venv name
	```
	- I used [this](https://github.com/MichaelAquilina/zsh-autoswitch-virtualenv) module for my ZSH terminal
	- If you do not use a venv, then just change the `ExecStart` commands in each *.service* file
1. Activate the virtual env
	```bash
	source /home/pi/.virtualenvs/playground-flql/bin/activate
	```
	- You WILL need to do this every time you SSH into your PI, unless you use the plugin mentioned above, then the venv will be activated upon cd'ing into the playground folder.
1. Install requirements
	- Install Tensorflow lite using this [guide](https://www.tensorflow.org/lite/guide/python#install_tensorflow_lite_for_python) 
	- Install remaining reqs for the venv:
	```bash
	pip install -r requirements.txt 	# This will install the reqs for both scripts
	```

<br>

### Test & Install **detect.service**
1. Ensure your venv is active and you are in the `playground` folder
1. Test **detect.service**
	```bash
	python3 detect.py
	```
	- You should see the flask server start.
	- To View the AI pet detection visit: **http://your-pi-ip:8000**
	- Here you should see the 🟡**YELLOW** turn on if the AI detects a Pet.
	- Quit the script (`ctrl + c`) and move on to the next step
1. Install, enable and activate the **detect.service**:
	```bash
	sudo cp services/detect.service /etc/systemd/system/
	sudo systemctl enable detect            
	sudo systemctl start detect
	sudo systemctl --no-page status detect  # Ensure the status is active
	```

<br>

### Test & Install **led-ip.service**
1. Ensure your venv is active and you are in the `playground` folder
1. Test **led-ip.service**
	```bash
	python3 led-ip.py
	```
	- Here you should see the 🟢**GREEN** blink the PI's IP address (see above to decode)
	- Quit the script (`ctrl + c`) and move on to the next step
1. Install, enable and activate the **led-ip.service**:
	```bash
	sudo cp services/led-ip.service /etc/systemd/system/
	sudo systemctl enable led-ip            
	sudo systemctl start led-ip
	sudo systemctl --no-page status led-ip  # Ensure the status is active
	```

<br>
<br>
<br>

## Useful Links and other tutorials
These links and videos really helped me out:
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