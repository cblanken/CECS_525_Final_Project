'''
# Written by: Cameron Blankenbuehler
# Course: CECS 525 Team 8 Spring 2018 Final Project
# Title: War Game
#
#
'''
import os as os
import tkinter as tk
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

class WarGame:
    def __init__(self):
        self.round_cnt = 0
        self.deck = Deck()
        player1_hand = Hand()
        player2_hand = Hand()
    



### END Card Deck Stuff



### GUI Stuff
class CardDisplay:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent, bg='black')

        self.current_path = os.path.normpath("Image Recognition Stuff/Cards Vector Files/ace_clubs.png")
        self.card_image = tk.PhotoImage(file=self.current_path)
        self.card_image = self.card_image.zoom(2)
        self.card_image = self.card_image.subsample(23)

        self.divider = ttk.Separator(self.frame, orient=tk.VERTICAL).pack(side="left", fill="y", expand=True)
        self.card_Lbl = tk.Label(self.frame, image=self.card_image, borderwidth=20, bg='black')
        # Make reference for image to avoid garbage collection
        self.card_Lbl.image = self.card_image
        self.card_Lbl.pack(side=tk.RIGHT)


    def updateDisplay(new_path):
        self.current_path = new_path
        self.card_Lbl.configure(image=self.card_image)


class Statusbar:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.divider = ttk.Separator(self.frame, orient=tk.HORIZONTAL).pack(side="top", fill="x", expand=True)


class Main:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.frame.width = 50

        self.deck = Deck()

        testLbl = tk.Label(self.frame, text=self.deck.ace_clubs.suit_name, font=("Cambria Bold", 16))
        testLbl.pack()

class MainApplication:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title("War Game")
        self.master.geometry('800x450')

        self.statusbar = Statusbar(master).frame.pack(side="bottom", fill="x")
        self.main = Main(master).frame.pack(side="left", fill="both", expand=True)
        self.carddisplay = CardDisplay(master).frame.pack(side="right", fill="both", expand=False)



### END GUI Stuff

def main():
    root = tk.Tk()
    mainApp = MainApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
