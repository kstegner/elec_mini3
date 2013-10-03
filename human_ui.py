import msvcrt
import hellousb
import time
from time import sleep

hello = hellousb.hellousb()

KEY_W = chr(119) #define the keys to be used in the interface program
KEY_A = chr(97)
KEY_S = chr(115)
KEY_D = chr(100)
KEY_P = chr(112)

TILT_VAL = 0 #set initial values of PAN and TILT
PAN_VAL =0
DUTY = 0
SCAN = 0


INC_VAL = 2.2**9 #set the value to increment servo position by

MAX = 2**16 - 1 #put limits on servo motion
MIN = 0

while True: #set up interface to run continuously
	if msvcrt.kbhit():
		key = msvcrt.getch()

		if key == KEY_W:
			TILT_VAL += INC_VAL
		elif key == KEY_S:
			TILT_VAL -= INC_VAL
		elif key == KEY_D:
			PAN_VAL -= INC_VAL
		elif key == KEY_A:
			PAN_VAL += INC_VAL
		elif key == KEY_P:
			SCAN = not SCAN
			print SCAN

	if PAN_VAL > MAX:
		PAN_VAL = MAX
	if PAN_VAL < MIN:
		PAN_VAL = MIN
	if TILT_VAL > MAX:
		TILT_VAL = MAX
	if TILT_VAL < MIN:
		TILT_VAL = MIN
		

	hello.set_vals(SCAN, DUTY)