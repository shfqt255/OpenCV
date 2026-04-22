import cv2

image = cv2.imread('assets/opencv.png')

# Get image dimensions
height, width = image.shape[:2]

# Define the center of the image
center = (width // 2, height // 2)

# Define the angle of rotation
angle = 45

# Get the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0) # scale 1.0 means no scaling and 0.5 means half scaling and 2.0 means double scaling
# scale means zoom in or zoom out of the image

# Rotate the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()