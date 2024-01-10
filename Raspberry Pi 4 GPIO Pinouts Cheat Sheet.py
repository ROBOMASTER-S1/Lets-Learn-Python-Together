'''
Raspberry Pi 4 GPIO Pinouts Cheat Sheet for both Board
and BCM/Broadcom settings for GPIO set modes:

This is also a cheat sheet for the 74HC595 shift register
set up and activation process

Created by Joseph C. Richardson, GitHub.com

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

You can also use the Broadcom SOC
Channel method if you prefer.

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

Please read onward to learn more.
'''
# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# These are all the GPIO pins that you can use for lighting
# up LEDs or whatever devices that can 'safely' use these
# GPIO pins. I created these Cheat Sheets examples for
# quick references and understanding of the GPIO pin layout. 
# (GPIO) General Purpose Input/Output Pinouts:

# (GPIO) General Purpose Input/Output Pinouts:

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

# How to set up 74HC595 shift registers:

# Create variables for the RCLK, data bit and the SRCLK.

# You can rename all these variables to any names you wish,
# but keep in mind that you must also rename any variables
# in your program as well. Click the Find and Replace command
# on the IDLE menu to make any renaming changes faster to cover
# any variables you want to rename. However, you should stick
# to meaningful names, so other programmers can learn and
# understand what's happening throughout the program's
# execution/run.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Note: Python executes its programs from the top, downward.
# You must place these variable values in this correct order as shown.
# These pinout values won't execute right if you don't.

RCLK = 13
SER = 15
SRCLK = 11
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
control_shift = RCLK,SER,SRCLK

for i in control_shift:GPIO.setup(i,GPIO.OUT) # setup desired GPIO pinouts

GPIO.setup(27,GPIO.OUT) # GPIO 0
GPIO.setup(28,GPIO.OUT) # GPIO 1
GPIO.setup(3,GPIO.OUT) # GPIO 2
GPIO.setup(5,GPIO.OUT) # GPIO 3
GPIO.setup(7,GPIO.OUT) # GPIO 4
GPIO.setup(29,GPIO.OUT) # GPIO 5
GPIO.setup(31,GPIO.OUT) # GPIO 6
GPIO.setup(26,GPIO.OUT) # GPIO 7
GPIO.setup(24,GPIO.OUT) # GPIO 8
GPIO.setup(21,GPIO.OUT) # GPIO 9
GPIO.setup(19,GPIO.OUT) # GPIO 10
GPIO.setup(32,GPIO.OUT) # GPIO 12
GPIO.setup(33,GPIO.OUT) # GPIO 13
GPIO.setup(36,GPIO.OUT) # GPIO 16
GPIO.setup(11,GPIO.OUT) # GPIO 17
GPIO.setup(12,GPIO.OUT) # GPIO 18
GPIO.setup(35,GPIO.OUT) # GPIO 19
GPIO.setup(38,GPIO.OUT) # GPIO 20
GPIO.setup(40,GPIO.OUT) # GPIO 21
GPIO.setup(15,GPIO.OUT) # GPIO 22
GPIO.setup(16,GPIO.OUT) # GPIO 23
GPIO.setup(18,GPIO.OUT) # GPIO 24
GPIO.setup(22,GPIO.OUT) # GPIO 25
GPIO.setup(37,GPIO.OUT) # GPIO 26
GPIO.setup(13,GPIO.OUT) # GPIO 27

# these three for loops are how you activate 74HC595 shift registers:

for i in range(8):            
    GPIO.output(RCLK,0)
    GPIO.output(SER,0) # 1 = ON/HIGH and 0 = LOWOFF
    GPIO.output(SRCLK,1)
    GPIO.output(RCLK,1)
    GPIO.output(SRCLK,0)

for i in range(16):            
    GPIO.output(RCLK,0)
    GPIO.output(SER,0) # 1 = ON/HIGH and 0 = LOWOFF
    GPIO.output(SRCLK,1)
    GPIO.output(RCLK,1)
    GPIO.output(SRCLK,0)

for i in range(24):            
    GPIO.output(RCLK,0)
    GPIO.output(SER,0) # 1 = ON/HIGH and 0 = LOWOFF
    GPIO.output(SRCLK,1)
    GPIO.output(RCLK,1)
    GPIO.output(SRCLK,0)

# By changing the for loop values to 8,16 and 24 allows you
# to add more 74HC595 shift registers, up to as many as you
# please. However, you must use the right for loop value settings.
# for example, if you had five 74HC595 shift registers, you would
# create this for loop value (40) instead. Five 74HC595 shift registers
# give you forty extra GPIO pinouts for your Raspberry Pi

for i in range(40):            
    GPIO.output(RCLK,0)
    GPIO.output(SER,0) # 1 = ON/HIGH and 0 = LOWOFF
    GPIO.output(SRCLK,1)
    GPIO.output(RCLK,1)
    GPIO.output(SRCLK,0)
    
GPIO.cleanup() # GPI.cleanup() sets all GPIO pins to LOW/OFF state
'''
Use these GPIO commands to turn
GPIO pins ON or OFF

Example 1:
    
GPIO.output(7,GPIO.HIGH) # On
GPIO.output(7,GPIO.LOW) # Off

Example 2:
    
GPIO.output(7,1) # On
GPIO.output(7,0) # Off

Example 3:
    
GPIO.output(7,True) # On
GPIO.output(7,False) # Off

Note: make sure to turn off all GPIO pins
first before stopping any programs.

GPIO.cleanup() # Release all GPIO pins
'''

# (GPIO) General Purpose Input/Output Pinouts:

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # broadcom method
GPIO.setwarnings(False) # disable setwarnings

# How to set up 74HC595 shift registers:

# Create variables for the RCLK, data bit and the SRCLK.

# You can rename all these variables to any names you wish,
# but keep in mind that you must also rename any variables
# in your program as well. Click the Find and Replace command
# on the IDLE menu to make any renaming changes faster to cover
# any variables you want to rename. However, you should stick
# to meaningful names, so other programmers can learn and
# understand what's happening throughout the program's
# execution/run.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Note: Python executes its programs from the top, downward.
# You must place these variable values in this correct order as shown.
# These pinout values won't execute right if you don't.

RCLK = 27
SER = 22
SRCLK = 17
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
control_shift = RCLK,SER,SRCLK

for i in control_shift:GPIO.setup(i,GPIO.OUT) # setup desired GPIO pinouts

GPIO.setup(0,GPIO.OUT) # PIN 27
GPIO.setup(1,GPIO.OUT) # PIN 28
GPIO.setup(2,GPIO.OUT) # PIN 3
GPIO.setup(3,GPIO.OUT) # PIN 5
GPIO.setup(4,GPIO.OUT) # PIN 7
GPIO.setup(5,GPIO.OUT) # PIN 29
GPIO.setup(6,GPIO.OUT) # PIN 31
GPIO.setup(7,GPIO.OUT) # PIN 26
GPIO.setup(8,GPIO.OUT) # PIN 24
GPIO.setup(9,GPIO.OUT) # PIN 21
GPIO.setup(10,GPIO.OUT) # PIN 19
GPIO.setup(12,GPIO.OUT) # PIN 32
GPIO.setup(13,GPIO.OUT) # PIN 33
GPIO.setup(16,GPIO.OUT) # PIN 36
GPIO.setup(17,GPIO.OUT) # PIN 11
GPIO.setup(18,GPIO.OUT) # PIN 12
GPIO.setup(19,GPIO.OUT) # PIN 35
GPIO.setup(20,GPIO.OUT) # PIN 38
GPIO.setup(21,GPIO.OUT) # PIN 40
GPIO.setup(22,GPIO.OUT) # PIN 15
GPIO.setup(23,GPIO.OUT) # PIN 16
GPIO.setup(24,GPIO.OUT) # PIN 18
GPIO.setup(25,GPIO.OUT) # PIN 22
GPIO.setup(26,GPIO.OUT) # PIN 37
GPIO.setup(27,GPIO.OUT) # PIN 13

# these three for loops are how you activate 74HC595 shift registers:

for i in range(8):            
    GPIO.output(RCLK,0)
    GPIO.output(SER,0) # 1 = ON/HIGH and 0 = LOWOFF
    GPIO.output(SRCLK,1)
    GPIO.output(RCLK,1)
    GPIO.output(SRCLK,0)

for i in range(16):            
    GPIO.output(RCLK,0)
    GPIO.output(SER,0) # 1 = ON/HIGH and 0 = LOWOFF
    GPIO.output(SRCLK,1)
    GPIO.output(RCLK,1)
    GPIO.output(SRCLK,0)

for i in range(24):            
    GPIO.output(RCLK,0)
    GPIO.output(SER,0) # 1 = ON/HIGH and 0 = LOWOFF
    GPIO.output(SRCLK,1)
    GPIO.output(RCLK,1)
    GPIO.output(SRCLK,0)

# By changing the for loop values to 8,16 and 24 allows you
# to add more 74HC595 shift registers, up to as many as you
# please. However, you must use the right for loop value settings.
# for example, if you had five 74HC595 shift registers, you would
# create this for loop value (40) instead. Five 74HC595 shift registers
# give you forty extra GPIO pinouts for your Raspberry Pi

for i in range(40):            
    GPIO.output(RCLK,0)
    GPIO.output(SER,0) # 1 = ON/HIGH and 0 = LOWOFF
    GPIO.output(SRCLK,1)
    GPIO.output(RCLK,1)
    GPIO.output(SRCLK,0)
    
GPIO.cleanup() # GPI.cleanup() sets all GPIO pins to LOW/OFF state

# Always use a KeyboardInterrupt, try and except error handler to force
# all GPIO pinouts to shut down to LOW/OFF state.

# Note: it is recomended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

try:
    for i in range(8):
        GPIO.output(RCLK,0)
        GPIO.output(SER,1) # 1 = ON/HIGH and 0 = LOWOFF
        GPIO.output(SRCLK,1)
        GPIO.output(RCLK,1)
        GPIO.output(SRCLK,0)

except KeyboardInterrupt:
    print('All GPIO pins are set to LOW/OFF') # GPIO notification message
    GPIO.cleanup() # GPIO.cleanup() sets all GPIO pins to LOW/OFF
    break
'''
Use these GPIO commands to turn GPI pins ON or OFF

Example 1:
    
GPIO.output(4,GPIO.HIGH) # On
GPIO.output(4,GPIO.LOW) # Off

Example 2:
    
GPIO.output(4,1) # On
GPIO.output(4,0) # Off

Example 3:
GPIO.output(4,True) # On
GPIO.output(4,False) # Off

Note: make sure to turn off all GPIO pins
first before stopping any programs.

GPIO.cleanup() # Release all GPIO pins

You can also use the Broadcom SOC
Channel method if you prefer.

GitHub username: Robomaster-S1
https://github.com/ROBOMASTER-S1

You can visit my GitHubGist page for
quicker access to these Python files
and Python programs:

https://github.com/ROBOMASTER-S1

The Python Tutorial is a great reference
tool to get you started.

https://www.w3schools.com/default.asp

w3schools.com
'''
