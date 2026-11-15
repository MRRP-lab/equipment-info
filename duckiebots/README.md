
> [!WARNING]
> **Duckiebots are very finicky:** Some of these operations have been known corrupt the OS requiring a re-flash.

[Link to all the duckiebot documentation.](https://docs.duckietown.com/ente/duckietown-manual/welcome-to-the-duckietown-manual.html)

Before working with the Duckiebots, make sure that a DTS workspace has been properly installed. Attached is the [Duckietown installation](https://docs.duckietown.com/ente/duckietown-manual/10-setup/01-accounts/accounts-introduction.html) steps. Start with the account setup and the DTS installation.
# Turning Duckiebot On/Off
### On
To turn the Duckiebot on, press the battery button on the side of the Duckiebot **Once**. If properly flashed the upper display, and top power button should both turn on. This may take a few minutes. Once properly booted it should show up on `dts fleet discover`
### Off
There are three ways power off the Duckiebot:
- Press and hold the top power button for 6 seconds.
- run `dts duckiebot shutdown DUCKIEBOT_NAME`
- Via SSH (In progress)
# Connecting to Duckiebot

If you want your bot to work over a different wifi network than our "robo_wifi" in the lab, you can avoid re-flashing the SD card by manually editing the config on the Duckiebot. You will need to connect a monitor (HDMI) and keyboard (USB) to the Duckiebot itself while it is powered on, then follow these steps:

[https://docs.duckietown.com/ente/duckietown-manual/06-troubleshooting/duckiebot-network-faqs.html#duckiebot-setup-wifi](https://docs.duckietown.com/ente/duckietown-manual/06-troubleshooting/duckiebot-network-faqs.html#duckiebot-setup-wifi)


# Calibrating Duckiebot

Once you are on the same wifi network as the duckiebot, you can follow these instructions to test and calibrate hardware:

[https://docs.duckietown.com/ente/duckietown-manual/21-testing-debugging/02-components-testing/introduction-to-hardware-component-testing.html](https://docs.duckietown.com/ente/duckietown-manual/21-testing-debugging/02-components-testing/introduction-to-hardware-component-testing.html)

[https://docs.duckietown.com/ente/duckietown-manual/20-operations/04-calibrations/duckiebot-calibrations-intro.html](https://docs.duckietown.com/ente/duckietown-manual/20-operations/04-calibrations/duckiebot-calibrations-intro.html)


# Controlling Duckiebot

### Using ROS
If you have ROS installed on a laptop device, you can send and receive messages over WIFI. This includes remote-control driving and streaming camera images.

[Start here!](https://docs.duckietown.com/ente/duckietown-manual/04-software-tools/duckietown-duckiebot-additional-software-tools.html#ros)

### Using DTS Commands
In [this file](Duckietown%20Shell%20Commands.txt) there are some basic dts commands for viewing the camera and controlling the Duckiebot with the keyboard. 

- To run the Duckietown lane following demo ensure that the Duckietown roads meet the minimum specifications for a road [here.](https://docs.duckietown.com/ente/duckietown-manual/30-duckietown-city/appearance-specifications/duckietown-smart-city-tile-map.html)
- Run the following command with your Duckiebot name:

  ` dts duckiebot demo --demo_name lane_following --duckiebot_name ![DUCKIEBOT_NAME] --package_name duckietown_demos `
- Then launch the dts keyboard control command, in a new terminal, once the lights on the bot are green.

  ` dts duckiebot keyboard_control DUCKIEBOT_NAME `
- Turn on autopilot in the GUI window that appears, the Duckiebot should start to lane follow in the right lane.


# Flashing the Duckiebot
To flash a Duckiebot you can either use a shell commands with a dts installed or use their [GUI](https://docs.duckietown.com/daffy/opmanual-duckiebot/setup/setup_sd_card/gui.html) (The GUI seems to have more consistent results). To flash using a CLI, follow this [tutorial](https://docs.duckietown.com/daffy/opmanual-duckiebot/setup/setup_sd_card/cli.html). The Duckiebots in our lab are DB21J, make sure that all information is typed in correctly and the naming conventions are properly followed.

# Known issues
- Lane following is very poor when running the demo (Investigating camera and wheel calibration, as well as floor coloring).
- Current configuration of the Duckiebots think that it is 2023, will not allow updates (Investigating ntp)
- SSH default key is not quack, or quackquack. Need to investigate how to get this working, could be related to the above issue.

