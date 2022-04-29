import time
import sys
import numpy as np
from numpy.random import default_rng


def pi_estimate(desired_iterations):
	"""
	Simple method of estimating PI by comparing randomly sampled point
	inside the area of a circle and a square (of diameter/length 1).
	
	:param desired_iterations: INT,
		Number of desired iterations to estimate PI
	:return: FLOAT,
		Estimate of PI
	"""
	rng = default_rng()
	
	increment = 0
	part_of_circle = 0
	part_of_square = 0
	while increment < desired_iterations:
		x = rng.uniform(-1.0, 1.0)
		y = rng.uniform(-1.0, 1.0)

		if x**2 + y**2 <= 1:
			part_of_circle += 1
	
		part_of_square += 1
		increment += 1
	
	return 4 * part_of_circle / part_of_square


def main():
	
	if len(sys.argv) > 1:
		iterations = float(sys.argv[1])
	else:
		iterations = 1e5
	
	start = time.time()
	monte_carlo_pi = pi_estimate(iterations)
	end = time.time()
	
	print(f"\nAfter {iterations:.0e} iterations\n\n"
	      f"Estimation of PI: \tPI = {monte_carlo_pi}\n"
	      f"Compare to NumPy: \tPI = {np.pi}\n\n"
	      f"Execution time was {end-start:f}s.\n")


if __name__ == "__main__":
	main()
