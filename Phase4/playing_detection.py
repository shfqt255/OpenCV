# week2_playing_start.py
import cv2

cap = cv2.VideoCapture(0)  # Webcam
previous_frame = None

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)  # Reduce noise
    
    if previous_frame is not None:
        # Find differences
        diff = cv2.absdiff(previous_frame, gray)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        
        # Count white pixels
        motion_percent = (cv2.countNonZero(thresh) / thresh.size) * 100
        
        if motion_percent > 10:
            print(f"ACTIVITY: Playing ({motion_percent:.1f}% motion)")
        else:
            print("ACTIVITY: Still")
    
    previous_frame = gray
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()