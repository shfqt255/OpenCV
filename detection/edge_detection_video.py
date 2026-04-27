import cv2 

video= cv2.VideoCapture(0)

while True:
    ret, frame= video.read()
    gray_frame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    edge_frame= cv2.Canny(gray_frame, 100,200) # 100 is lower threshold means edges l, 200 is upper threshold 
    cv2.imshow("Edges Detected", edge_frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()

    
