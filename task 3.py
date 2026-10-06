import numpy as np

image = np.random.randint(0, 256, size=(5, 5))
img_min = np.min(image)
img_max = np.max(image)
img_mean = np.mean(image)

threshold = 128
mask = image > threshold
thresholded_image = np.where(mask, 255, 0)

print("Original Image Matrix:\n", image)
print("Min Intensity:", img_min)
print("Max Intensity:", img_max)
print("Mean Intensity:", img_mean)
print("Binary Mask:\n", mask)
print("Thresholded Image:\n", thresholded_image)
