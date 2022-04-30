from numpy.random import default_rng
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["xtick.top"] = mpl.rcParams["ytick.right"] = True
mpl.rcParams["xtick.direction"] = mpl.rcParams["ytick.direction"] = "in"


def generate_sample(sample_size: int):
	"""
	Generates a set of random point coordinates within (-1, 1), as well
	as a monte carlo estimation of PI.
	
	:param sample_size: INT,
		Number of points to be generated.
	:return: TUPLE,
		Returns both "circle" and "remainder" coordinate pairs, as well
		as PI estimate.
	"""
	circle_points_x = []
	circle_points_y = []
	remainder_x = []
	remainder_y = []
	
	rng = default_rng()
	
	coord_one = rng.uniform(-1.0, 1.0, size=sample_size)
	coord_two = rng.uniform(-1.0, 1.0, size=sample_size)
	origin_dist2 = coord_one ** 2 + coord_two ** 2
	
	for i in range(len(origin_dist2)):
		if origin_dist2[i] <= 1:
			circle_points_x.append(coord_one[i])
			circle_points_y.append(coord_two[i])
		else:
			remainder_x.append(coord_one[i])
			remainder_y.append(coord_two[i])
	
	pi_estimate = 4 * len(circle_points_x) / sample_size
	
	return (circle_points_x, circle_points_y, remainder_x, remainder_y,
	        pi_estimate)


def main(sample_size: int):
	"""
	Main call. Takes sample size and returns a plot to illustrate the
	idea behind the MC PI estimation.
	
	:param sample_size: INT,
		Total point number.
	:return: NONE
	"""
	fig, ax = plt.subplots(figsize=(7, 7))
	
	rectangle = plt.Rectangle((-1, -1), 2, 2, fill=False, ec="tab:blue",
	                          lw=2.5, ls="--", alpha=0.5)
	circle = plt.Circle((0, 0), 1, fill=False, ec="red", lw=2.5, ls="--",
	                    alpha=0.5)
	plt.gca().add_patch(rectangle)
	plt.gca().add_patch(circle)
	
	xc, yc, xr, yr, mc_pi = generate_sample(sample_size)
	ax.scatter(xc, yc, c="tab:red", s=10)
	ax.scatter(xr, yr, c="tab:blue", s=10)
	
	plt.title(f"Using {sample_size} points \n"
	          f"$\\pi \\approx {mc_pi:1.5f}$")
	plt.savefig("MonteCarlo_PI_concept.png")
	plt.savefig("MonteCarlo_PI_concept.svg")
	
	plt.show()


if __name__ == "__main__":
	main(5000)
