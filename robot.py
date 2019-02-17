from rrb3 import *
import time, random

BATTERY_VOLTS = 9
MOTOR_VOLTS = 6

rr = RRB3(BATTERY_VOLTS, MOTOR_VOLTS)

running = False

def turn_randomly():
    turn_time = random.randint(1, 3)
    if random.randint(1, 2) == 1:
        rr.left(turn_time, 0.5) # turn at half speed
    else:
        rr.right(turn_time, 0.5)
    rr.stop()

try:
    while True:
        distance = rr.get_distance()

        if distance < 50 and running :
        	print "Turning"
        	
        	turn_randomly()
        elif rr.sw1_closed():
        	print "Enabling Robot"

            running = not running

        else :
        	print "Going forward"
        	rr.forward(2)

    time.sleep(1)

finally:
	print "bye bye"
	rr.cleanup()
