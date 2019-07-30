#!/usr/bin/python3
"""
Readjust this Docstring as follows:
Names: Songezo Kenene
Student Number: KNNSON002
Prac: 01
Date: 26/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
import itertools

# global variables
count = 0

# set up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
leds = (11,13,15)
GPIO.setup(leds, GPIO.OUT)
inputs = (16,18)
GPIO.setup(inputs, GPIO.IN, pull_up_down=GPIO.PUD_UP)
patterns = {0:(0,0,0),1:(0,0,1),2:(0,1,0),3:(0,1,1),4:(1,0,0),5:(1,0,1),6:(1,1,0),7:(1,1,1)}

# callback functions
def count_up(channel):
        global count
	print('Count up')
	if count >= 7:
		count = 0
	else:
		count = count + 1
	for i in range(0,3):
        	GPIO.output(leds[i], patterns[count][i])
        time.sleep(0.2)












def count_down(channel):
	global count
	if count <= 0:
		count = 7
	else:
		count = count - 1
	print('Count down')
	for i in range(0,3):
        	GPIO.output(leds[i], patterns[count][i])
        time.sleep(0.1)

# interrupts
GPIO.add_event_detect(16, GPIO.FALLING, callback=count_up, bouncetime=400)
GPIO.add_event_detect(18, GPIO.FALLING, callback=count_down, bouncetime=400)


# Logic that you write
def main():
    print('on')
    time.sleep(0.2)

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
    GPIO.cleanup()
