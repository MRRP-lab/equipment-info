#!/usr/bin/python3

import sys
import time
import numpy as np
from scipy.spatial.transform import Rotation as R
from interpreter.interpreter import InterpreterHelper

ip = "192.168.101.55"

def generate_rotation_matrix_zyx(rx, ry, rz):
    # Create a Rotation object from Euler angles with 'ZYX' convention
    # The input to from_euler should be in the order of the axes string.
    r = R.from_euler('ZYX', [rz, ry, rx], degrees=False)
    
    # Convert to a 3x3 rotation matrix
    rotation_matrix = r.as_matrix()
    
    return rotation_matrix

def genPose(x,y,z,rx,ry,rz):
    mat = np.eye(4)
    mat[0, -1] = x
    mat[1, -1] = y
    mat[2, -1] = z
    rot_mat = generate_rotation_matrix_zyx(rx,ry,rz)
    mat[:3, :3] = rot_mat
    return mat

def moveToPose(pose):
    interpreter.execute_command("movej("+str(pose)+",a=1,v=1.05,t=0,r=0)")
    time.sleep(1.0)

if __name__ == "__main__":

    pose = genPose(x=-0.3,y=-.12,z=-0.25,rx=1.8,ry=2.5,rz=0.)
    
    diff = 0.01

    interpreter = InterpreterHelper(ip)
    interpreter.connect()
    
    for i in range(3):
        pose = genPose(x=-0.3+diff*i,y=-.12,z=-0.25,rx=1.8,ry=2.5,rz=0.)
        moveToPose(pose)

    interpreter.end_interpreter()

