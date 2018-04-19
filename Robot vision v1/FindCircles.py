import math 
import numpy as np
import cv2


def FindCircles(inputImage, param1, param2):
    if inputImage.shape[-1] == 3:           # color image
        #b,g,r = cv2.split(inputImage)       # get b,g,r
        #rgb_img = cv2.merge([r,g,b])     # switch it to rgb
        gray_img = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)
    else:
        gray_img = inputImage

    img = cv2.medianBlur(gray_img, 5)

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT, 1, 60, param1=param1,param2=param2,minRadius=0,maxRadius=0)
    
    #check if we found circles
    if circles != None:
        #print("[+] Found Circles!: " + str(circles[0]))
        circles = np.uint16(np.around(circles))

        return circles
    else:
        return None

def FindCircles_PrintCirclesOnImage(inputImage, circles):
    if circles != None:
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(inputImage,(i[0],i[1]),i[2],(255,255,255),2)
            # draw the center of the circle
            cv2.circle(inputImage,(i[0],i[1]),2,(255,255,255),3)
        return inputImage
    else:
        return inputImage

def FindCircles_getNumCircles(circles):
    if circles != None:
        return len(circles[0,:])
    else:
        return 0

def FindCircles_calculateDistances(circles_leftROI, circles_RightROI, centerX, centerY):  
    if ((circles_leftROI != None) and (circles_RightROI != None)):
        #get distance for leftROI
        x1 = circles_leftROI[0][0][0]
        y1 = circles_leftROI[0][0][1]
        x2 = centerX
        y2 = centerY
        LeftCenterDistance = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))  
    
        #get distance for leftROI
        x1 = circles_RightROI[0][0][0]
        y1 = circles_RightROI[0][0][1]
        x2 = 0
        y2 = centerY
        RightCenterDistance = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))  
        
        return LeftCenterDistance, RightCenterDistance      

