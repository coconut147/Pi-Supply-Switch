#!/usr/bin/env python

# Import the modules to send commands to the system and access GPIO pins
from subprocess import call
import RPi.GPIO as GPIO
from time import sleep

def Shutdown():

 print "Will shutdown right now !"
 GPIO.output(PinEight,0) # Bring down PinEight so that the capacitor can discharge an remove power to the Pi
 GPIO.cleanup() # Cleanup of GPIO usage
 call('poweroff', shell=False) # Initiate OS Poweroff
 return




# Map pin seven and eight on the Pi Switch PCB to chosen pins on the Raspberry Pi header
# The PCB numbering is a legacy with the original design of the board
PinSeven = 7
PinEight = 11

# Initialization of GPIOs
GPIO.setmode(GPIO.BOARD) # Set pin numbering to board numbering
GPIO.setup(PinSeven, GPIO.IN) # Set up PinSeven as an input
GPIO.setup(PinEight, GPIO.OUT, initial=1) # Setup PinEight as output

# Now we can wait for a button press
# To address an issue with spikes we'll only accept a press of the button if it lasts 100ms

while (GPIO.input(PinSeven) == False): # While button not pressed

	GPIO.wait_for_edge(PinSeven, GPIO.RISING) # Wait for a rising edge on PinSeven
	print "Detected a rising edge."
	sleep(0.1); # Sleep for 100ms


Shutdown()


