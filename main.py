#!/usr/bin/python
import os, sys
from wallaby import *
import Constants as c
import Motors as m
import Actions as a
dist = 0


def main():
    a.init()
    a.lineFollowToCan()
    a.wait_for_button()
    a.grabcan()


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
