# ----------------------
# Shape Indetifier
# ----------------------

import cv2

class RankIdentifier:
    def __init__(self):
        pass

    def find(self, contour):

        # ------------------------------------------
        # get criteria for identifying contours
        # ------------------------------------------
        
        # initialize shape as unknown
        shape = ""

        # epsilon as a fraction of approximate arc length
        perim = cv2.arcLength(contour, True)
        epsilon = 0.01 * perim

        # Ramer-Douglas-Peucker algorithm
        # removes point from contour if deviation less than epsilon
        RDP = cv2.approxPolyDP(contour, epsilon, True)

        # number of vertices in contour
        vert = len(RDP)
        print("vertices: ", vert)

        # perim and area of RDP contour
        perimRDP = cv2.arcLength(RDP, True)
        print('RDP perim:', perimRDP)
        
        areaRDP = cv2.contourArea(RDP)
        print('RDP area: ', areaRDP)

        # ratio of perimeter^2 to area
        p2a = round(((perimRDP**2) / areaRDP),4)
        print('ratio:    ', p2a)

        # bounding rectangle
        (x, y, w, h) = cv2.boundingRect(RDP)

        # minimum area rectangle
        (x1,y1),(w1,h1),theta = cv2.minAreaRect(RDP)
        print('angle:    ', round(theta,2))

        # ------------------------------------------
        # identify contours based on above criteria
        # ------------------------------------------

        # Ace
        # 12 < vert < 16
        # 36 < p2a < 44
        if 12 <= vert and vert <= 16 and 36 <= p2a and p2a <= 44:
            shape = "Ace"
            
        # King
        # 16 < vert < 20
        # 78 < p2a < 86
        elif 16 <= vert and vert <= 20 and 78 <= p2a and p2a <= 86:
            shape = "King"

        # Queen
        # 12 < vert < 16
        # 16 < p2a < 24
        elif 12 <= vert and vert <= 16 and 16 <= p2a and p2a <= 24:
            shape = "Queen"

        # Jack
        # 13 < vert < 17
        # 60 < p2a < 68
        elif 13 <= vert and vert <= 17 and 60 <= p2a and p2a <= 68:
            shape = "Jack"

        # 0
        # 6 < vert < 10
        # 12 < p2a < 20
        elif 6 <= vert and vert <= 10 and 12 <= p2a and p2a <= 20:
            shape = "0"

        # 1
        # 3 < vert < 7
        # 40 < p2a < 48
        elif 3 <= vert and vert <= 7 and 40 <= p2a and p2a <= 48:
            shape = "1"

        # 2
        # 13 < vert < 17
        # 76 < p2a < 84
        elif 13 <= vert and vert <= 17 and 76 <= p2a and p2a <= 84:
            shape = "2"

        # 3
        # 16 < vert < 20
        # 80 < p2a < 88
        elif 16 <= vert and vert <= 20 and 80 <= p2a and p2a <= 88:
            shape = "3"

        # 4
        # 13 < vert < 17
        # 26 < p2a < 34
        elif 13 <= vert and vert <= 17 and 26 <= p2a and p2a <= 34:
            shape = "4"

        # 5
        # 16 < vert < 20
        # 76 < p2a < 84
        elif 16 <= vert and vert <= 20 and 76 <= p2a and p2a <= 84:
            shape = "5"

        # 6
        # 14 < vert < 18
        # 26 < p2a < 30
        elif 14 <= vert and vert <= 18 and 26 <= p2a and p2a <= 30:
            shape = "6"

        # 7
        # 10 < vert < 14
        # 56 < p2a < 64
        elif 10 <= vert and vert <= 14 and 56 <= p2a and p2a <= 64:
            shape = "7"

        # 8
        # 13 < vert < 17
        # 15 < p2a < 19
        elif 13 <= vert and vert <= 17 and 15 <= p2a and p2a <= 19:
            shape = "8"

        # 9
        # 14 < vert < 18
        # 26 < p2a < 34
        elif 14 <= vert and vert <= 18 and 26 <= p2a and p2a <= 34:
            shape = "9"

        # Clubs
        # 18 < vert < 22
        # 26 < p2a < 34
        elif 18 <= vert and vert <= 22 and 26 <= p2a and p2a <= 34:
            shape = "Clubs"

        # Spades
        # 12 < vert < 16
        # 20 < p2a < 28
        elif 12 <= vert and vert <= 16 and 20 <= p2a and p2a <= 28:
            shape = "Spades"

        # Hearts
        # 9 < vert < 13
        # 14 < p2a < 22
        elif 9 <= vert and vert <= 13 and 14 <= p2a and p2a <= 22:
            shape = "Hearts"

        # Diamonds
        # 2 < vert < 6
        # 14 < p2a < 22
        elif 2 <= vert and vert <= 6 and 14 <= p2a and p2a <= 22 and theta >= -55 and theta <= -35:
            shape = "Diamonds" 

        # otherwise, dunno
        else:
            shape = "IDFK"
        
        print('rank/suit:', shape)
        print("")
        return shape

    def approxCont(self, contour):
        # epsilon as a fraction of approximate arc length
        epsilon = 0.01 * cv2.arcLength(contour, True)

        # Ramer-Douglas-Peucker algorithm
        # removes point from contour if deviation less than epsilon
        RDP = cv2.approxPolyDP(contour, epsilon, True)

        return RDP
