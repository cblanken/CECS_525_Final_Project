'''
# Written by: Cameron Blankenbuehler
# Course: CECS 525 Team 8 Spring 2018 Final Project
# Title: War Game
#
#
'''

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
    def __init__(self, suit, rank, img=None):
        self.suit = suit
        self.rank = rank
        self.img = img

    def __str__(self):
        return "Suit: " + str(self.suit) + "\nRank: " + str(self.rank)


class Deck():
    def __init__(self):
        suit_names = ['clubs', 'diamonds', 'hearts', 'spades']

        # Clubs
        two_clubs = Card(Suit.clubs, Rank.two)
        three_clubs = Card(Suit.clubs, Rank.three)
        four_clubs = Card(Suit.clubs, Rank.four)
        five_clubs = Card(Suit.clubs, Rank.five)
        six_clubs = Card(Suit.clubs, Rank.six)
        seven_clubs = Card(Suit.clubs, Rank.seven)
        eight_clubs = Card(Suit.clubs, Rank.eight)
        nine_clubs = Card(Suit.clubs, Rank.nine)
        ten_clubs = Card(Suit.clubs, Rank.ten)
        jack_clubs = Card(Suit.clubs, Rank.jack)
        queen_clubs = Card(Suit.clubs, Rank.queen)
        king_clubs = Card(Suit.clubs, Rank.king)
        ace_clubs = Card(Suit.clubs, Rank.ace)

        # Diamonds
        two_diamonds = Card(Suit.diamonds, Rank.two)
        three_diamonds = Card(Suit.diamonds, Rank.three)
        four_diamonds = Card(Suit.diamonds, Rank.four)
        five_diamonds = Card(Suit.diamonds, Rank.five)
        six_diamonds = Card(Suit.diamonds, Rank.six)
        seven_diamonds = Card(Suit.diamonds, Rank.seven)
        eight_diamonds = Card(Suit.diamonds, Rank.eight)
        nine_diamonds = Card(Suit.diamonds, Rank.nine)
        ten_diamonds = Card(Suit.diamonds, Rank.ten)
        jack_diamonds = Card(Suit.diamonds, Rank.jack)
        queen_diamonds = Card(Suit.diamonds, Rank.queen)
        king_diamonds = Card(Suit.diamonds, Rank.king)
        ace_diamonds = Card(Suit.diamonds, Rank.ace)

        # Hearts
        two_hearts = Card(Suit.hearts, Rank.two)
        three_hearts = Card(Suit.hearts, Rank.three)
        four_hearts = Card(Suit.hearts, Rank.four)
        five_hearts = Card(Suit.hearts, Rank.five)
        six_hearts = Card(Suit.hearts, Rank.six)
        seven_hearts = Card(Suit.hearts, Rank.seven)
        eight_hearts = Card(Suit.hearts, Rank.eight)
        nine_hearts = Card(Suit.hearts, Rank.nine)
        ten_hearts = Card(Suit.hearts, Rank.ten)
        jack_hearts = Card(Suit.hearts, Rank.jack)
        queen_hearts = Card(Suit.hearts, Rank.queen)
        king_hearts = Card(Suit.hearts, Rank.king)
        ace_hearts = Card(Suit.hearts, Rank.ace)

        # Spades
        two_spades = Card(Suit.spades, Rank.two)
        three_spades = Card(Suit.spades, Rank.three)
        four_spades = Card(Suit.spades, Rank.four)
        five_spades = Card(Suit.spades, Rank.five)
        six_spades = Card(Suit.spades, Rank.six)
        seven_spades = Card(Suit.spades, Rank.seven)
        eight_spades = Card(Suit.spades, Rank.eight)
        nine_spades = Card(Suit.spades, Rank.nine)
        ten_spades = Card(Suit.spades, Rank.ten)
        jack_spades = Card(Suit.spades, Rank.jack)
        queen_spades = Card(Suit.spades, Rank.queen)
        king_spades = Card(Suit.spades, Rank.king)
        ace_spades = Card(Suit.spades, Rank.ace)


### END Card Deck Stuff



### GUI Stuff
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
        WarDeck = Deck()



class MainApplication:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.statusbar = Statusbar(master)
        self.main = Main(master)

        self.statusbar.frame.pack(side="bottom", fill="x")
        self.main.frame.pack(side="right", fill="both", expand=True)

### END GUI Stuff

def main():
    root = tk.Tk()
    mainApp = MainApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
