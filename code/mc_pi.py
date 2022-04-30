import time
import sys
import numpy as np
from numpy.random import default_rng


def pi_iteration(circle_points: int):
	rng = default_rng()

	x = rng.uniform(-1.0, 1.0)
	y = rng.uniform(-1.0, 1.0)
	
	if x ** 2 + y ** 2 <= 1:
		circle_points += 1
	
	return circle_points


def pi_estimate(desired_iterations):
	"""
	Simple method of estimating PI by comparing randomly sampled point
	inside the area of a circle and a square (of diameter/length 1).
	
	:param desired_iterations: INT,
		Number of desired iterations to estimate PI
	:return: FLOAT,
		Estimate of PI
	"""
	# INITIALIZING NECESSARY PARAMETERS
	# It is notable that ALL points will be within the square, so we can
	# initially set the number of iterations as the variable
	# part_of_square
	increment = 0
	part_of_circle = 0
	part_of_square = desired_iterations
	
	while increment < desired_iterations:
		part_of_circle = pi_iteration(part_of_circle)
		increment += 1
	
	return 4 * part_of_circle / part_of_square


def main():
	if len(sys.argv) > 1: 
		iterations = float(sys.argv[1])
		print_flag = int(sys.argv[2])
	else: 
		iterations = 1e5
		print_flag = 0
	
	start = time.time()
	mc_pi = pi_estimate(iterations)
	end = time.time()
	
	if print_flag == 1:
		print(f"\nAfter {iterations:.0e} iterations\n"
		      f"\nEstimation of PI:\t PI = {mc_pi}"
		      f"\nCompare to NumPy:\t PI = {np.pi}"
		      f"\nFirst 10 digits:\t PI = 3.141592653 ...\n"
		      f"\nExecution time was {end-start:1.5e}s.\n")
	elif print_flag == 2:
		print(f"{end-start:1.5e}")


if __name__ == "__main__":
	main()
