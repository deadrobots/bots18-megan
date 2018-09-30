#!/usr/bin/python
import os, sys
from wallaby import *
def drive(leftspeed, rightspeed, time):
    motor(1, leftspeed)
    motor(0, rightspeed)
    msleep(time)
    ao()

def main():
    print "Hi there im Waiting for you to push the button"
    # we are going to see if picking up the can still works after rebuilding robot"
    wait_for_button()
    enable_servos()
    set_servo_position(1,1775)
    msleep (1000)
    set_servo_position(0,390)
    msleep (1000)
    wait_for_button()
    motor(0,100)
    motor(1,100)
    etPort=0
    dist=0
    while(dist<2600):
        dist=analog(etPort)
        print dist
    ao()
    wait_for_button()
    set_servo_position(1, 750)
    msleep (1000)
    set_servo_position(0,890)
    msleep (1000)
    for x in range(0, 4):
        drive(100, 100, 1000)
        drive(100, 0, 980)
    set_servo_position(1, 2047)
    msleep(1000)

    # Stop
    motor(1, 0)
    motor(0, 0)
    msleep(1000)

def wait_for_button():
    print "press left button"
    while not left_button():
        pass





if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();