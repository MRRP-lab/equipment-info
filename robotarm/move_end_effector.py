#!/usr/bin/python3

import sys
import time
import numpy as np
from scipy.spatial.transform import Rotation as R
from interpreter.interpreter import InterpreterHelper

ip = "192.168.56.101"

def init():
    import socket
    # Robot IP and Port
    HOST = ip # Replace with your robot's IP
    PORT = 30002
    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("Connected")
    # Send interpreter_mode() command
    # Ensure to include \n to signify the end of the command
    command = "interpreter_mode()\n"
    s.send(command.encode('utf-8'))
    data = s.recv(1024)
    s.close()
    print("Received",repr(data))


def generate_rotation_matrix_zyx(rx, ry, rz):
    # Create a Rotation object from Euler angles with 'ZYX' convention
    # The input to from_euler should be in the order of the axes string.
    r = R.from_euler('ZYX', [rz, ry, rx], degrees=False)
    
    # Convert to a 3x3 rotation matrix
    rotation_matrix = r.as_matrix()
    
    return rotation_matrix

def genPose(x,y,z,rx,ry,rz):
    pose = [x,y,z,rx,ry,rz]
    return pose

def moveToPose(pose):
    print("moving...")
    interpreter.execute_command("movej("+str(pose)+",a=1,v=1.05,t=0,r=0)")
    time.sleep(1.0)

if __name__ == "__main__":

    
    diff = 0.01

    #print("Init...")
    #init()

    print("Connecting....")
    interpreter = InterpreterHelper(ip)
    interpreter.connect()
    print("Connected!")
    time.sleep(1.)
    
    for i in range(3):
        pose = genPose(x=-0.3+diff*i,y=-.12,z=-0.25,rx=1.8,ry=2.5,rz=0.)
        moveToPose(pose)

    interpreter.end_interpreter()

