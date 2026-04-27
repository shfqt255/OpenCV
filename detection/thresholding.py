import cv2

image = cv2.imread('assets/opencv.png', 0) # 0 for grayscale

thresh, result = cv2.threshold(image, 125, 255, cv2.THRESH_BINARY) # 125 for the threshold and 255 for the maximum value    
# which means if the pixel value is greater than 125, it will be set to 255 and will be considered as white and will be considered as edges
# and if the value is less than 125, it will not be set to 0 and will not be considered as black and will not be considered as background and it will be considered as foreground
# which is also called as thresholding

cv2.imshow('thresholding', result)
cv2.imshow('original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()