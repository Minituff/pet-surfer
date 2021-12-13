## Main design
* Use a under cabinet mounted device with a camera facing the counter-tops
* Use AI to determine if a pet is on the counter
	* Hopefully AI can also tell the color of the pet just in case there are multiple dogs
* Use a collar mounted device which can be shocked/buzzed/noisy if the AI finds they are on the counter
* Use bleutooth LE to detect presense which also helps with false positives

To View the AI pet detection visit:
http://<your-ip>:8000

## Useful Links
* [Pet Detection YouTube Link](https://www.youtube.com/watch?v=gGqVNuYol6o&t=5s)
* [L1 Linux Guides](https://forum.level1techs.com/t/bluetooth-presence-detection-for-home-automation-the-level1-way/148516) and [YouTube Link](https://www.youtube.com/watch?v=7vm7oL4JDi8*)
* [Monitor](https://github.com/andrewjfreyer/monitor) - MQTT trigger of detection
* [BlyPy](https://github.com/IanHarvey/bluepy)
* Enable RDP [Video](https://www.youtube.com/watch?v=IfzBPi4FHpI)
* Sending Texts Free [Youtube](https://www.youtube.com/watch?v=4-ysecoraKo)   - [Python Script](https://www.reddit.com/r/Python/comments/8gb88e/free_alternatives_to_twilio_for_sending_text/)
* [Capstone](https://gitlab.com/mark-matura/ble-ips-rpi-client)
* [Beacons Indian nice video](https://www.youtube.com/watch?v=keruN9f92so)
* [iBeacon](https://www.hackster.io/memoryleakyu/diy-ibeacon-and-beacon-scanner-with-raspberry-pi-and-hm13-fe558a)

### A somewhat working BT LE Setep
Follow [this](https://www.thepolyglotdeveloper.com/2018/03/use-nodejs-raspberry-pi-zero-w-scan-ble-ibeacon-devices/) guide. (esure monitor is *not* running or this will break noble)
Fix for Raspberry PI [here](https://github.com/noble/node-bluetooth-hci-socket/issues/107)



## Run Node.js script as service
Stack Overflow [instructions](https://stackoverflow.com/questions/60100830/how-should-i-start-a-node-js-script-automatically)
