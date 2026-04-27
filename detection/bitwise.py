import cv2
import numpy as np

# Create two blank images
image1 = np.zeros((300, 300), dtype='uint8')  # Black image
print(image1)
cv2.circle(image1, (150, 150), 100, 255, -1)  # White circle, -1 is for filled circle and 0 is for outline of circle, thickness
print(image1)
image2 = np.zeros((300, 300), dtype='uint8')  # Black image
cv2.rectangle(image2, (50, 50), (250, 250), 255, -1)  # White square
mask = cv2.circle(image1, (150, 150), 100, 255, -1)
# Perform bitwise operations
bitwise_and = cv2.bitwise_and(image1, image2) # where both images are white
bitwise_or = cv2.bitwise_or(image1, image2) # where either image is white
bitwise_xor = cv2.bitwise_xor(image1, image2) # where either image is white but not both
bitwise_not = cv2.bitwise_not(image1) # invert the image

# Display images
cv2.imshow('Original Image', image1)
cv2.imshow('Mask', mask)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.imshow("Bitwise NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()