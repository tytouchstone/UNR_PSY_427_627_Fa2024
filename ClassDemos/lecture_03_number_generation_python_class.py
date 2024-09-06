# %% Python demos of simple number generation 
# First, we need to import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt


# %% sequences
a = np.arange(10)
b = np.linspace(0, 1, 101)
c = np.zeros((4,5)) # note parentheses - input is a TUPLE
d = np.array([1, 2, 3, 4, 7, 12])
# matlab: a = [1, 2, 3, 4, 7, 12]
# in python, that's a LIST


# %% random number generation
e = np.random.uniform() # pythonic way
f = np.random.rand() # matlab-like way

# Add arguments here to get arrays of different sizes
g = np.random.normal() # pythonic way
h = np.random.randn() # matlab way

# %% Basic python vs numpy
#operations
a.mean()
# vs
np.mean(a)
# SAME. See also np.nanmean, np.nanstd

# %% plotting
# by convnetion, matplotlib is imported as plt. So, all your plot functions 
# (most of which will have names similar to Matlab functions) are to be found
# in plt.<whatever>

# Basic lineplot
plt.plot(e)


# %% Image plot
snow_image = np.random.rand(50,50)
plt.imshow(snow_image)
plt.show() # necessary! (usually...)


# %% Scatter plot
 x = ...
 y = ...
 plt.plot(x, y)

# %% Exercises

# As last week: 
# plot a parabola (what is x? what is y?)
# plot a sine wave (what is x? what is y?)

# New challenges: 
# 1. make a scatter plot of dots in a circle
# 2. make an image plot of a sine wave grating (as I demo'd at the end of last week)

# Do some googling! Ask the robots! 