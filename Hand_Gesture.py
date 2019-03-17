import cv2
import numpy as np


hand = cv2.imread('capture.png', 0)

cv2.imshow('Original Image', hand)

cv2.waitKey(0)
cv2.destroyAllWindows()
