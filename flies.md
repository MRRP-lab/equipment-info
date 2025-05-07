Getting Started with CrazyFlies
-------------------------------
We have tons of working CrazyFlie drones. Use them responsibly.
# Building a CrazyFlie
- We still have some CrazyFlie kits that haven't been assembled yet. See assembly instructions [here](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/#assembling)
- Some pieces are fragile. Be very careful.

# Flying Manually

## Mobile
- You can download a mobile app called the CrazyFlie client to control a single drone using low energy Bluetooth, available on both iPhone and Android. Also see official instructions [here](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/#controlling-the-crazyflie).

## PC
- To control a drone from a PC environment, you must have a few things:
  1. The CrazyFlie client set up and ready to go. You need special permissions to use the client because it needs to be able to scan the USB ports; either use root on your own machine or use one of the Ubuntu machines in the robotics lab.
  2. Some kind of controller (We have 3 white Xbox controllers.)
  3. A way to communicate with the drone wirelessly. Our equipment comes with Crazyradio 2.0 adapters you can plug into a USB port.

Some things to watch out for here during setup:
- Permissions to scan the USB ports.
- Some students have tried using the client on a virtual machine, and they needed access to the vboxusers group. The command to do this is `sudo usermod -a -G vboxusers $USER`.
- After the client is set up, you might need to set the proper input mapping. Some of them are messed up and the drone will just immediately begin to fly up and away. Watch out for that. It seems that **PS3_Mode_1** is one of the most reasonable mappings. You'll only need to bind the assisted flight button if you need to use that (You'd also need a flow deck on your drone.)
- You'll notice that the client has some readings for things like link quality, battery, state estimation (thrust, x, y, and z,), among other things.
- Certain input mappings seem to have have a default (nonzero) control for yaw, pitch, roll, and even thrust. So if you don't notice it and immediately give it thrust, it will veer off in some direction, or it might just veer off immediately as you connect which is really bad.
- To enable advanced flight: While not connected to a drone, see the menu on the left and change "Flight mode" to "Advanced." This just allows you to set certain flight control parameters.

- See more [here](https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/userguides/userguide_client) and [here](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/#config-client)

# Controlling Many CrazyFlies

- IN-PROGRESS. There's no manual control of many at once without writing a program to do so. You'll need some special permissions to do so, because there's more risk involved with flying many at once. 
- There seems to be an issue where multiple crazyflie drones in the same area have the exact same radio controller address, leading to pairing issues. BUT. Sometimes it works and you can control multiple drones at the same time. Not recommended for manual control for any reason.

# Programming a CrazyFlie

- It boils down to downloading the firmware release for the crazyflie and modifying it to your needs, then flashing it back to a drone using a crazyradio dongle. Can NOT be done over USB. Must be over radio.
### Setting up the build system
- [Reference this page](https://github.com/bitcraze/crazyflie-firmware/blob/master/docs/building-and-flashing/build.md). The page "Getting Started With Development - Programming the CrazyFlie" has the wrong command. Your git pull command should include the --recursive option so it can also pull the dependencies for compiling to bare metal targets.
- DO NOT FLASH MULTIPLE DRONES AT THE SAME TIME, the results are unpredictable. Keep in mind that the crazyradio PA often can reach across into the next room over.

# When Finished

- Please unplug your CrazyFlies when you are done using them, and return them to the right-most cabinet.

# Cautions

- The drones are really finicky sometimes. Sometimes not flying after hitting the ground, requiring you to reset them by toggling a tiny switch on the top of the board near the front right arm.
- Pay attention to the LEDs!!! They each have different meanings and will tell you that something's wrong. See their meanings [here](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/#leds) But just for quick reference: 
    - Solid red LED (M1 by default): Low battery
    - 5 red LED blinks followed by brief pause repeating: Failed self-test.
    - Red blinking twice each second: Good to go!
    - Led 4 blinking red/green: Radio connected.
    - For anything else check the link above.
- We've had 2 cases now of a minor crash resulting in a broken leg. Be careful.
- In my (Parker) opinion, the crazyflie client sucks. It crashes quite frequently and most of the default controller input layouts have certain flight parameters set which shouldn't be set... like a mapping which automatically has pitch at -30 degrees or one which has thrust at 40% for no reason, forcing you to need to go into the settings to set those controls.
- It seems like the PS3 Mode 1 is one of the most reasonable control schemes.
More resources: https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/#controlling-the-crazyflie
