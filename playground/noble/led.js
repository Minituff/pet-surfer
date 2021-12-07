const Gpio = require('onoff').Gpio; // Gpio class

const led = new Gpio(19, 'out');


led.writeSync(0);


while (true){}

led.unexport();    // Unexport GPIO and free resources
