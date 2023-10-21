import cv2
import numpy as np
import random

input_image = cv2.imread("Image_01.bmp", 0)
_, thresholded_image = cv2.threshold(input_image, 128, 255, cv2.THRESH_BINARY)

def dfs(label, x, y):
    stack = [(x,y)]
    while stack:
        i, j = stack.pop()
        labels[i,j] = label

        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if dx==0 and dy==0:
                    continue
                new_x, new_y = i+dx, j+dy
                if 0<=new_x<input_image.shape[0] and 0<=new_y<input_image.shape[1] and thresholded_image[new_x, new_y]==255 and labels[new_x, new_y]==0:
                    stack.append((new_x, new_y))

labels = np.zeros_like(thresholded_image)
label = 1

for i in range(thresholded_image.shape[0]):
    for j in range(thresholded_image.shape[1]):
        if thresholded_image[i, j] == 255 and labels[i, j] == 0:
            dfs(label, i, j)
            label = label+1

output_image = np.zeros((input_image.shape[0], input_image.shape[1], 3), dtype=np.uint8)
colors = [tuple(np.random.choice(range(256), size=3)) for _ in range(label)]

for i in range(1, label):
    output_image[labels == i] = colors[i]

cv2.imshow("Labeled Image", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
