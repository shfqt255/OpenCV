import cv2

image=cv2.imread('assets/opencv.png')

# cv2.putText(image, text, org, font, fontScale, color, thickness, lineType)

cv2.putText(image, 'Hello Python Programmers', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

cv2.imshow('putText', image)
cv2.waitKey(0)
cv2.destroyAllWindows()