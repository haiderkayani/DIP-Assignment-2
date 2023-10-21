import cv2
import numpy as np

original_image = cv2.imread("Image_01.bmp")

cv2.imshow("test", original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()