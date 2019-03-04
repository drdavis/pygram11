# Script to make the comparison plot for the benchmark

import numpy as np
import matplotlib

matplotlib.use("pdf")
import matplotlib.pyplot as plt

(
    size,
    np_1d_min,
    np_1d_mean,
    np_1d_median,
    pg_1d_min,
    pg_1d_mean,
    pg_1d_median,
    np_2d_min,
    np_2d_mean,
    np_2d_median,
    pg_2d_min,
    pg_2d_mean,
    pg_2d_median,
) = np.loadtxt("benchmark_times_omp.txt", unpack=True)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(size, np_1d_min / pg_1d_min, label="1D np/pg11")
ax.plot(size, np_2d_min / pg_2d_min, label="2D np/pg11")
ax.set_title("pygram11 OpenMP enabled")
ax.legend(loc="upper left", ncol=3)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.3, 3e8)
ax.set_ylim(0.5, 100)
ax.grid()
ax.set_xlabel("Array size")
ax.set_ylabel("Time Ratios")

fig.savefig("compare_omp.png")