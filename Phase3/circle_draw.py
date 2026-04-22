import cv2

image= cv2.imread('assets/opencv.png')
center=(150, 150)
radius=100
color=(255,0,255)
thickness=4

circle=cv2.circle(image, center, radius,color, thickness )

cv2.imshow('rectangle', circle)
cv2.waitKey(0)
cv2.destroyAllWindows()