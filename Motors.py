from wallaby import *
import Constants as c

def drive(leftspeed, rightspeed, time):
    motor(c.lm, leftspeed)
    motor(c.rm, rightspeed)
    msleep(time)
    ao()