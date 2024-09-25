from psychopy import visual, core, event
import random
import colorsys
import numpy as np

# Initialize the window
win = visual.Window([800, 600], color=(0.5, 0.5, 0.5), units='pix')  # Grey background


# Function to generate a random color from hue space
def random_rgb_from_hue(hue):
    rgb = colorsys.hsv_to_rgb(hue, 1, 1)  # Full saturation and value
    return rgb


# Function to generate a color pair based on hue distance
def generate_color_pair():
    base_hue = random.random()  # Random base hue between 0 and 1
    delta_hue = random.uniform(0.1, 0.5)  # Random distance in hue space

    color1 = random_rgb_from_hue(base_hue)
    color2 = random_rgb_from_hue((base_hue + delta_hue) % 1)  # Ensure it's within [0, 1] hue range

    # Calculate color distance
    color_distance = abs(delta_hue)

    # Adjusted distance labels
    if color_distance <= 0.1:
        distance_label = 'Near Color D'
    elif color_distance <= 0.2:
        distance_label = 'Mid Color D'
    elif color_distance <= 0.4:
        distance_label = 'Mid-Far Color D'
    else:
        distance_label = 'Far Color D'

    return color1, color2, color_distance, distance_label


# Function to create a star shape
def create_star(pos, size, color):
    radius_outer = size / 2
    radius_inner = radius_outer * 0.5

    # Angles for a star pointing straight up
    angles_outer = np.linspace(-np.pi / 2, -np.pi / 2 + 2 * np.pi, 6)[:-1]
    angles_inner = angles_outer + np.pi / 5

    vertices = []
    for outer, inner in zip(angles_outer, angles_inner):
        vertices.append([radius_outer * np.cos(outer), radius_outer * np.sin(outer)])
        vertices.append([radius_inner * np.cos(inner), radius_inner * np.sin(inner)])

    return visual.ShapeStim(
        win=win,
        vertices=vertices,
        pos=pos,
        fillColor=color,
        lineColor=color,
        ori=180  # Ensure star points up
    )


# Function to draw a flipped 'U' shape (∩) without tails and pushed down
def draw_U_shape():
    U_vertices = []
    for x in np.linspace(-600, 600, 100):  # Wider U (widened to 2x)
        y = 0.005 * (x ** 2) - 300  # Adjusted to flip, widen the U, and lower it
        # Removing tails by ensuring the ends of the U meet at the same y-value
        if 20 <= abs(x) <= 150:  # Only include vertices where x is between 50 and 100
            U_vertices.append((x, y))

    return visual.ShapeStim(win=win, vertices=U_vertices, lineColor='black', fillColor=None, lineWidth=5)


# Experiment parameters
n_blocks = 3
colors_per_block = 20
block_duration = 20  # seconds
inter_block_interval = 3  # seconds
gap_between_pairs = 0.25  # seconds

# Labels for color distances
labels = ['Near Color D', 'Mid Color D', 'Mid-Far Color D', 'Far Color D']

# Start the experiment
for block in range(n_blocks):
    block_timer = core.Clock()

    # Display 20 color pairs per block (1 second per pair)
    for pair in range(colors_per_block):
        # Generate a pair of colors
        color1, color2, color_distance, distance_label = generate_color_pair()

        # Create star stimuli
        star1 = create_star(pos=(-200, 0), size=200, color=color1)
        star2 = create_star(pos=(200, 0), size=200, color=color2)

        # Draw the stars
        star1.draw()
        star2.draw()

        # Display the color distance and distance label at the top
        message = visual.TextStim(win, text=f'Color Distance: {color_distance:.2f} - {distance_label}', pos=(0, 220),
                                  color=(1, 1, 1))
        message.draw()

        # Draw category labels below the stars
        # for i, label in enumerate(labels):
        #     label_stim = visual.TextStim(win, text=label, pos=(-200 + i * 100, -300), color=(1, 1, 1))
        #     label_stim.draw()

        # Draw a wider 'U' shape below the stars, moved closer
        U_shape = draw_U_shape()
        U_shape.draw()

        win.flip()
        core.wait(1)

        # Clear screen (gap of 0.25 seconds)
        win.flip()
        core.wait(gap_between_pairs)

    # After each block, wait for 3 seconds before starting the next block
    if block < n_blocks - 1:
        win.flip()
        core.wait(inter_block_interval)

# Close the window and exit
win.close()
core.quit()
