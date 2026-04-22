import cv2

image=cv2.imread('assets/opencv.png')

flip_horizontal=cv2.flip(image, 1)
flip_vertical=cv2.flip(image,0)
flip_both=cv2.flip(image, -1)

cv2.imshow('Original Image', image)
cv2.imshow('Flip Horizontal', flip_horizontal)
cv2.imshow('Flip Vertical', flip_vertical)
cv2.imshow('Flip Both', flip_both)
cv2.waitKey(0)
cv2.destroyAllWindows()