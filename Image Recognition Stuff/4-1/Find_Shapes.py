# ----------------------
# Find Shapes
# ----------------------

# run by opening powershell window in folder and typing python Find_Shapes.py

from Rank_Identifier import RankIdentifier
#from Suit_Identifier import SuitIdentifier
import numpy as np
import argparse
import imutils
import cv2

# import image from command line
#AP = argparse.ArgumentParser()
#AP.add_argument("-i", "--image", required = True,
               # help = "path to the imput image")
#args = vars(AP.parse_args())

# load image
#Image = cv2.imread(args["image"])
Image = cv2.imread(r"Test Images\allRanksSuits.png")
print (Image.shape)

#cv2.imshow("Original",Image)

# convert to grayscale
ImGray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)

#cv2.imwrite("Out_Images\A_gray.jpg", ImGray)

# Guassian blur
ImBlur = cv2.GaussianBlur(ImGray, (5,5), 0)

#cv2.imwrite("Out_Images\A_blur.jpg", ImBlur)

# threshold
ImThresh = cv2.threshold(ImBlur, 127, 255, cv2.THRESH_BINARY)[1]

#cv2.imwrite("Out_Images\A_thresh.jpg",ImThresh)

# find all contours in ImThresh
allComponents = cv2.findContours(ImThresh, cv2.RETR_TREE,
                             cv2.CHAIN_APPROX_SIMPLE)

allContours = allComponents[1]
allHierarchies = allComponents[2]
# hierarchy format [next, previous, 1st child, parent]
# -1 if does not exist

# initialize Rank and Suit Identifiers
RankIdent = RankIdentifier()
#SuitIdent = SuitIdentifier()

# identify contours
for contour in allContours:
#for component in allComponents:

    #contour = component[1]
    #hierarchy = component[2]

    # find centroid of contour
    M = cv2.moments(contour)
    if M["m00"] != 0:
        centerX = int(M["m10"] / M["m00"])
        centerY = int(M['m01'] / M['m00'])
    else:
        centerX, centerY = 0, 0
        
    # find rank
    rank = RankIdent.find(contour)

    # find suit
    #suit = SuitIdent.find(contour)

    # outline each shape detected
    #cv2.drawContours(Image, [contour], -1, (0, 255, 0), 2)
    
    # draw approximate contour
    RDP = RankIdent.approxCont(contour)
    cv2.polylines(Image, [RDP], True, (0, 255, 255), 2)
    
    cv2.putText(Image, rank, (centerX, centerY), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 0), 2)

    # show image within loop, each outline is added when key pressed
    cv2.imshow("Image", Image)
    cv2.waitKey(0)

# write output image to file
#cv2.imwrite("Out_Images\A_shapes.jpg", Image)
    
