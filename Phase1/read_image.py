import cv2

image=cv2.imread('assets/opencv.png', -1) # -1 for default image, 0 for grayscale, 1 for color image

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()