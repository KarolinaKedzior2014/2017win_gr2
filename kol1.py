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



import sys
import numpy as np
import time

import threading


std_deviation =  0.1
def gaussian_turbulation(orientation):
	return np.random.normal(orientation, std_deviation)

class AutoCorrector:
	def __init__(self, desired_value, step_correction, minimal_value, maximum_value):
		self.desired_value = desired_value
		self.step_correction = step_correction
		self.value_min = minimal_value
		self.value_max = maximum_value
	def change_desired_value(self, new_value, isDegree = True):
		if not isDegree:
			self.desired_value = new_value * 180.0/Math.PI
		else:
			self.desired_value = new_value
	def correct_value(self, value_in):
		value_in = value_in % 360 
		correct_value = value_in
		if value_in < self.desired_value:
			corrected_value = value_in + self.step_correction
		elif value_in > self.desired_value:
			corrected_value = value_in - self.step_correction
		return correct_value
				
class FlightSimulator(threading.Thread):
	def __init__(self, start_orientation = 90.0, orientation_corrector = None, generate_turbulation_fun = gaussian_turbulation, ):

		super(FlightSimulator, self).__init__()
		
		self.current_orientation = start_orientation
		self.orientation_corrector = orientation_corrector
		self.turbulation_generator = generate_turbulation_fun
		self._stop_event = True
	def generate_turbulation(self):
		self.current_orientation =  self.turbulation_generator(self.current_orientation) 
	def apply_correction(self):
		if self.orientation_corrector:
			self.current_orientation = self.orientation_corrector.correct_value(self.current_orientation)
	def print_current_orientation(self,  unit = 'degrees'):
		print('Current Orientation: ' + '{:.4f}'.format(self.current_orientation) + " " + unit)
	def run(self):
		self._stop_event = True
		while True:
			if self._stop_event:
				flight_sim.generate_turbulation() 
				flight_sim.apply_correction()
				time.sleep(0.3)
			else:
				break
			
	def stop(self):
		self._stop_event = False
		
			
if __name__ == "__main__":

	flight_sim = FlightSimulator( start_orientation =20.0 , orientation_corrector = AutoCorrector(90.0,0.2, 0.0, 360.0) )
	
	while True:
		print('''Choose option:
		[1] - Start flight simulation.
		[2] - Close program ''' )
		option = raw_input().lower();
		
		if(option == '1'):
			print('Simulation ON')
			flight_sim.start()
			while True:
				print('''Choose option:
[1] - Show flight current orientation (Ctr+C to return)
[2] - Stop simulation ''' )
				option = raw_input().lower();
				if(option== '1'):
					try:
						while True:
							flight_sim.print_current_orientation()	
							time.sleep(0.3)
					except KeyboardInterrupt:
						pass
				elif(option== '2'):
					flight_sim.stop()
					print('\nSimulation OFF\n')
					break
		elif(option == '2'):
			break











