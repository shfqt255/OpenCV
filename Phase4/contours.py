import cv2

image= cv2.imread('assets/opencv.png',0)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary Image",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours, hierarchy= cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print(f"Found {(contours)} contours")


cv2.drawContours(image, contours, -1, (0,255,0), 3)

cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()