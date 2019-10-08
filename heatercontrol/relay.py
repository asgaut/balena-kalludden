import os

# Assume we are running on RPi if BALENA exists
if "BALENA" in os.environ:
	import RPi.GPIO as GPIO
else:
	import simgpio as GPIO # enables testing without relay hardware

_relay = 17 # BCM GPIO number
_initialized = False

def _init():
	global _initialized
	if _initialized == False:
		# Set GPIO mode: GPIO.BCM or GPIO.BOARD
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(_relay, GPIO.OUT)
		_initialized = True

# Closes (activates) the relay
def close():
	_init()
	GPIO.output(_relay, 1)

# Opens the relay
def open():
	_init()
	GPIO.output(_relay, 0)
