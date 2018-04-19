from FindCircles import *
import cv2
import numpy as np

#Steps to do:
#1) get 2 ROIs of the input image(vertical)
#2) count the circles in each of the ROIs or measure distance of each circle from centre(if there is 1 circle in each ROI) 
#3) then determine which direction the robot must turn in

#test_img = cv2.imread('/Users/josephsundar/Desktop/2Center.jpg')

def getTurnDirectionToHome(inputFrame):
    #get 2 ROIs of the input image(vertical)
    height = int(np.size(inputFrame, 0))
    width = int(np.size(inputFrame, 1))
    leftROI = inputFrame[0:height, 0:int(width/2)]
    rightROI = inputFrame[0:height, int(width/2):width]


    #count the circles in each of the ROIs:
    #Find the circles in ROIs
    circles_RightROI = FindCircles(rightROI)
    #FindCircles_PrintCirclesOnImage(rightROI, circles_RightROI)
    circles_leftROI = FindCircles(leftROI)
    #FindCircles_PrintCirclesOnImage(leftROI, circles_leftROI)

    #check count on each image
    numCirLeft = FindCircles_getNumCircles(circles_leftROI)
    numCirRight = FindCircles_getNumCircles(circles_RightROI)

    #check is we have two circles on either side:
    if ((numCirLeft == 1) and (numCirRight == 1)):
        #print("[+] Found 1 circle on each ROI! Potentially Found Home\n")
        #Now we calculate distances to the centre mark.
        distLeft, distRight = FindCircles_calculateDistances(circles_leftROI, circles_RightROI, int(width/2), 0)
        print(distLeft, distRight)
        #get a suggestion for turn Direction
        if (distLeft - distRight) > 15:
            return '[L]'
        elif (distRight - distLeft) > 15:
            return '[R]'
        else:
            return '[F]'
    #if there's only one circle on one of the ROIs
    elif((numCirLeft + numCirRight) == 1):
        #print('[-] Cannot Find Home!     Detected circles in left ROI: ' + str(numCirLeft) + '    Detected circles in right ROI: ' + str(numCirRight))
        if numCirLeft > 0:
            return '[LA]'
        elif numCirRight > 0:
            return '[RA]'

    elif((numCirLeft + numCirRight) > 2):
        return '[Err]'

    