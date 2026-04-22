import cv2

image= cv2.imread('assets/opencv.png')

print(image.shape)

resized_image=cv2.resize(image, (300, 300), interpolation=cv2.INTER_AREA)

cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
print(resized_image.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()