# ------------------------------------------
# Get Card Rank and Suit
# ------------------------------------------

from cardInfo import cardInfo
from Identifier import Identify
import numpy as np
import argparse
import imutils
import cv2

# read image
Image = cv2.imread(r"Test Images\allRanksSuits.png")


# identify card information
card = cardInfo(Image)

print(card)
