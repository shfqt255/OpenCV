import cv2

image= cv2.imread('assets/opencv.png')

gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

bgr_image= cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

# It takes the gray value
# Copies it into 3 channels (B, G, R)
# So each pixel becomes:
# (gray, gray, gray)

cv2.imshow('BGR', bgr_image)
cv2.waitKey(0)
cv2.destroyAllWindows()