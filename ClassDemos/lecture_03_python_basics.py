# %% Python demos of simple number generation 
# -*- coding: utf-8 -*-
"""
Basic demonstration of some differences bewteen python (and numpy and 
matplotlib) and matlab
"""

# %% Basic python
# simple types
# A scalar (standalone number) integer
a = 1
b = [3, 6, 9, 12]
c = 3

# %% Operations with basic python syntax:
# What will happen with:

print(a * c)

# %% Operations with basic python syntax:
# What will happen with:

print(b * c)


# %% Strings
# Strings are nice in python
s = 'hello_world'
print(s)

# Two ways to format strings
my_number = 10
s_formatted_1 = 'I think this class is a %d'%my_number
s_formatted_2 = f'I think this class is a {my_number:d}'


# %% Imports
# To be able to use many numerical functions, you have to IMPORT numpy
# When you import modules, you can give them a cute little name. By convention,
# numpy is nearly always imported as np

import numpy as np

# Create an array like b above
d = np.array([3, 6, 9, 12])

# %%
print(d * c)

# Continued in number generation example code!


# %% Exercises

# 1 Use np.pi instead of my_number above, and format a string with pi to 5 decimal places

# 2 Create a list of strings for 'subject01', 'subject02', etc up to 'subject10'

 