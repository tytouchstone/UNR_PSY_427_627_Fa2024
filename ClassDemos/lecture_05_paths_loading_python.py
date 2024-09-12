# Python loading data
# %% PRIOR TO RUNNING: Install new libraries!
# conda install h5py 
# Imports
# Dealing with array data
import numpy as np
# Dealing with paths
import pathlib
import glob
import os
# To load and show images
import matplotlib.pyplot as plt
# Alternative to load arrays
import h5py

# %% String file paths
# Combine elements of a string
string_1 = 'hello'
string_2 = 'world'
new_string = string_1 + string_2
print(new_string)

# Join with .join() method
spacer = ' '
spacer.join(['hello', 'world'])

# %% Combining strings into file paths
import os
# curdir() gives you '.', the indicator for (right here)
base_dir1 = os.curdir()
print(base_dir1)
# Convert that to the actual path to where you are
base_dir1 = os.path.abspath(os.curdir)
print(base_dir1)
# Join that with something else
my_file_1 = os.path.join(base_dir1, 'test.txt')
print(my_file_1)
# Check if that file is there
print('Does my file exist?', os.path.exists(my_file_1))

# %% Alternative: pathlib
# pathlib is a builtin python library, no need to install
base_dir_2 = pathlib.Path('.')
base_dir_2 = base_dir_2.absolute()
my_file_2 = base_dir / 'test.txt'
print('Does my file exist?', my_file_2.exists())
# %% Get all files in a directory
# glob is a builtin python library, no need to install
import glob
files_a = os.listdir()
files_b = glob.glob('*') # Supports wild card (*) syntax

# or: 
files_c = base_dir_2.glob('*')
print(files_c)

# %% Read text from a file
fname = 'makeCircle.m'
with open (fname) as fid:
    # get all lines of file
    lines = fid.readlines()
print(lines)

# %% save arrays
# Create a random array
a = np.random.rand(10,10)
# Save it
np.save('test_array_1.npy', a)
# Save multiple arrays
b = np.random.rand(20,10)
np.savez('test_arrays_2.npz', a=a, b=b)

# %% Load arrays
a_loaded = np.load('test_array_1.npy')
print('Is it the same after loading?', np.all(a==a_loaded))

dict(np.load())

# %% save with h5py
q = np.random.rand(10,10)
with h5py.File('test_array.hdf', mode='w') as fid:
    fid.create_dataset('data', data=q)

# Load back in
with h5py.File('test_array.hdf', mode='r') as fid:
    q_loaded = fid['data'][:]

# %% Load images
fdir = '/Users/mark/pomsync/mark/Teaching/PSY427_627/datasets/fLoc_stimuli'
# Load image
im = plt.imread(os.path.join(fdir, 'adult-1.jpg'))
# display image
plt.imshow(im)