from wallaby import *
import Constants as c

def grabcan():
    set_servo_position(c.clawservo, 1775)
    msleep(1000)
    set_servo_position(c.armservo, 390)
    msleep(1000)
    wait_for_button()

def dropcan():
    set_servo_position(c.clawservo, 750)
    msleep(1000)
    set_servo_position(c.armservo, 890)
    msleep(1000)

def wait_for_button():
    print "press left button"
    while not left_button():
        pass