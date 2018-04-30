'''
# Written by: Cameron Blankenbuehler
# Course: CECS 525 Team 8 Spring 2018 Final Project
# Title: War Game
# Description:
#
'''

import os as os
import tkinter as tk
import time as time
# import RPi.GPIO as GPIO

from tkinter import ttk
from enum import Enum

#
# from picamera import PiCamera
#
# camera = PiCamera()
# camera.resolution = (1024, 768)
# # camera.start_preview()
# # Camera warm-up time
# time.sleep(2)
# camera.capture('foo{}.jpg'.format, 1)


### Card Deck Stuff
class Suit(Enum):
    # Card suits
    clubs = 1
    diamonds = 2
    hearts = 3
    spades = 4


class Rank(Enum):
    # Card ranks
    ace = 14
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13


class Card:
    def __init__(self, suit_name, suit_value, rank_name, rank_value):
        self.suit_name = suit_name
        self.suit_value = suit_value
        self.rank_name = rank_name
        self.rank_value = rank_value
        self.rank_suit = self.rank_name + "_" + self.suit_name
        self.img_path = os.path.normpath("Image Recognition Stuff/Cards Vector Files/" + rank_name + "_" + suit_name + ".png")

    # def __str__():
    #     return "Suit: " + str(self.suit_name) + "\nRank: " + str(self.rank_name)


class Deck:
    def __init__(self):
        # Clubs
        self.two_clubs = Card(Suit.clubs.name, Suit.clubs.value, Rank.two.name, Rank.two.value)
        self.three_clubs = Card(Suit.clubs.name, Suit.clubs.value, Rank.three.name, Rank.three.value)
        self.four_clubs = Card(Suit.clubs.name, Suit.clubs.value, Rank.four.name, Rank.four.value)
        self.five_clubs = Card(Suit.clubs.name, Suit.clubs.value, Rank.five.name, Rank.five.value)
        self.six_clubs = Card(Suit.clubs.name, Suit.clubs.value, Rank.six.name, Rank.six.value)
        self.seven_clubs = Card(Suit.clubs.name, Suit.clubs.value, Rank.seven.name, Rank.seven.value)
        self.eight_clubs = Card(Suit.clubs.name, Suit.clubs.value, Rank.eight.name, Rank.eight.value)
        self.nine_clubs = Card(Suit.clubs.name, Suit.clubs.value, Rank.nine.name, Rank.nine.value)
        self.ten_clubs = Card(Suit.clubs.name, Suit.clubs.value, Rank.ten.name, Rank.ten.value)
        self.jack_clubs = Card(Suit.clubs.name, Suit.clubs.value, Rank.jack.name, Rank.jack.value)
        self.queen_clubs = Card(Suit.clubs.name, Suit.clubs.value, Rank.queen.name, Rank.queen.value)
        self.king_clubs = Card(Suit.clubs.name, Suit.clubs.value, Rank.king.name, Rank.king.value)
        self.ace_clubs = Card(Suit.clubs.name, Suit.clubs.value, Rank.ace.name, Rank.ace.value)

        # Diamonds
        self.two_diamonds = Card(Suit.diamonds.name, Suit.diamonds.value, Rank.two.name, Rank.two.value)
        self.three_diamonds = Card(Suit.diamonds.name, Suit.diamonds.value, Rank.three.name, Rank.three.value)
        self.four_diamonds = Card(Suit.diamonds.name, Suit.diamonds.value, Rank.four.name, Rank.four.value)
        self.five_diamonds = Card(Suit.diamonds.name, Suit.diamonds.value, Rank.five.name, Rank.five.value)
        self.six_diamonds = Card(Suit.diamonds.name, Suit.diamonds.value, Rank.six.name, Rank.six.value)
        self.seven_diamonds = Card(Suit.diamonds.name, Suit.diamonds.value, Rank.seven.name, Rank.seven.value)
        self.eight_diamonds = Card(Suit.diamonds.name, Suit.diamonds.value, Rank.eight.name, Rank.eight.value)
        self.nine_diamonds = Card(Suit.diamonds.name, Suit.diamonds.value, Rank.nine.name, Rank.nine.value)
        self.ten_diamonds = Card(Suit.diamonds.name, Suit.diamonds.value, Rank.ten.name, Rank.ten.value)
        self.jack_diamonds = Card(Suit.diamonds.name, Suit.diamonds.value, Rank.jack.name, Rank.jack.value)
        self.queen_diamonds = Card(Suit.diamonds.name, Suit.diamonds.value, Rank.queen.name, Rank.queen.value)
        self.king_diamonds = Card(Suit.diamonds.name, Suit.diamonds.value, Rank.king.name, Rank.king.value)
        self.ace_diamonds = Card(Suit.diamonds.name, Suit.diamonds.value, Rank.ace.name, Rank.ace.value)

        # Hearts
        self.two_hearts = Card(Suit.hearts.name, Suit.hearts.value, Rank.two.name, Rank.two.value)
        self.three_hearts = Card(Suit.hearts.name, Suit.hearts.value, Rank.three.name, Rank.three.value)
        self.four_hearts = Card(Suit.hearts.name, Suit.hearts.value, Rank.four.name, Rank.four.value)
        self.five_hearts = Card(Suit.hearts.name, Suit.hearts.value, Rank.five.name, Rank.five.value)
        self.six_hearts = Card(Suit.hearts.name, Suit.hearts.value, Rank.six.name, Rank.six.value)
        self.seven_hearts = Card(Suit.hearts.name, Suit.hearts.value, Rank.seven.name, Rank.seven.value)
        self.eight_hearts = Card(Suit.hearts.name, Suit.hearts.value, Rank.eight.name, Rank.eight.value)
        self.nine_hearts = Card(Suit.hearts.name, Suit.hearts.value, Rank.nine.name, Rank.nine.value)
        self.ten_hearts = Card(Suit.hearts.name, Suit.hearts.value, Rank.ten.name, Rank.ten.value)
        self.jack_hearts = Card(Suit.hearts.name, Suit.hearts.value, Rank.jack.name, Rank.jack.value)
        self.queen_hearts = Card(Suit.hearts.name, Suit.hearts.value, Rank.queen.name, Rank.queen.value)
        self.king_hearts = Card(Suit.hearts.name, Suit.hearts.value, Rank.king.name, Rank.king.value)
        self.ace_hearts = Card(Suit.hearts.name, Suit.hearts.value, Rank.ace.name, Rank.ace.value)

        # Spades
        self.two_spades = Card(Suit.spades.name, Suit.spades.value, Rank.two.name, Rank.two.value)
        self.three_spades = Card(Suit.spades.name, Suit.spades.value, Rank.three.name, Rank.three.value)
        self.four_spades = Card(Suit.spades.name, Suit.spades.value, Rank.four.name, Rank.four.value)
        self.five_spades = Card(Suit.spades.name, Suit.spades.value, Rank.five.name, Rank.five.value)
        self.six_spades = Card(Suit.spades.name, Suit.spades.value, Rank.six.name, Rank.six.value)
        self.seven_spades = Card(Suit.spades.name, Suit.spades.value, Rank.seven.name, Rank.seven.value)
        self.eight_spades = Card(Suit.spades.name, Suit.spades.value, Rank.eight.name, Rank.eight.value)
        self.nine_spades = Card(Suit.spades.name, Suit.spades.value, Rank.nine.name, Rank.nine.value)
        self.ten_spades = Card(Suit.spades.name, Suit.spades.value, Rank.ten.name, Rank.ten.value)
        self.jack_spades = Card(Suit.spades.name, Suit.spades.value, Rank.jack.name, Rank.jack.value)
        self.queen_spades = Card(Suit.spades.name, Suit.spades.value, Rank.queen.name, Rank.queen.value)
        self.king_spades = Card(Suit.spades.name, Suit.spades.value, Rank.king.name, Rank.king.value)
        self.ace_spades = Card(Suit.spades.name, Suit.spades.value, Rank.ace.name, Rank.ace.value)

class Hand(Deck):
    def __init__(self, *args):
        self.hand = []
        for arg in args:
            hand.append(arg)

### END Card Deck Stuff

class WarGame:
    def __init__(self):
        self.round_cnt = 0
        self.deck = Deck()
        self.player1_hand = Hand()
        self.player2_hand = Hand()
        self.player1_on_table = [self.deck.ace_spades]
        self.player2_on_table = [self.deck.ace_hearts]

    def getCardsPlayed(self):
        # Receive cards names/values form
        self.player1_on_table[0] = getattr(self.deck, "four_hearts")
        self.player2_on_table[0] = getattr(self.deck, "seven_clubs")


    def playRound(self):
        self.getCardsPlayed()
        self.round_cnt += 1
        # Compare card rank then suit if necessary
        # return the winner
        if self.player1_on_table[0].rank_value > self.player2_on_table[0].rank_value:
            return "player1"
        elif self.player1_on_table[0].rank_value == self.player2_on_table[0].rank_value:
            if(self.player1_on_table[0].suit_value > self.player2_on_table[0].suit_value):
                return "player1"
            else:
                return "player2"
        else:
            return "player2"



### GUI Stuff
class CardDisplay:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.left_frame = tk.Frame(self.frame, bg='black')
        self.right_frame = tk.Frame(self.frame, bg='black')

        # Left (player1) card display
        self.player1_current_path = os.path.normpath("Image Recognition Stuff/Cards Vector Files/ace_clubs.png")
        self.player1_card_image = self.imgDownscale(tk.PhotoImage(file=self.player1_current_path))
        self.divider = ttk.Separator(self.left_frame, orient=tk.VERTICAL).pack(side="left", fill="y", expand=True)
        self.player1_card_lbl = tk.Label(self.left_frame, image=self.player1_card_image, borderwidth=20, bg='black')
        # Make reference for image to avoid garbage collection
        self.player1_card_lbl.image = self.player1_card_image
        self.player1_card_lbl.pack(side=tk.LEFT)
        self.left_frame.pack(side=tk.LEFT, fill="y", expand=True)

        # Right (player2) card display
        self.player2_current_path = os.path.normpath("Image Recognition Stuff/Cards Vector Files/ace_spades.png")
        self.player2_card_image = self.imgDownscale(tk.PhotoImage(file=self.player2_current_path))
        self.divider = ttk.Separator(self.left_frame, orient=tk.VERTICAL).pack(side="left", fill="y", expand=True)
        self.player2_card_lbl = tk.Label(self.left_frame, image=self.player2_card_image, borderwidth=20, bg='black')
        # Make reference for image to avoid garbage collection
        self.player2_card_lbl.image = self.player2_card_image
        self.player2_card_lbl.pack(side=tk.RIGHT)
        self.right_frame.pack(side=tk.RIGHT, fill="y", expand=True)

    def imgDownscale(self, img):
        return img.zoom(1).subsample(13)

    def updateDisplay(self, player1_card_name, player2_card_name):
        # Player1 card display update
        self.player1_current_path = os.path.normpath("Image Recognition Stuff/Cards Vector Files/" + player1_card_name + ".png")
        self.player1_card_image = self.imgDownscale(tk.PhotoImage(file=self.player1_current_path))
        self.player1_card_lbl.config(image=self.player1_card_image)
        # Player2 card display update
        self.player2_current_path = os.path.normpath("Image Recognition Stuff/Cards Vector Files/" + player2_card_name + ".png")
        self.player2_card_image = self.imgDownscale(tk.PhotoImage(file=self.player2_current_path))
        self.player2_card_lbl.config(image=self.player2_card_image)


class Statusbar:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.divider = ttk.Separator(self.frame, orient=tk.HORIZONTAL).pack(side="top", fill="x", expand=True)
        self.start_btn = tk.Button(self.frame, text="START", font=("Cambria Bold", 11))
        self.start_btn.pack(side="left", padx=3, pady=3)

class Main:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.frame.width = 50

        self.deck = Deck()

        self.test_lbl = tk.Label(self.frame, text=self.deck.ace_clubs.suit_name, font=("Cambria Bold", 16))
        self.test_lbl.pack()

class MainApplication:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title("War Game")
        self.master.geometry('1200x700')

        self.statusbar = Statusbar(master)
        self.main = Main(master)
        self.carddisplay = CardDisplay(master)

        self.statusbar.frame.pack(side="bottom", fill="x")
        self.main.frame.pack(side="left", fill="both", expand=True)
        self.carddisplay.frame.pack(side="right", fill="both", expand=False)

        self.wargame = WarGame()

        def playRound():
            self.wargame.playRound()
            self.carddisplay.updateDisplay(self.wargame.player1_on_table[0].rank_suit, self.wargame.player2_on_table[0].rank_suit)

        # self.winner = self.wargame.playRound()
        # self.carddisplay.updateDisplay(self.wargame.player1_on_table[0].rank_suit, self.wargame.player2_on_table[0].rank_suit)

        '''
        ### GPIO Setup
        GPIO.setmode(GPIO.BCM)
        # pin 23 -> playRound button
        GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # interrupt button callback
        GPIO.add_event_detect(23, GPIO.FALLING, callback=self.playRound, bouncetime=300)
        '''



        # self.carddisplay.updateDisplay("three_spades", "eight_hearts")


### END GUI Stuff

def main():
    root = tk.Tk()
    mainApp = MainApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
