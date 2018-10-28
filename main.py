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

# Great work so far, Megan!
# Next up, let's put your constants and motor functions in different files. Try using the following structure:
# constants.py (holds your constants!)
# actions.py  (contains collections of motor and servo commands to perform an action. EX: grabCan() )
# servo.py (just holds servo related functions. Not motor commands, generally)
# motors.py (just holds your motor commands. drive(), driveTimed(), driveUntilBlackLine(), stuff like that.)
# main.py (where everything starts!)
# I think I'm looking at old code, because I remember working with you on your line follow/can detection
# Don't forget to commit (AND PUSH!) your code before you leave the cave. I'll try to do a better job of 
# reminding people before they leave. Next time I'll have more specific comments for you 
# -LMB

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

def main():
    print "Hi there I am Waiting for you to push the button"
    # add tophat"
    wait_for_button()
    enable_servos()

    drive(100, 100, 100)

    while(dist<2600):
        dist=analog(etPort)
        print dist
    ao()
    # thport
    if analog(thport)>1500: #on  black
        drive(100, 50, 10)

    else: #on white
        drive(50, 100, 10)
    wait_for_button()

    for x in range(0, 4):
        drive(100, 100, 1000)
        drive(100, 0, 980)
    set_servo_position(clawservo, 2047) #opens up claw all the way to grab can
    msleep(1000)

    # Stop
    ao()
    msleep(1000)

def wait_for_button():
    print "press left button"
    while not left_button():
        pass





if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();
