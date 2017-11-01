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

std_deviation =  0.5
def gaussian_turbulation(orientation):
	return np.random.normal(orientation, std_deviation)

class FlightSimulator:
	def __init__(self, start_orientation, step_correction, perfect_orientation, generate_turbulation = gaussian_turbulation):
		self.current_orientation = start_orientation
		self.step_correction =step_correction
		self.perfect_orientation = perfect_orientation
		self.turbulation_generator = generate_turbulation
	
	def correct_tilt(self):
		self.current_orientation = self.current_orientation % 360 
		if self.current_orientation < self.perfect_orientation:
			self.current_orientation = self.current_orientation + self.step_correction
		elif self.current_orientation > self.perfect_orientation:
			self.current_orientation = self.current_orientation - self.step_correction
		
	def generate_turbulation(self):
		self.current_orientation =  self.turbulation_generator(self.current_orientation) 
	
	def print_current_orientation(self,  unit = 'degrees'):
		print('Current Orientation: ' + '{:.4f}'.format(self.current_orientation) + " " + unit)
		
		
if __name__ == "__main__":

	flight_sim = FlightSimulator( 20.0 ,0.1, 90.0)
	
	while True:
		print('''Choose option:
		[1] - Start flight simulation. (Hit Ctrl+C to return)
		[2] - Show flight current orientation
		[3] - Change flight correction parameters.
		[4] - Exit ''' )
		option = raw_input().lower();
		
		if(option == '1'):
			print('Simulation ON')
			try:
				while True:
					flight_sim.generate_turbulation() 
					flight_sim.correct_tilt()
					flight_sim.print_current_orientation()
					time.sleep(0.3)
			except KeyboardInterrupt:
				pass
			print('\nSimulation OFF\n')
		elif(option== '2'):
			flight_sim.print_current_orientation()			
		elif(option== '3'):
			try:
				flight_sim.step_correction = float(raw_input("Enter step correction value: "))
				flight_sim.perfect_orientation = float(raw_input('Enter desired orientation: '))
			except Exception:
				pass
			print('Parameters changed sucesssfuly!\n')
		elif(option == '4'):
			break

## Darnise



'''
dfadfda
fad
fda
sf
adf
af
'''











