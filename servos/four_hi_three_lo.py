"""Example that iterates through a servo on every channel, sets each to 180 and then back to 0."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)


def serial_scan_rotate(): 
	for i in range(len(kit.servo)):
		kit.servo[i].angle = 180
		time.sleep(1)
		kit.servo[i].angle = 0
		time.sleep(1)


def syncro_all_rotate():
	for i in range(len(kit.servo)):
		kit.servo[i].angle = 180
		time.sleep(1)
	for i in range(len(kit.servo)):
		kit.servo[i].angle = 0
		time.sleep(1)

serial_scan_rotate()
# syncro_all_rotate()

