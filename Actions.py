from wallaby import *
import Constants as c
import Motors as m

def init():
    print "Hello there I am Waiting for you to push the button"
    # add tophat"
    wait_for_button()
    enable_servos()
    set_servo_position(c.armservo, 350)

def grabcan():
    set_servo_position(c.clawservo, 1775)
    msleep(1000)
    m.drive(10,50,400)
    set_servo_position(c.clawservo, 800)
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


def lineFollowToCan():
    m.drive(100, 100, 100)
    #follow line until It  gets close to the can
    dist = analog(c.etPort)
    while(dist<2600):
        dist=analog(c.etPort)
        print analog(c.thport)
        m.linefollow()
    ao()
