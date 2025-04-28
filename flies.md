Getting Started with CrazyFlies
-------------------------------
We have tons of working CrazyFlie drones
# Building a CrazyFlie
- We still have some CrazyFlie kits that haven't been assembled yet. See assembly instructions [here](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/#assembling)
- Some pieces are fragile. Be very careful.

# Controlling a CrazyFlie
### Mobile
- You can download a mobile app called the CrazyFlie client to control a single drone using low energy Bluetooth, available on both iPhone and Android. Also see official instructions [here](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/#controlling-the-crazyflie)
### PC
- To control a drone from a PC environment, you must have a few things:
  1. The CrazyFlie client set up and ready to go. You need root access to use the client because it needs to be able to scan the USB ports.
  2. Some kind of controller (We have 3 white Xbox controllers.)
  3. A way to communicate with the drone wirelessly. Our equipment comes with Crazyradio 2.0 adapters you can plug into a USB port.

Some things to watch out for here during setup.
- You'll need root access to the computer to scan the USB ports.
- Some students have tried using the client on a virtual machine, and they needed access to the vboxusers group. The command to do this is `sudo usermod -a -G vboxusers (user)`.
- After the client is setup, you might need to set the proper input mapping. Some of them are messed up and the drone will just immediately begin to fly up and away. Watch out for that. The input mapping that seems most normal is called Generic_OS_X (actually might be wrong, has a weird default pitch?), and can be found at Input Device>Device>Input Map.
- You'll notice that the client has some readings for things like link quality, battery, state estimation (thrust, x, y, and z,), and 
- Certain input mappings seem to have have a default control for yaw, pitch, or roll. So if you don't notice it and immediately give it thrust, it will veer off in some direction.
- This extra information just doesn't work sometimes. You can still fly the drone but without that extra information.
- To enable advanced flight: While not connected to a drone, see the menu on the left and change "Flight mode" to "Advanced."

- See more [here](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/#config-client).

# Controlling Many CrazyFlies
- This part is in-progress. There's no manual control of many at once without writing a program to do so. You need some special permissions to do so, because there's more risk involved with flying many at once.

# Programming a CrazyFlie
- Not finished.

# When Finished
- Please unplug your CrazyFlies when you are done using them!
- 
# Cautions
- The drones are really finicky sometimes. Sometimes not flying after hitting the ground, requiring you to reset them by toggling a tiny switch on the top of the board near the front right arm.
More resources: https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/#controlling-the-crazyflie
