'''
# Written by: Cameron Blankenbuehler
# Course: CECS 525 Team 8 Spring 2018 Final Project
# Title: War Game
#
#
'''
import os as os
import tkinter as tk
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
    def __init__(self, suit_name, suit_value, rank_name, rank_value, img=None):
        self.suit_name = suit_name
        self.suit_value = suit_value
        self.rank_name = rank_name
        self.rank_value = rank_value
        self.img = img

    def __str__(self):
        return "Suit: " + str(self.suit) + "\nRank: " + str(self.rank)


class Deck:
    def __init__(self):
        # Clubs
        two_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.two.name, Rank.two)
        three_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.three.name, Rank.three)
        four_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.four.name, Rank.four)
        five_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.five.name, Rank.five)
        six_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.six.name, Rank.six)
        seven_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.seven.name, Rank.seven)
        eight_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.eight.name, Rank.eight)
        nine_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.nine.name, Rank.nine)
        ten_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.ten.name, Rank.ten)
        jack_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.jack.name, Rank.jack)
        queen_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.queen.name, Rank.queen)
        king_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.king.name, Rank.king)
        ace_clubs = Card(Suit.clubs.name, Suit.clubs, Rank.ace.name, Rank.ace)

        # Diamonds
        two_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.two.name, Rank.two)
        three_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.three.name, Rank.three)
        four_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.four.name, Rank.four)
        five_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.five.name, Rank.five)
        six_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.six.name, Rank.six)
        seven_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.seven.name, Rank.seven)
        eight_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.eight.name, Rank.eight)
        nine_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.nine.name, Rank.nine)
        ten_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.ten.name, Rank.ten)
        jack_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.jack.name, Rank.jack)
        queen_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.queen.name, Rank.queen)
        king_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.king.name, Rank.king)
        ace_diamonds = Card(Suit.diamonds.name, Suit.diamonds, Rank.ace.name, Rank.ace)

        # Hearts
        two_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.two.name, Rank.two)
        three_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.three.name, Rank.three)
        four_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.four.name, Rank.four)
        five_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.five.name, Rank.five)
        six_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.six.name, Rank.six)
        seven_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.seven.name, Rank.seven)
        eight_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.eight.name, Rank.eight)
        nine_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.nine.name, Rank.nine)
        ten_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.ten.name, Rank.ten)
        jack_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.jack.name, Rank.jack)
        queen_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.queen.name, Rank.queen)
        king_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.king.name, Rank.king)
        ace_hearts = Card(Suit.hearts.name, Suit.hearts, Rank.ace.name, Rank.ace)

        # Spades
        two_spades = Card(Suit.spades.name, Suit.spades, Rank.two.name, Rank.two)
        three_spades = Card(Suit.spades.name, Suit.spades, Rank.three.name, Rank.three)
        four_spades = Card(Suit.spades.name, Suit.spades, Rank.four.name, Rank.four)
        five_spades = Card(Suit.spades.name, Suit.spades, Rank.five.name, Rank.five)
        six_spades = Card(Suit.spades.name, Suit.spades, Rank.six.name, Rank.six)
        seven_spades = Card(Suit.spades.name, Suit.spades, Rank.seven.name, Rank.seven)
        eight_spades = Card(Suit.spades.name, Suit.spades, Rank.eight.name, Rank.eight)
        nine_spades = Card(Suit.spades.name, Suit.spades, Rank.nine.name, Rank.nine)
        ten_spades = Card(Suit.spades.name, Suit.spades, Rank.ten.name, Rank.ten)
        jack_spades = Card(Suit.spades.name, Suit.spades, Rank.jack.name, Rank.jack)
        queen_spades = Card(Suit.spades.name, Suit.spades, Rank.queen.name, Rank.queen)
        king_spades = Card(Suit.spades.name, Suit.spades, Rank.king.name, Rank.king)
        ace_spades = Card(Suit.spades.name, Suit.spades, Rank.ace.name, Rank.ace)

class Hand(Deck):
    def __init__(self, *args):
        self.hand = []
        for arg in args:
            hand.append(arg)


### END Card Deck Stuff



### GUI Stuff
class CardDisplay:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)

        self.current_path = os.path.normpath("Image Recognition Stuff/Cards Vector Files/ace_clubs.png")
        self.card_image = tk.PhotoImage(file=self.current_path)
        self.card_image = self.card_image.zoom(2)
        self.card_image = self.card_image.subsample(24)
        self.card_Lbl = tk.Label(self.frame, image=self.card_image)
        self.card_Lbl.pack(side=tk.RIGHT)

class Statusbar:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)


class Main:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)

        parent.title("War Game")
        parent.geometry('650x450')
        deck = Deck()



class MainApplication:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.statusbar = Statusbar(master)
        self.main = Main(master)
        self.carddisplay = CardDisplay(master)

        self.statusbar.frame.pack(side="bottom", fill="x")
        self.main.frame.pack(side="right", fill="both", expand=True)
        self.carddisplay.frame.pack(side="right", fill="x", expand=False)

### END GUI Stuff

def main():
    root = tk.Tk()
    mainApp = MainApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
