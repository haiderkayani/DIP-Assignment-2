import cv2
import numpy as np

def label(image):
    labeled_image = np.zeros_like(image)
    neighbours = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
    
    label = 1
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i,j] == 255 and labeled_image[i,j] == 0:
                stack = [(i,j)]
                while stack:
                    current_i, current_j = stack.pop()
                    labeled_image[current_i, current_j] = label
                    for x, y in neighbours:
                        ni, nj = current_i+x, current_j+y
                        if 0<=ni<image.shape[0] and 0<=nj<image.shape[1] and image[ni,nj] == 255 and labeled_image[ni,nj] == 0:
                            stack.append((ni,nj))
                            
                label = label+1
    return labeled_image
              
original_image = cv2.imread("Image_01.bmp", cv2.IMREAD_GRAYSCALE)
labeled_image = label(original_image)

cv2.imshow("Original image", original_image)
cv2.imshow("Labeled objects image", labeled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()