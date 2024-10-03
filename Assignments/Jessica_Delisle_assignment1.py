# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:20:14 2024

@author: jessy
"""

#%% Base
import os
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

#%% Access images
# Path to the folder containing images
fdir = 'C:/Users/jessy/Desktop/School/Y4/S3/PSY 427/fLoc_stimuli'

# List all files in the folder
all_files = os.listdir(fdir)

# Filter out only the .jpg files
image_files = [file for file in all_files if file.lower().endswith('.jpg')]

# Sort the list of image files
image_files.sort()

print("Sorted list of images:", image_files)

#%% Random selection of images
# Select a random sample of 12 images
sampled_images = random.sample(image_files, 12)

print("Randomly selected images:", sampled_images)


#%% Layout
# Create a figure for displaying images
fig, axes = plt.subplots(3, 4, figsize=(12, 9))

# Flatten axes array for easy indexing
axes = axes.flatten()

for ax, img_file in zip(axes, sampled_images):
    img_path = os.path.join(fdir, img_file)
    img = mpimg.imread(img_path)
    ax.imshow(img)
    ax.axis('off')  # Hide axes
    ax.set_title(img_file)

    
#%% Final
# Resize images to a common size (e.g., 256x256)
common_size = (256, 256)

def load_and_resize_image(img_path, size):
    with Image.open(img_path) as img:
        img = img.resize(size)
        return np.array(img)

# Load images and convert to numpy arrays
image_arrays = [np.array(mpimg.imread(os.path.join(fdir, img_file))) for img_file in sampled_images]

# Stack images into a single 4D array (12, height, width, channels)
image_array_stack = np.stack(image_arrays)

#color
for ax, img_array in zip(axes, image_arrays):
    ax.imshow(img_array, cmap='gray')  # Use grayscale colormap
    ax.axis('off')

plt.tight_layout()
plt.show()

# Save the array to a file
np.save('randomly_selected_images.npy', image_array_stack)

print("Saved image array as 'randomly_selected_images.npy'")


