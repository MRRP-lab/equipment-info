# How to interpret the files in this folder:

- Each .yaml file is meant to be created and reused by the CFclient.
- The name of the file represents the LxWxH of the cube created by orienting the node towers in the corresponding locations.
- All measurements are in meters.

## How to use the files:
1. Must have a Crazyflie with the Loco Positioning Deck installed
2. Towers must be placed in the following orientation:  
    **5**---L---**7**  
    |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  
    W&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;W  
    |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|  
    **0**---L---**2**  
* Only bottom nodes are displayed. The height of each tower's top node must be set to match the file's H value. If H = 1.10, that is the lowest position. O.w. follow the markings on the tower's rods.
* Node 0 acts as the origin of the XYZ-plane. All other nodes are oriented in relation to node 0. 
3. Crazyflie and Nodes must be powered on. CFclient must be connected to the Crazyflie. Crazyflie should be placed on the floor in the center of the towers.
4. In Loco Position tab, select *Configure positions* 
5. Select *Load from file...*
6. Select desired .yaml file
7. Select *Write to anchors*
8. Done! The nodes now know where they are in relation to one another.

## Note on the node towers:
- When the tower is collapsed, the top nodes are at z=1.10m
- Extending the middle rod adds 0.95m
- Extending the inner rod adds 0.93m
- For simplicity's sake, configurations should be use 1 of 3 tower height configurations for easy reproducability:
  1. **Position #1:** Tower collaped, z=1.10
  2. **Position #2:** Only inner rod extended, z=2.03
  3. **Position #3:** Inner and middle rods extended, z=2.98
