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

from tkinter import ttk
from enum import Enum


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
        self.img_path = os.path.normpath("Image Recognition Stuff/Cards Vector Files/" + rank_name + "_" + suit_name + ".png")

    # def __str__():
    #     return "Suit: " + str(self.suit_name) + "\nRank: " + str(self.rank_name)


class Deck:
    def __init__(self):
        # Clubs
        self.two_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.two.name, Rank.two)
        self.three_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.three.name, Rank.three)
        self.four_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.four.name, Rank.four)
        self.five_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.five.name, Rank.five)
        self.six_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.six.name, Rank.six)
        self.seven_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.seven.name, Rank.seven)
        self.eight_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.eight.name, Rank.eight)
        self.nine_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.nine.name, Rank.nine)
        self.ten_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.ten.name, Rank.ten)
        self.jack_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.jack.name, Rank.jack)
        self.queen_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.queen.name, Rank.queen)
        self.king_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.king.name, Rank.king)
        self.ace_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.ace.name, Rank.ace)

        # Diamonds
        self.two_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.two.name, Rank.two)
        self.three_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.three.name, Rank.three)
        self.four_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.four.name, Rank.four)
        self.five_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.five.name, Rank.five)
        self.six_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.six.name, Rank.six)
        self.seven_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.seven.name, Rank.seven)
        self.eight_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.eight.name, Rank.eight)
        self.nine_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.nine.name, Rank.nine)
        self.ten_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.ten.name, Rank.ten)
        self.jack_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.jack.name, Rank.jack)
        self.queen_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.queen.name, Rank.queen)
        self.king_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.king.name, Rank.king)
        self.ace_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.ace.name, Rank.ace)

        # Hearts
        self.two_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.two.name, Rank.two)
        self.three_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.three.name, Rank.three)
        self.four_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.four.name, Rank.four)
        self.five_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.five.name, Rank.five)
        self.six_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.six.name, Rank.six)
        self.seven_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.seven.name, Rank.seven)
        self.eight_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.eight.name, Rank.eight)
        self.nine_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.nine.name, Rank.nine)
        self.ten_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.ten.name, Rank.ten)
        self.jack_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.jack.name, Rank.jack)
        self.queen_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.queen.name, Rank.queen)
        self.king_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.king.name, Rank.king)
        self.ace_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.ace.name, Rank.ace)

        # Spades
        self.two_spades = Card(Suit.spades.name, Suit.spades, Rank.two.name, Rank.two)
        self.three_spades = Card(Suit.spades.name, Suit.spades, Rank.three.name, Rank.three)
        self.four_spades = Card(Suit.spades.name, Suit.spades, Rank.four.name, Rank.four)
        self.five_spades = Card(Suit.spades.name, Suit.spades, Rank.five.name, Rank.five)
        self.six_spades = Card(Suit.spades.name, Suit.spades, Rank.six.name, Rank.six)
        self.seven_spades = Card(Suit.spades.name, Suit.spades, Rank.seven.name, Rank.seven)
        self.eight_spades = Card(Suit.spades.name, Suit.spades, Rank.eight.name, Rank.eight)
        self.nine_spades = Card(Suit.spades.name, Suit.spades, Rank.nine.name, Rank.nine)
        self.ten_spades = Card(Suit.spades.name, Suit.spades, Rank.ten.name, Rank.ten)
        self.jack_spades = Card(Suit.spades.name, Suit.spades, Rank.jack.name, Rank.jack)
        self.queen_spades = Card(Suit.spades.name, Suit.spades, Rank.queen.name, Rank.queen)
        self.king_spades = Card(Suit.spades.name, Suit.spades, Rank.king.name, Rank.king)
        self.ace_spades = Card(Suit.spades.name, Suit.spades, Rank.ace.name, Rank.ace)

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
        self.player1_on_table = []
        self.player2_on_table = []

    def getCardsPlayed():
        # Receive cards names/values form
        self.player1_on_table = None
        self.player2_on_table = None


    def playRound():
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
        self.player2_current_path = os.path.normpath("Image Recognition Stuff/Cards Vector Files/two_hearts.png")
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
        self.player1_card_image = imgDownscale(tk.PhotoImage(file=self.player1_current_path))
        self.player1_card_lbl.config(image=self.player1_card_image)
        # Player2 card display update
        self.player2_current_path = os.path.normpath("Image Recognition Stuff/Cards Vector Files/" + player2_card_name + ".png")
        self.player2_card_image = imgDownscale(tk.PhotoImage(file=self.player2_current_path))
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

        # self.carddisplay.updateDisplay("three_spades", "eight_hearts")


### END GUI Stuff

def main():
    root = tk.Tk()
    mainApp = MainApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
