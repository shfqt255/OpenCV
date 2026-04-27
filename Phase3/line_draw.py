import cv2

image= cv2.imread('assets/opencv.png')

line= cv2.line(image, (20, 30), (500,30 ), (255, 245, 0), 4) # 4 for thickness

cv2.imshow('line', line)
cv2.waitKey(0)
cv2.destroyAllWindows()