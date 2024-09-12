# %% More exercises to generate images and interesting plots

# %% Imports
import matplotlib.pyplot as plt
import numpy as np

# %% Stacking arrays
# In python, you stack arrays with numpy functions, not [] syntax
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
# Note that the list of things to stack has to be a LIST, i.e. you have to use []
# Stack Vertically (Vstack)
c = np.vstack([a, b])
print(c)

# Stack Horizontally (Hstack)
d = np.hstack([a, b])
print(d)

# %% Stacking in depth
r1 = np.random.rand(4,4)
r2 = np.random.rand(4,4)

# %%
r3a = np.dstack([r1, r2])
print(r3a)
print(r3a.shape)
# Stack with new dimension first
r3b = np.array([r1, r2])
print(r3b.shape)

# %%
# Stack in arbitrary dimension
# remember python is zero-based, so axis=2 means THIRD axis
r3c = np.concatenate([r1[:,:,np.newaxis], r2[:,:,np.newaxis]], axis=2) 
print(r3c.shape)

# %% For loops

for i in ['hi','my','name','is', 'bob']: # range(10):
    print(i)

# %% A few ways to solve the same problem in python: (1) build a list
my_list = []
for i in range(10):
    row = np.arange(i, i+10)
    my_list.append(row)
# combine the arrays in the list into one big array (will be 10x10)
image = np.array(my_list)

plt.imshow(image)
plt.show()

# %% (2) one-line list comprehension
image2 = np.array([np.arange(i, i+10) for i in range(10)])
plt.imshow(image2)
plt.show()

# %% (3) matlab-like, pre-allocating array
image = np.zeros((10,10))
for i in range(10):
    image[i,:] = np.arange(i, i+10)

plt.imshow(image)
plt.show()


# %% Continuation: how would you...
# (There are several ways to do this! try to think of multiple ways)

# Make a vertical gradient? (increasing values from top to bottom?)
image = np.zeros((10,10))
for i in range(10):
    image[i,:] = i #np.arange(i, i+10)

plt.imshow(image)
plt.show()
# Make a horizontal gradient? (increasing values from left to right?)



# %% Defining functions
# sadly cart2pol and pol2cart don't exist in numpy, but the good news is we
# can define them prety easily as FUNCTIONS. We will use slightly more pythonic
# names.

def cart_to_pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return theta, rho

def pol_to_cart(theta, rho):
    x = rho * np.cos(theta)
    y = rho * np.sin(theta)
    return x, y


# %% Making circles
# Define a mesh grid from -1 to 1
t = np.linspace(-1, 1, 101)
x, y = np.meshgrid(t, t)

# Convert the grid to polar coordinates!
theta, rho = cart_to_pol(x, y)

# Show the radial dimension
plt.imshow(rho)
plt.show()

# %% threshold the radial dimension to get a circle!
circ = rho < 0.5
plt.imshow(circ)
plt.show()



# %% Defining a circle function
def make_circle(size):
    """This is a docstring! Provide useful information here.
    
    Parameters
    ----------
    size : scalar
        How large the circle image should be on one side.
    """

    t = np.linspace(-1, 1, size)
    x, y = np.meshgrid(t, t);
    theta, rho = cart_to_pol(x, y)
    circle_out = rho < 1;
    return circle_out

circ = make_circle(101)
plt.imshow(circ)
plt.show()
