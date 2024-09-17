# Lecture 6: Plotting 
# %% Imports
import matplotlib.pyplot as plt
import numpy as np

# %% Generate data to use below
n_points = 10
line_data_x = np.linspace(0, 10, n_points)
line_data_y = np.random.rand(n_points,)
image_data = np.random.randn(n_points,n_points)
scatter_data_x = np.random.randn(n_points,)
scatter_data_y = scatter_data_x * 2 + np.random.normal(scale=2, size=(n_points,))
bar_data = np.random.rand(2,3)

# %% Line plot
# Generate a figure (default)
fig = plt.figure()
# Plot line data
line_h = plt.plot(line_data_x, line_data_y)
# To expliclity get the axis, you can call: 
# ax = plt.gca(line_data_x, line_data_y)
# And then you can call: 
# ax.plot(line_data_x, line_data_y)
# We will hereafer prefer this syntax as more pythonic
# Add labels
plt.xlabel('X data')
plt.ylabel('Y data')
# Last, make sure plot is shown:
plt.show()
# The result is UGLY! 

# %% Make it pretty: 
# Control size of figure in inches, explicitly get axis at figure creation
fig, ax = plt.subplots(figsize=(6, 4))
nice_red = 'darkred'
fontname = 'arial'
label_size = 24
tk_size = 20
linewidth = 3
yticks = np.round(np.arange(0, 1.01, .2), decimals=1)
ax.plot(line_data_x, line_data_y, linewidth=linewidth, color=nice_red)
ax.set_xlabel('X data', fontsize=label_size, fontname=fontname)
ax.set_ylabel('Y data', fontsize=label_size, fontname=fontname)
ax.set_xticks(np.arange(0, n_points+1, 2))
ax.set_xticklabels(np.arange(0, n_points+1, 2), fontsize=tk_size, fontname=fontname)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks, fontsize=tk_size, fontname=fontname)

# Assure that everything fits within figure
plt.tight_layout 
plt.show()

# %% Save


# %% Scatter plot
fig, ax = plt.subplots()
ax.scatter(scatter_data_x, scatter_data_y)
plt.show()

# TO DO: Make it pretty! 
# Set dot sizes, fonts, 

# Bonus: open up axes, such that only left and bottom axis are shown, not top and right 

# %% Image plot
fig, ax = plt.subplots()
ax.imshow(image_data)
plt.show()

# TO DO: Make it pretty!
# Change the colormap to something biphasic - which shows positive and negative
# values in different colors. Get rid of axis ticks. 


# %% bar plot
# Apologies, the matplotlib bar plot function is terrible.
bar_x = np.arange(bar_data.shape[1])
plt.bar(bar_x, bar_data[0], width=0.4)
plt.bar(bar_x+0.5, bar_data[1], width=0.4)
plt.show()

# TO DO: Make a better bar function by WRAPPING this function. Set x locations
# of each group to be spaced more sensibly (grouped)

# %% Bonus bonus: 
'''Write a function to set all tick labels in a graph to a particular size and
font, and set all axis labels (xlabel and ylabel) to a particular size and 
font. 

Write a function to open the axes up (to get rid of right and top bounding box)

Write a function to set axis linewidths

Write a better bar function! 

'''