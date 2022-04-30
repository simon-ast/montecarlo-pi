import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["ytick.minor.visible"] = True
mpl.rcParams["xtick.top"] = mpl.rcParams["ytick.right"] = True
mpl.rcParams["xtick.direction"] = mpl.rcParams["ytick.direction"] = "in"


def plot(ax, x, y, color, marker, label):
	ax.plot(x, y, color=color, lw=2, label=label, marker=marker)


def main():
	# LOAD TOTAL DATA
	data = np.loadtxt("TimeComparison.dat", skiprows=1)
	
	# SPLIT INTO APPROPRIATE ARRAYS
	numit = data[:, 0]
	time_py = data[:, 1]
	time_pypool = data[:, 2]
	time_cpp = data[:, 3]
	time_c = data[:, 4]
	
	# PLOT THE DATA
	fig, ax = plt.subplots()
	
	plot(ax, numit, time_py, "tab:red", "o", "Python (serial)")
	plot(ax, numit, time_pypool, "tab:blue", "d", "Python (Pool4)")
	plot(ax, numit, time_cpp, "tab:green", "^", "C++")
	plot(ax, numit, time_c, "black", "s", "C")
	
	ax.set(
		xscale="log", yscale="log",
		xlabel="# Iterations",
		ylabel="Execution time [s]",
	)

	plt.grid(True, alpha=0.8)
	plt.legend()
	
	plt.savefig("ExecComp.png")
	plt.savefig("ExecComp.svg")
	plt.show()


if __name__ == "__main__":
	main()
