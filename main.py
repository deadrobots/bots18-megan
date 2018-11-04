#!/usr/bin/python
import os, sys
from wallaby import *
import Constants as c
import Motors as m
import Actions as a
dist = 0


# Great work so far, Megan!
# actions.py  (contains collections of motor and servo commands to perform an action. EX: grabCan() )
# servo.py (just holds servo related functions. Not motor commands, generally)
# motors.py (just holds your motor commands. drive(), driveTimed(), driveUntilBlackLine(), stuff like that.)
# main.py (where everything starts!)
# I think I'm looking at old code, because I remember working with you on your line follow/can detection
# Don't forget to commit (AND PUSH!) your code before you leave the cave. I'll try to do a better job of 
# reminding people before they leave. Next time I'll have more specific comments for you 
# -LMB


def main():
    print "Hello there I am Waiting for you to push the button"
    # add tophat"
    a.wait_for_button()
    enable_servos()

    m.drive(100, 100, 100)
    #follow line until It  gets close to the can
    dist = analog(c.etPort)
    while(dist<2600):
        dist=analog(c.etPort)
        print analog(c.thport)
        if analog(c.thport) > 400:  # on  black
            m.drive(100, 5, 1)
        else:  # on white
            m.drive(5, 100, 1)
    ao()
    # thport

    a.wait_for_button()

    for x in range(0, 4):
        m.drive(100, 100, 1000)
        m.drive(100, 0, 980)
    set_servo_position(c.clawservo, 2047) #opens up claw all the way to grab can
    msleep(1000)

    # Stop
    ao()
    msleep(1000)







if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();
