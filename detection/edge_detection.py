import cv2

image = cv2.imread('assets/opencv.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edge = cv2.Canny(gray, 100, 200)

cv2.imshow('edge', edge)
cv2.imshow('original', image)

cv2.waitKey(0)
cv2.destroyAllWindows()