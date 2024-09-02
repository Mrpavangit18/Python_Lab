# Task 1: Using a Sobel Filter, filter the image and then display it.

import matplotlib.pyplot as plt
from scipy import ndimage, misc
import numpy as np

# Load the image from the provided path
image_path = 'dogs.jpeg'  # Make sure this matches the uploaded image's name

# Load the image using matplotlib
image = plt.imread(image_path)

# Display the original image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')

# Convert the image to grayscale
gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

# Apply Sobel filter on the grayscale image
sobel_x = ndimage.sobel(gray_image, axis=0)
sobel_y = ndimage.sobel(gray_image, axis=1)
sobel_magnitude = np.hypot(sobel_x, sobel_y)

# Normalize the magnitude to range [0, 255]
sobel_magnitude = (sobel_magnitude / sobel_magnitude.max()) * 255

# Display the Sobel filtered image
plt.subplot(1, 2, 2)
plt.imshow(sobel_magnitude, cmap='gray')
plt.title("Sobel Filtered Image")
plt.axis('off')

plt.show()
