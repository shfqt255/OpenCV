import cv2

image=cv2.imread('assets/opencv.png')

choice= input('Do you want to draw a line, rectangle, circle, triangle, or put text?:l for line, r for rectangle, c for circle, t for triange and p for text: ')

if choice == 'l':
    x1= int(input('Enter x1: '))
    y1= int(input('Enter y1: '))
    x2= int(input('Enter x2: '))
    y2= int(input('Enter y2: '))
    cv2.line(image, (x1, y1), (x2, y2), (255, 245, 0), 4) # 4 for thickness
    cv2.imshow('line', line)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif choice == 'r':
    x1= int(input('Enter x1: '))
    y1= int(input('Enter y1: '))
    x2= int(input('Enter x2: '))
    y2= int(input('Enter y2: '))
    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 255, 0)) # 6 is thickness
    cv2.imshow('rectangle', rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif choice == 'c':
    center= int(input('Enter center: '))
    radius= int(input('Enter radius: '))
    color= int(input('Enter color: '))
    thickness= int(input('Enter thickness: '))
    cv2.circle(image, center, radius,color, thickness )
    cv2.imshow('circle', circle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif choice == 't':
    x1= int(input('Enter x1: '))
    y1= int(input('Enter y1: '))
    x2= int(input('Enter x2: '))
    y2= int(input('Enter y2: '))
    x3= int(input('Enter x3: '))
    y3= int(input('Enter y3: '))
    cv2.triangle(image, (x1, y1), (x2, y2), (x3, y3), (255, 245, 0), 4) # 4 for thickness
    cv2.imshow('triangle', triangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif choice == 'p':
    text= input('Enter text: ')
    cv2.putText(image, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('putText', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Invalid input')
    cv2.destroyAllWindows()