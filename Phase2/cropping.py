import cv2

image = cv2.imread('assets/opencv.png')

# Crop only top section where HTTP image exists
cropped_image = image[0:250, 150:550]

cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()