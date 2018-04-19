from FindCircles import *
from BotDirection import *
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #frame = frame[0:500, 0:500]
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #threshold images to make finding circles easier
    #circles are dark-grey to black.

    print(getTurnDirectionToHome(gray))
    circles = FindCircles(frame)

    gray = FindCircles_PrintCirclesOnImage(gray, circles)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()