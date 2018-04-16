# ------------------------------------------
# Get Card Rank and Suit
# ------------------------------------------

from Identifier import Identify
import numpy as np
import argparse
import imutils
import cv2


def cardInfo(Image):
    # ------------------------------------------
    # Initial Image Operations
    # ------------------------------------------

    # load image from main function
    print(Image.shape)

    # convert to grayscale
    ImGray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)

    # Gaussian blur
    ImBlur = cv2.GaussianBlur(ImGray, (5,5), 0)

    # image threshold
    ImThresh = cv2.threshold(ImBlur, 127, 255, cv2.THRESH_BINARY)[1]

    # find all contours and hierarchies in ImThresh
    # findContours = [allContours, allHierarchies]
    allComponents = cv2.findContours(ImThresh, cv2.RETR_TREE,
                                     cv2.CHAIN_APPROX_SIMPLE)

    # allComponents[0] contains the image
    allContours = allComponents[1]
    allHierarchies = allComponents[2]
    allHierarchies = allHierarchies[0]

    print('All Hierarchies')
    print('[next, prev, 1st child, parent]')
    print(allHierarchies)

    # hierarchy format [next, previous, 1st child, parent]
    # -1 if does not exist

    # ------------------------------------------
    # does card need to be rotated?
    # ------------------------------------------
    print('----------------')
    print('Card Rotation')
    print('----------------')



    # ------------------------------------------
    # loop over contours identifying rank & suit
    # ------------------------------------------

    # initialize Identifier
    Ident = Identify()

    # card = [rank, suit]
    card = [0,0]

    for component in zip(allContours, allHierarchies):
        contour = component[0]
        hierarchy = component[1]

        print('Hierarchy')
        print('[next, prev, 1st child, parent]')
        print(hierarchy)

        # find centroid of contour
        M = cv2.moments(contour)
        if M['m00'] != 0:
            centerX = int(M['m10'] / M['m00'])
            centerY = int(M['m01'] / M['m00'])
        else:
            centerX, centerY = 0, 0

        # find rank
        rank = Ident.rank(contour, Image)

        # find suit
        suit = Ident.suit(contour, Image)

        # draw approximate contour
        # note: color scheme is BGR
        if rank != 'IDFK':
            rankRDP = Ident.approxCont(contour)
            cv2.polylines(Image, [rankRDP], True, (0, 255, 255), 2)

        if suit != 'IDFK':
            suitRDP = Ident.approxCont(contour)
            cv2.polylines(Image, [suitRDP], True, (255, 255, 0), 2)

        # draw bounded rectangle and calculate nonzero ratio
        boundRect = Ident.boundRectangle(contour)
        x = boundRect[0]
        y = boundRect[1]
        w = boundRect[2]
        h = boundRect[3]
        dw = int(w/5)
        dh = int(h/8)
        #cv2.rectangle(Image, (x, y+h-dh), (x+w, y+h), (150, 0, 0), 2)

        # put text on image
        if rank != 'IDFK':
            card[0] = rank
            cv2.putText(Image, rank, (centerX, centerY), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)

        if suit != 'IDFK':
            card[1] = suit
            cv2.putText(Image, suit, (centerX, centerY), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 0, 255), 2)

        # show image within loop, each outline is added when key pressed
        cv2.imshow('Image', Image)
        #cv2.waitKey(0)

    # write output image to file
    #cv2.imwrite('Out_Images\A_shapes.jpg', Image)

    #print(card)

    return(card)







    





    
