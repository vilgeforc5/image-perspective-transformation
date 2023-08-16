import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import sys



for img_path in sys.argv[1:]:
    img = cv.imread(img_path)
    img1 = img.copy()
    circles = [
        [100,150, (0,0,255)], 
        [600, 90, (0,0,255)], 
        [72, 400, (0,0,255)],
        [637, 420, (0,0,255)]]

    key = ''
    redraw_image = False
    current_Circle = None
    def getXY(evt, x,y, flags, userdata ):
        if evt == cv.EVENT_LBUTTONDOWN:
            if current_Circle in [0,1,2,3]:
                circles[current_Circle][0] = x
                circles[current_Circle][1] = y

    print("PRESS q TO TERMINATE ")
    print("PRESS  1/2/3/4 BUTTON TO SELECT CORRESPONDING VERTEX TO BE CHANGED")
    print("PRESS ON IMAGE PART TO CHANGE VERTEX LOCATION")


    while (1): 
        for circle in circles:
            cv.circle(img1, (circle[0], circle[1]), 10, circle[2],2)

        if redraw_image:
            img1 = img.copy()
            for circle in circles:
                cv.circle(img1, (circle[0], circle[1]), 10, circle[2],2)

        
        cv.setMouseCallback("Origin", getXY, "")

        imgPts = np.float32([
            [circles[0][0],circles[0][1]],
            [circles[1][0], circles[1][1]],
            [circles[2][0], circles[2][1]],
            [circles[3][0], circles[3][1]]])
        objPoints = np.float32([[0,0],[600, 0],[0,900],[600,900]])
        matrix = cv.getPerspectiveTransform(imgPts,objPoints)
        result = cv.warpPerspective(img,matrix,(600,900))
        cv.imshow('Origin',img1)
        cv.imshow('Transform',result)
        key = cv.waitKey(1)
        if key == ord('q') & 0xFF:
            break

        plt.show()
        

        if (key == ord('1') & 0xFF):
            circles[0][2] = (0,255,0)
            circles[1][2] = (0,0,255)
            circles[2][2] = (0,0,255)
            circles[3][2] = (0,0,255)
            current_Circle = 0
            redraw_image = True


            
            
        elif (key == ord('2') & 0xFF):
            circles[0][2] = (0,0,255)
            circles[1][2] = (0,255,0)
            circles[2][2] = (0,0,255)
            circles[3][2] = (0,0,255)
            current_Circle = 1
            redraw_image = True

        elif (key == ord('3') & 0xFF):
            circles[0][2] = (0,0,255)
            circles[1][2] = (0,0,255)
            circles[2][2] = (0,255,0)
            circles[3][2] = (0,0,255)
            current_Circle = 2
            redraw_image = True

        elif (key == ord('4') & 0xFF):
            circles[0][2] = (0,0,255)
            circles[1][2] = (0,0,255)
            circles[2][2] = (0,0,255)
            circles[3][2] = (0,255,0)
            current_Circle = 3
            redraw_image = True
        else: 
            continue

