###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#If you have spare time you can implement: Command Line Interface, generators, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck


#!/usr/bin/env python2.7
import random 
import math
import numpy as np
from time import time

current_orientation = 50.0 
perfect_tilt = 90.0


angles = range(0,360)

def StepCorrection(orientation, step_correction):
	orientation = orientation % 360 #just in case
	if orientation < perfect_tilt:
		orientation = orientation + step_correction
	elif orientation > perfect_tilt:
		orientation = orientation - step_correction
	return orientation

print('a')
	

while True:
	#start	
	#current_orientation = np.random.normal( to future
	current_orientation = current_orientation + random.uniform(0,1) - 0.5
	print('Current Orientation', current_orientation)
	current_orientation = StepCorrection(current_orientation, 0.6)
	print('Current Orientation after correction/n/n', current_orientation)

















