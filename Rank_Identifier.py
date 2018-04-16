# ----------------------
# Shape Indetifier
# ----------------------

import cv2

class RankIdentifier:
    def __init__(self):
        pass

    def find(self, contour, Image):

        print('----------------')
        print('Rank Identifier')
        print('----------------')
        print('')
        
        # initialize shape as unknown
        rank = ""
        
        # ------------------------------------------
        # get criteria for identifying contours
        # ------------------------------------------

        # grayscale, blur, and threshold
        ImGray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
        ImBlur = cv2.GaussianBlur(ImGray, (5,5), 0)
        ImThresh = cv2.threshold(ImBlur, 127, 255, cv2.THRESH_BINARY)[1]

        # Ramer-Douglas-Peucker algorithm
        # removes point from contour if deviation less than epsilon
        # epsilon as a fraction of approximate arc length
        perim = cv2.arcLength(contour, True)
        epsilon = 0.01 * perim
        RDP = cv2.approxPolyDP(contour, epsilon, True)

        # number of vertices in contour
        vert = len(RDP)
        print('vertices :', vert)

        # perim and area of RDP contour
        perimRDP = cv2.arcLength(RDP, True)
        print('RDP perim:', round(perimRDP,2))
        print('perim    :', round(perim,2))
        
        areaRDP = cv2.contourArea(RDP)
        area = cv2.contourArea(contour)
        print('RDP area :', areaRDP)
        print('area     :', area)

        # ratio of perimeter^2 to area
        p2a = round(((perimRDP**2) / areaRDP),2)
        p2aOrig = round(((perim**2) / area),2)
        print('RDP ratio:', p2a)
        print('ratio    :', p2aOrig)

        # bounding rectangle (x, y, w, h)
        boundRect = cv2.boundingRect(RDP)
        x = boundRect[0]
        y = boundRect[1]
        w = boundRect[2]
        h = boundRect[3]

        # ROI sections
        dw = int(w/6)
        dh = int(h/8)
        sections = [
            ((x, y), (x+w, y+h)),       # [0] whole
            ((x, y), (x+w, y+dh)),      # [1] top
            ((x, y), (x+dw, y+h)),      # [2] left side
            ((x+w-dw, y), (x+w, y+h)),  # [3] right side
            ((x, y+h-dh), (x+w, y+h)),  # [4] bottom
            ]
        
        pctBLKPix = [0] * len(sections)
        
        print('')
        print('[0] Whole: [1] Top: [2] Left: [3] Right: [4] Bottom')

        # black pixel % of ROI
        ROI = ImThresh[y:y+h, x:x+w]
        for (i, ((xA, yA), (xB, yB))) in enumerate(sections):
            sectROI = ImThresh[yA:yB, xA:xB]
            sectWHTPix = cv2.countNonZero(sectROI)
            sectArea = (xB - xA) * (yB - yA)
            sectPctBLKPix = 100 * (1 - (sectWHTPix / sectArea))

            pctBLKPix[i] = sectPctBLKPix

            print('[',i,'] Blk %:', round(sectPctBLKPix,2),'%')

        print('')
        
        # minimum area rectangle
        (x1,y1),(w1,h1),theta = cv2.minAreaRect(RDP)
        print('angle    :', round(theta,2))

        # ------------------------------------------
        # identify contours based on above criteria
        # ------------------------------------------
            
        # Ace
        # 12 < vert < 16
        # 36 < p2a < 44
        if (    vert >= 12
            and vert <= 16
            and p2a >= 36
            and p2a <= 44):
            rank = "Ace"
            
        # King
        # 16 < vert < 20
        # 78 < p2a < 86
        elif (    vert >= 16
              and vert <= 20
              and p2a >= 78
              and p2a <= 86
              and pctBLKPix[4] > 60):
            rank = "King"

        # Queen
        # 12 < vert < 16
        # 16 < p2a < 24
        elif (    vert >= 12
              and vert <= 16
              and p2a >= 16
              and p2a <= 24
              and pctBLKPix[4] > 50
              and pctBLKPix[4] < 70):
            rank = "Queen"

        # Jack
        # 13 < vert < 17
        # 60 < p2a < 68
        elif (    vert >= 13
              and vert <= 17
              and p2a >= 60
              and p2a <= 68
              and pctBLKPix[1] < 50):
            rank = "Jack"

        # 9
        # 14 < vert < 18
        # 26 < p2a < 34
        elif (    vert >= 14
              and vert <= 18
              and p2a >= 26
              and p2a <= 34
              and pctBLKPix[3] > 40):
            rank = "9"

        # 8
        # 13 < vert < 17
        # 15 < p2a < 19
        elif (    vert >= 13
              and vert <= 17
              and p2a >= 15
              and p2a <= 19
              and pctBLKPix[3] < 45):
            rank = "8"

        # 7
        # 10 < vert < 14
        # 56 < p2a < 64
        elif (    vert >= 10
              and vert <= 14
              and p2a >= 56
              and p2a <= 64):
            rank = "7"

        # 6
        # 14 < vert < 18
        # 26 < p2a < 30
        elif (    vert >= 14
              and vert <= 18
              and p2a >= 26
              and p2a <= 30
              and pctBLKPix[2] > 40):
            rank = "6"

        # 5
        # 16 < vert < 20
        # 76 < p2a < 84
        elif (    vert >= 16
              and vert <= 20
              and p2a >= 76
              and p2a <= 84
              and pctBLKPix[1] < 65):
            rank = "5"

        # 4
        # 13 < vert < 17
        # 26 < p2a < 34
        elif (    vert >= 13
              and vert <= 17
              and p2a >= 26
              and p2a <= 34):
            rank = "4"

        # 3
        # 16 < vert < 20
        # 80 < p2a < 88
        elif (    vert >= 16
              and vert <= 20
              and p2a >= 80
              and p2a <= 88):
            rank = "3"

        # 2
        # 13 < vert < 17
        # 76 < p2a < 84
        elif (    vert >= 13
              and vert <= 17
              and p2a >= 76
              and p2a <= 84):
            rank = "2"

        # 1
        # 3 < vert < 7
        # 40 < p2a < 48
        elif (    vert >= 3
              and vert <= 7
              and p2a >= 40
              and p2a <= 48):
            rank = "1"

        # 0
        # 7 < vert < 10
        # 12 < p2a < 20
        elif (    vert >= 7
              and vert <= 10
              and p2a >= 12
              and p2a <= 20):
            rank = "0"

        # otherwise, dunno
        else:
            rank = "IDFK"
        
        print('rank     :', rank)
        print('')
        
        return rank

    def approxCont(self, contour):
        # epsilon as a fraction of approximate arc length
        epsilon = 0.01 * cv2.arcLength(contour, True)

        # Ramer-Douglas-Peucker algorithm
        # removes point from contour if deviation less than epsilon
        RDP = cv2.approxPolyDP(contour, epsilon, True)

        return RDP

    def boundRectangle(self, contour):
        # bounding rectangle (x, y, w, h)
        boundRect = cv2.boundingRect(contour)

        return boundRect
