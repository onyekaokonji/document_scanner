""" Perspective Transform"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('b_o_a_t.jpeg')
img_copy = img.copy()

img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)

# the 4 corners of the object in an anti-clockwise direction
# starting from the top left corner
pointA = [1588, 892]
pointB = [1577, 2696]
pointC = [4026, 2707]
pointD = [3982, 914]

# calculate the width and height of the object in question
width_AD = np.sqrt(((pointA[0] - pointD[0]) ** 2) + ((pointA[1] - pointD[1]) ** 2))
width_BC = np.sqrt(((pointB[0] - pointC[0]) ** 2) + ((pointB[1] - pointC[1]) ** 2))
maxWidth = max(int(width_AD), int(width_BC))

height_AB = np.sqrt(((pointA[0] - pointB[0]) ** 2) + ((pointA[1] - pointB[1]) ** 2))
height_CD = np.sqrt(((pointC[0] - pointD[0]) ** 2) + ((pointC[1] - pointD[1]) ** 2))
maxHeight = max(int(height_AB), int(height_CD))

# get input and output coordinates | input is the coordinates of the warped image, output is the desired coordinates
input_points = np.float32([pointA, pointB, pointC, pointD]) # Top-Left, Bottom-Left, Bottom-Right, Top-Right
output_points = np.float32([[0, 0], [0, maxHeight-1], [maxWidth-1, maxHeight-1], [maxWidth-1, 0]]) # Top-Left, Bottom-Left, Bottom-Right, Top-Right

# perform perspective transform
perspective_matrix = cv2.getPerspectiveTransform(src=input_points, dst=output_points)
new_img = cv2.warpPerspective(img, perspective_matrix, (maxWidth, maxHeight), flags=cv2.INTER_LINEAR)
new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB)

plt.imsave('./new_image.jpeg', new_img)

plt.imshow(new_img)
plt.show()