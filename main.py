#!/usr/bin/python
import os, sys
from wallaby import *
thport = 1
#lm= Left Motor
lm = 1
#rm= Right Motor
rm = 0
etPort = 0
dist = 0
armservo = 0
clawservo = 1

def drive(leftspeed, rightspeed, time):
    motor(lm, leftspeed)
    motor(rm, rightspeed)
    msleep(time)
    ao()

def grabcan():
    set_servo_position(clawservo, 1775)
    msleep(1000)
    set_servo_position(armservo, 390)
    msleep(1000)
    wait_for_button()

def dropcan():
    set_servo_position(clawservo, 750)
    msleep(1000)
    set_servo_position(armservo, 890)
    msleep(1000)

def wait_for_button():
    print "press left button"
    while not left_button():
        pass

def main():
    print "Hello there I am Waiting for you to push the button"
    # add tophat"
    wait_for_button()
    enable_servos()

    drive(100, 100, 100)
    #follow line until It  gets close to the can
    dist = analog(etPort)
    while(dist<2600):
        dist=analog(etPort)
        print analog(thport)
        if analog(thport) > 400:  # on  black
            drive(100, 5, 1)
        else:  # on white
            drive(5, 100, 1)
    ao()
    # thport

    wait_for_button()

    for x in range(0, 4):
        drive(100, 100, 1000)
        drive(100, 0, 980)
    set_servo_position(clawservo, 2047) #opens up claw all the way to grab can
    msleep(1000)

    # Stop
    ao()
    msleep(1000)







if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();
