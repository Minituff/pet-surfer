//const Noble = require("noble");
//const noble = require('@abandonware/noble');
const BeaconScanner = require("node-beacon-scanner");
const Gpio = require('onoff').Gpio;

const redLed = new Gpio(9, 'out');
// const yellowLed = new Gpio(10, 'out')
// const greenLed = new Gpio(11, 'out')

function gracefulShutdown(){
  console.log("\nGracefully shutting down...");

  redLed.write(0);
  // yellowLed.write(0);
  // greenLed.write(0);
  redLed.unexport();    // Unexport GPIO and free resources
  // yellowLed.unexport();    // Unexport GPIO and free resources
  // greenLed.unexport();    // Unexport GPIO and free resources

  console.log("Exiting...");
};

process.on('SIGTERM', function() {
  console.log('Got SIGTERM signal');
  gracefulShutdown();
  process.exit(0)
});

process.on('SIGINT', function() {
  gracefulShutdown();
});

var scanner = new BeaconScanner();

scanner.onadvertisement = (advertisement) => {
    var beacon = advertisement["iBeacon"];
    if (beacon){
    	beacon.rssi = advertisement["rssi"];
    	//console.log(JSON.stringify(beacon, null, "    "))
    	console.log(beacon.rssi)

	if (beacon.rssi >= -60){
	  redLed.write(1)
	  // greenLed.write(0)
	  // yellowLed.write(0)
	} else if (beacon.rssi <= -61 && beacon.rssi >= -85) {
	  // yellowLed.write(1)
	  redLed.write(0)
	  // greenLed.write(0)
	} else {
	  // greenLed.write(1)
	  redLed.write(0)
	  // yellowLed.write(0)
	}
    }
};

scanner.startScan().then(() => {
    console.log("Scanning for BLE devices...")  ;
}).catch((error) => {
    console.error(error);
});
