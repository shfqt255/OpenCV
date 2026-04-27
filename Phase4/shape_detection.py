import cv2

image= cv2.imread('assets/opencv.png')
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary Image",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours, hierarchy= cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print(f"Found {(contours)} contours")

approx = []
for c in contours:
    # calculate the perimeter of the contour
    perimeter = cv2.arcLength(c, True)
    # approximate the contour
    approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)
cv2.drawContours(image, contours, -1, (0,255,0), 3)

if len(approx) == 3:
    print("Triangle")
elif len(approx) == 4:
    print("Rectangle")
elif len(approx) == 5:
    print("Pentagon")
elif len(approx) == 6:
    print("Hexagon")


cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()