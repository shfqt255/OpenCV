import cv2

image= cv2.imread('assets/opencv.png', 0)

if image is not None:
    cv2.imwrite('assets\written_image.png', image)
    print('image is written')
if image is None:
    print('could not load the image')
