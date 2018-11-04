from wallaby import *
import Constants as c

def drive(leftspeed, rightspeed, time):
    motor(c.lm, leftspeed)
    motor(c.rm, rightspeed)
    msleep(time)
    ao()


def linefollow():
    if analog(c.thport) > 400:  # on  black
        drive(100, 5, 1)
    else:  # on white
        drive(5, 100, 1)