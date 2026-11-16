# -*- coding: utf-8 -*-
# Flies to each corner with a 0.5m buffer
import sys
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.utils import uri_helper
from cflib.utils.reset_estimator import reset_estimator

# URI to the Crazyflie to connect to
uri = uri_helper.uri_from_env(default='radio://0/17/2M/E7E7E7E7E7')

# Grid dimensions (in meters)
X_MAX = 2.0
Y_MAX = 3.0
Z_MAX = 2.0
BUFFER = 0.5

# Calculate buffered bounds
x_low, x_high = BUFFER, X_MAX - BUFFER  # 0.5m to 1.5m
y_low, y_high = BUFFER, Y_MAX - BUFFER  # 0.5m to 2.5m
z_low, z_high = BUFFER, Z_MAX - BUFFER  # 0.5m to 1.5m

# Ordered list of all 8 corners (bottom loop first, then top loop)
# Format: (x, y, z, yaw_radians, travel_duration_seconds)
CORNERS = [
    # Bottom layer (z = 0.5m)
    (x_low,  y_low,  z_low,  0.0, 3.0),  # Near (0, 0, 0)
    (x_high, y_low,  z_low,  0.0, 3.0),  # Near (2, 0, 0)
    (x_high, y_high, z_low,  0.0, 4.0),  # Near (2, 3, 0)
    (x_low,  y_high, z_low,  0.0, 3.0),  # Near (0, 3, 0)

    # Top layer (z = 1.5m)
    (x_low,  y_high, z_high, 0.0, 3.0),  # Near (0, 3, 2)
    (x_high, y_high, z_high, 0.0, 3.0),  # Near (2, 3, 2)
    (x_high, y_low,  z_high, 0.0, 4.0),  # Near (2, 0, 2)
    (x_low,  y_low,  z_high, 0.0, 3.0),  # Near (0, 0, 2)
]


def activate_mellinger_controller(cf):
    cf.param.set_value('stabilizer.controller', '2')


def run_corner_tour(cf):
    commander = cf.high_level_commander

    # Arm the Crazyflie
    print('Arming Crazyflie...')
    cf.supervisor.send_arming_request(True)
    time.sleep(1.0)

    # Take off to the buffered lower Z height (0.5m)
    print(f'Taking off to z={z_low}m...')
    commander.takeoff(z_low, 2.0)
    time.sleep(3.0)

    # Visit each buffered corner in absolute LPS coordinates
    for i, (x, y, z, yaw, duration) in enumerate(CORNERS, start=1):
        print(f'[{i}/{len(CORNERS)}] Flying to ({x:.2f}, {y:.2f}, {z:.2f})...')
        commander.go_to(x, y, z, yaw, duration, relative=False)
        # Wait for travel duration plus a 1-second hover at the corner
        time.sleep(duration + 1.0)

    # Land cleanly at the final corner's X/Y position
    print('Landing...')
    commander.land(0.0, 2.5)
    time.sleep(3.0)
    commander.stop()
    print('Flight complete!')


if __name__ == '__main__':
    cflib.crtp.init_drivers()

    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        cf = scf.cf

        # Uncomment if you prefer the Mellinger controller over the default PID
        # activate_mellinger_controller(cf)

        print('Resetting estimator...')
        reset_estimator(cf)
        run_corner_tour(cf)
