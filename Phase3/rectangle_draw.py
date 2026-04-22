import cv2

image= cv2.imread('assets/opencv.png')

rectangle=cv2.rectangle(image, (20,30), (150, 160), (255, 255, 0)) # 6 is thickness

cv2.imshow('rectangle', rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()