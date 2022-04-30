import sys
import time
import typing as tp
import numpy as np
from numpy.random import default_rng
from multiprocessing import Pool


def distribute_tasks(num_processes: int,
                     num_tasks: float
                     ) -> tp.List:
	"""
	DOCST
	
	:param num_processes:
	:param num_tasks:
	:return:
	"""
	int_distr = num_tasks // num_processes
	remain = num_tasks % num_processes
	
	distributed_tasks = [int_distr] * (num_processes - 1)
	distributed_tasks.append(int_distr + remain)
	
	# SMALL SANITY CHECK
	assert num_tasks == np.array(distributed_tasks).sum(), \
		f"For some reason, {num_tasks} were submitted but only" \
		f"{np.array(distributed_tasks).sum(),} were divided!"
	
	return distributed_tasks


def pi_estimate(desired_iterations: int) -> tp.Tuple:
	"""
	Simple method of estimating PI by comparing randomly sampled point
	inside the area of a circle and a square (of diameter/length 1).

	:param desired_iterations: INT,
		Number of desired iterations to estimate PI
	:return: FLOAT,
		Estimate of PI
	"""
	increment = 0
	part_of_circle = 0
	part_of_square = 0
	
	rng = default_rng()
	
	while increment < desired_iterations:
		
		x = rng.uniform(-1.0, 1.0)
		y = rng.uniform(-1.0, 1.0)
		
		if x ** 2 + y ** 2 <= 1:
			part_of_circle += 1
		
		increment += 1
		part_of_square += 1
	
	return part_of_circle, part_of_square


def main(num_processes):
	if len(sys.argv) > 1:
		iterations = float(sys.argv[1])
		print_flag = int(sys.argv[2])
	else:
		iterations = 1e5
		print_flag = 0
	
	start = time.time()
	
	pool = Pool(processes=num_processes)
	multi_eval = np.array(
		pool.map(pi_estimate, distribute_tasks(num_processes, iterations))
	)
	pool.close()
	
	result = multi_eval.sum(axis=0)
	mc_pi = 4 * result[0] / result[1]
	
	end = time.time()
	
	if print_flag == 1:
		print(f"\nAfter {iterations:.0e} iterations\n"
		      f"\nEstimation of PI:\t PI = {mc_pi}"
		      f"\nCompare to NumPy:\t PI = {np.pi}"
		      f"\nFirst 10 digits:\t PI = 3.141592653 ...\n"
		      f"\nExecution time was {end - start:1.5e}s.\n")
	elif print_flag == 2:
		print(f"{end - start:1.5e}")


if __name__ == "__main__":
	main(4)
