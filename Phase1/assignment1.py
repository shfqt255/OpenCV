import cv2

image=cv2.imread('Phase1/assets/opencv.png')
if image is None:
    print("Error: Could not read the image.")
    exit()


save_show=input("Do you want to save or show the image (s/h): ")

if(save_show=='s'):
    path=input('Enter the path of an image where you want to save: ')
    name=input('Enter the name of the image: ')
    cv2.imwrite(path+'/'+name, image)
    print("Image saved successfully")

elif(save_show=='h'):
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Invalid input")