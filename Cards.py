import random
from pygame import sprite

playerCount = 4

class Card(object):
    def __init__(self, farbe, zahl, wert):
        self.farbe = farbe
        self.zahl = zahl
        self.wert = wert
        self.owner = None

    def getID(self):
        return (self.farbe, self.zahl, self.owner)

    def show(self):
        print ("{} {} \t\t {}".format(self.farbe, self.zahl, self.wert))

class Deck(object):
    def __init__(self):
        self.karten = []
        self.build()

    def build(self):
        for s in ["Herz", "Kreuz", "Pig", "Karo"]:
            for i in [6,7,8,9,10,11,12,13,14]:
                self.karten.append(Card(s, i, 0))
        self.assignValues()
        self.shuffle()

    def assignValues(self):
        for c in self.karten:
            #Herzen = Wert 5
            if(c.farbe == "Herz"):
                c.wert = 5

                #Herz Ass = Wert 20
                if(c.zahl == 14):
                    c.wert = 20
            
            #Pig Dame
            if(c.farbe == "Pig"):
                if(c.zahl == 12):
                    c.wert = 30

    def show(self):
        for c in self.karten:
            c.show()

    def shuffle(self):
        for i in range(len(self.karten)-1, 0, -1):
            r = random.randint(0,i)
            self.karten[i], self.karten[r] = self.karten[r], self.karten[i]

    def getCard(self):
        return self.karten.pop()

class Player(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.hand = []
        self.handRects = []
        self.stapel = []
        self.roundScore = 0
        self.score = 0

    def drawCard(self, deck):
            for i in range(0, 36 // playerCount):
                self.hand.append(deck.getCard())
            
            for c in self.hand:
                c.owner = self.number

    def showHandConsole(self):
        print("{} hat folgende Karten:".format(self.name))
        for c in self.hand:
            c.show()
        print("\n")