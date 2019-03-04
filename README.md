# pygram11

[![builds.sr.ht status](https://builds.sr.ht/~ddavis/pygram11.svg)](https://builds.sr.ht/~ddavis/pygram11?)
[![Documentation Status](https://readthedocs.org/projects/pygram11/badge/?version=stable)](https://pygram11.readthedocs.io/en/stable/?badge=stable)
![](https://img.shields.io/pypi/pyversions/pygram11.svg?colorB=blue&style=flat)
[![PyPI version](https://img.shields.io/pypi/v/pygram11.svg?colorB=486b87&style=flat)](https://pypi.org/project/pygram11/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Simple and fast histogramming in python via
[pybind11](https://github.com/pybind/pybind11) and (optionally)
[OpenMP](https://www.openmp.org/)

`pygram11` provides fast functions for generating histograms (and
their sums-of-weights squared). Some benchmarks are shown in the
documentation. The API is very simple, check out the documentation
(you'll also find some benchmarks there).

## Installing

pygram11 requires only NumPy and pybind11 (and therefore a C++
compiler with C++11 support). **Note**: `pybind11` must be installed
explicitly before `pygram11` (because `setup.py` uses `pybind11` to
determine include directories).

### From PyPI

```none
$ pip install pybind11 ## or `conda install pybind11`
$ pip install pygram11
```

### From Source

```none
$ git clone https://github.com/drdavis/pygram11.git
$ cd pygram11
$ pip install .
```

## In Action

A fixed bin width histogram of weighted data in one dimension,
accelerated with OpenMP:

```python
>>> x = np.random.randn(10000)
>>> w = np.random.uniform(0.8, 1.2, 10000)
>>> h, sw2 = pygram11.histogram(x, bins=40, range=(-4, 4), weights=w, omp=True)
>>> stat_err = np.sqrt(sw2)
```

A variable bin width histogram in two dimensions:

```python
>>> x = np.random.randn(10000)
>>> y = np.random.randn(10000)
>>> xbins = [-2.0, -1.0, -0.5, 1.5, 2.0]
>>> ybins = [-3.0, -1.5, -0.1, 0.8, 2.0]
>>> h = pygram11.histogram2d(x, y, bins=[xbins, ybins])
```
