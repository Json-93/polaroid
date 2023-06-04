import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('test.jpg')
height, width, _ = img.shape

plus_height = 500
plus_width = 200

white_edge = np.ones((height + plus_height, width + plus_width, 3), np.uint8) * 255

polaroid_up = 200
polaroid_edge = 100

my_polaroid = white_edge.copy()
my_polaroid[polaroid_up:polaroid_up + height, polaroid_edge:polaroid_edge + width] = img

plt.imshow(cv.cvtColor(my_polaroid, cv.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
cv.imwrite('polaroid.jpg', my_polaroid)
