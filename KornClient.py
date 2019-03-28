#!/usr/bin/python

import socket
import datetime
from Adafruit_LED_Backpack import SevenSegment
import RPi.GPIO as GPIO
import time
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.0.31', 5545)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

#IMPORTS PLAYER A2GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)

#IMPORTS PLAYER B
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.IN)

#RESET BUTTON
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.IN)

#DECLARE VARIABLES
countA = 0
countB = 0

 
# ===========================================================================
# CORN HOLE - CORN HOLE - CORN HOLE - CORN HOLE - CORN HOLE - CORN HOLE - CORN HOLE 
# ===========================================================================

segment = SevenSegment.SevenSegment(address=0x70)

print ('Press CTRL+Z to exit')

# Initialize the display.
segment.begin()

segment.clear()

#INPUT FOR PLAYER A AND B BUTTONS  

while(True):
  inputValue = GPIO.input(17)
  if(inputValue == True):
   countA = countA + 1
   time.sleep(.2)
   
  inputValue = GPIO.input(5)
  if(inputValue == True):
   countB = countB + 1
   time.sleep(.2)

  if (countA) == (22):
      countA = countA -6
 
  if (countB) == (22):
      countB = countB -6
 
  segment.clear()
 
 #RESET BUTTON  
  inputValue = GPIO.input(22)
  if(inputValue == True):
        countA = 0
        countB = 0
  a = "a "
  b = "b "
  sock.send (str(countA) + (a))
  time.sleep(.01)

  sock.send (str(countB) + (b))
  time.sleep(.01)
 
  segment.clear()
# Sets first two digits (Player A)
  segment.print_float((countA), decimal_digits=0, justify_right=False)

# Sets second two digits (Player B)
  segment.print_float((countB), decimal_digits=0, justify_right=True) 

# Colon
  segment.set_colon(True)

# Write the display buffer to the hardware.  This must be called to
# update the actual display LEDs.
  segment.write_display()