import os
from re import X
import time
from turtle import done, screensize
from xml.etree.ElementInclude import include
import pygame
from pygame.event import *
from Cards import *
import easygui
from pygame.locals import *

#def sizes
SCREEN_SIZE = (1600, 900)
cardSize = (130, 200)


#init pygame
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Emma färben")
clock = pygame.time.Clock()

#init game variables
playerList = []
actRoundCards = []
aktuellerSpieler = 0
firstMove = 1

#region image-linking

background_image_filename = 'Images/background.jpg'

#Herz
iP_Herz6   = 'Images/herz6.png'
iP_Herz7   = 'Images/herz7.png'
iP_Herz8   = 'Images/herz8.png'
iP_Herz9   = 'Images/herz9.png'
iP_Herz10  = 'Images/herz10.png'
iP_Herz11  = 'Images/herz11.png'
iP_Herz12  = 'Images/herz12.png'
iP_Herz13  = 'Images/herz13.png'
iP_Herz14  = 'Images/herz14.png'

#Pig
iP_Pig6   = 'Images/pig6.png'
iP_Pig7   = 'Images/pig7.png'
iP_Pig8   = 'Images/pig8.png'
iP_Pig9   = 'Images/pig9.png'
iP_Pig10  = 'Images/pig10.png'
iP_Pig11  = 'Images/pig11.png'
iP_Pig12  = 'Images/pig12.png'
iP_Pig13  = 'Images/pig13.png'
iP_Pig14  = 'Images/pig14.png'

#Kreuz
iP_Kreuz6   = 'Images/kreuz6.png'
iP_Kreuz7   = 'Images/kreuz7.png'
iP_Kreuz8   = 'Images/kreuz8.png'
iP_Kreuz9   = 'Images/kreuz9.png'
iP_Kreuz10  = 'Images/kreuz10.png'
iP_Kreuz11  = 'Images/kreuz11.png'
iP_Kreuz12  = 'Images/kreuz12.png'
iP_Kreuz13  = 'Images/kreuz13.png'
iP_Kreuz14  = 'Images/kreuz14.png'

#Karo
iP_Karo6   = 'Images/karo6.png'
iP_Karo7   = 'Images/karo7.png'
iP_Karo8   = 'Images/karo8.png'
iP_Karo9   = 'Images/karo9.png'
iP_Karo10  = 'Images/karo10.png'
iP_Karo11  = 'Images/karo11.png'
iP_Karo12  = 'Images/karo12.png'
iP_Karo13  = 'Images/karo13.png'
iP_Karo14  = 'Images/karo14.png'


#convert to images

background = pygame.image.load(background_image_filename).convert_alpha()
background = pygame.transform.scale(background, SCREEN_SIZE)

#Herz
P_Herz6     = pygame.image.load(iP_Herz6).convert_alpha()
P_Herz7     = pygame.image.load(iP_Herz7).convert_alpha()
P_Herz8     = pygame.image.load(iP_Herz8).convert_alpha()
P_Herz9     = pygame.image.load(iP_Herz9).convert_alpha()
P_Herz10    = pygame.image.load(iP_Herz10).convert_alpha()
P_Herz11    = pygame.image.load(iP_Herz11).convert_alpha()
P_Herz12    = pygame.image.load(iP_Herz12).convert_alpha()
P_Herz13    = pygame.image.load(iP_Herz13).convert_alpha()
P_Herz14    = pygame.image.load(iP_Herz14).convert_alpha()

#Pig
P_Pig6     = pygame.image.load(iP_Pig6).convert_alpha()
P_Pig7     = pygame.image.load(iP_Pig7).convert_alpha()
P_Pig8     = pygame.image.load(iP_Pig8).convert_alpha()
P_Pig9     = pygame.image.load(iP_Pig9).convert_alpha()
P_Pig10    = pygame.image.load(iP_Pig10).convert_alpha()
P_Pig11    = pygame.image.load(iP_Pig11).convert_alpha()
P_Pig12    = pygame.image.load(iP_Pig12).convert_alpha()
P_Pig13    = pygame.image.load(iP_Pig13).convert_alpha()
P_Pig14    = pygame.image.load(iP_Pig14).convert_alpha()

#Kreuz
P_Kreuz6     = pygame.image.load(iP_Kreuz6).convert_alpha()
P_Kreuz7     = pygame.image.load(iP_Kreuz7).convert_alpha()
P_Kreuz8     = pygame.image.load(iP_Kreuz8).convert_alpha()
P_Kreuz9     = pygame.image.load(iP_Kreuz9).convert_alpha()
P_Kreuz10    = pygame.image.load(iP_Kreuz10).convert_alpha()
P_Kreuz11    = pygame.image.load(iP_Kreuz11).convert_alpha()
P_Kreuz12    = pygame.image.load(iP_Kreuz12).convert_alpha()
P_Kreuz13    = pygame.image.load(iP_Kreuz13).convert_alpha()
P_Kreuz14    = pygame.image.load(iP_Kreuz14).convert_alpha()

#Karo
P_Karo6     = pygame.image.load(iP_Karo6).convert_alpha()
P_Karo7     = pygame.image.load(iP_Karo7).convert_alpha()
P_Karo8     = pygame.image.load(iP_Karo8).convert_alpha()
P_Karo9     = pygame.image.load(iP_Karo9).convert_alpha()
P_Karo10    = pygame.image.load(iP_Karo10).convert_alpha()
P_Karo11    = pygame.image.load(iP_Karo11).convert_alpha()
P_Karo12    = pygame.image.load(iP_Karo12).convert_alpha()
P_Karo13    = pygame.image.load(iP_Karo13).convert_alpha()
P_Karo14    = pygame.image.load(iP_Karo14).convert_alpha()

#endregion

def initPlayers(newGame = 1):
    global aktuellerSpieler
    global firstMove
    firstMove = 1
    d = Deck()
    for i in range(0,4):
        if(newGame): playerList.append(Player(("P"+str(i)), i))
        playerList[i].drawCard(d)
        aktuellerSpieler = getStartingPlayer()

def getStartingPlayer():
    for p in playerList:
        for c in p.hand:
            if c.farbe == "Kreuz" and c.zahl == 7:
                return p.number

def nextPlayer(i = None):
    global aktuellerSpieler
    if(i == None):
        aktuellerSpieler += 1
        if(aktuellerSpieler > 3): 
            aktuellerSpieler = 0
    else: 
        aktuellerSpieler = i
    return

def drawBoard():
    screen.blit(background, (0,0))
    draw_Cards(playerList[0])
    draw_Cards(playerList[1])
    draw_Cards(playerList[2])
    draw_Cards(playerList[3])
    draw_CurrentPlayer()
    draw_Scores()
    pygame.display.update()

def draw_Scores():
    #Player1
        x = SCREEN_SIZE[0] - 100
        y = SCREEN_SIZE[1] - cardSize[1] + 40
        textsurface = myfont.render(str(playerList[0].score + playerList[0].roundScore), False, (0, 0, 0))
        screen.blit(textsurface,(x,y))
    #Player2
        x = SCREEN_SIZE[0] - 100
        y = 60
        textsurface = myfont.render(str(playerList[1].score + playerList[1].roundScore), False, (0, 0, 0))
        screen.blit(textsurface,(x,y))

    #Player3
        x = SCREEN_SIZE[0] - 100
        y = cardSize[1] + 50
        textsurface = myfont.render(str(playerList[2].score + playerList[2].roundScore), False, (0, 0, 0))
        screen.blit(textsurface,(x,y))

    #Player4
        x = SCREEN_SIZE[0] - 100
        y = cardSize[1] + cardSize[1] + 50
        textsurface = myfont.render(str(playerList[3].score + playerList[3].roundScore), False, (0, 0, 0))
        screen.blit(textsurface,(x,y))

def draw_CurrentPlayer():
    if(aktuellerSpieler == 0):
        x = 50
        y = SCREEN_SIZE[1] - cardSize[1] + 40
    if(aktuellerSpieler == 1):
        x = 50
        y = 60
    if(aktuellerSpieler == 2):
        x = 50
        y = cardSize[1] + 50
    if(aktuellerSpieler == 3):
        x = 50
        y = cardSize[1] + cardSize[1] + 50

    rectangle = pygame.Rect(x, y, 100, 100)
    pygame.draw.rect(screen, [0, 255, 0], rectangle)

def getImage(karte):
    x = karte.getID()
    if(x[0] == "Herz"):
        if(x[1] == 6): return P_Herz6
        if(x[1] == 7): return P_Herz7
        if(x[1] == 8): return P_Herz8
        if(x[1] == 9): return P_Herz9
        if(x[1] == 10): return P_Herz10
        if(x[1] == 11): return P_Herz11
        if(x[1] == 12): return P_Herz12
        if(x[1] == 13): return P_Herz13
        if(x[1] == 14): return P_Herz14
        
    elif(x[0] == "Karo"):
        if(x[1] == 6): return P_Karo6
        if(x[1] == 7): return P_Karo7
        if(x[1] == 8): return P_Karo8
        if(x[1] == 9): return P_Karo9
        if(x[1] == 10): return P_Karo10
        if(x[1] == 11): return P_Karo11
        if(x[1] == 12): return P_Karo12
        if(x[1] == 13): return P_Karo13
        if(x[1] == 14): return P_Karo14

    elif(x[0] == "Pig"):
        if(x[1] == 6): return P_Pig6
        if(x[1] == 7): return P_Pig7
        if(x[1] == 8): return P_Pig8
        if(x[1] == 9): return P_Pig9
        if(x[1] == 10): return P_Pig10
        if(x[1] == 11): return P_Pig11
        if(x[1] == 12): return P_Pig12
        if(x[1] == 13): return P_Pig13
        if(x[1] == 14): return P_Pig14

    elif(x[0] == "Kreuz"):
        if(x[1] == 6): return P_Kreuz6
        if(x[1] == 7): return P_Kreuz7
        if(x[1] == 8): return P_Kreuz8
        if(x[1] == 9): return P_Kreuz9
        if(x[1] == 10): return P_Kreuz10
        if(x[1] == 11): return P_Kreuz11
        if(x[1] == 12): return P_Kreuz12
        if(x[1] == 13): return P_Kreuz13
        if(x[1] == 14): return P_Kreuz14

def draw_Cards(spieler):
    if(spieler.number == 0):
        x_start = SCREEN_SIZE[0]/2 - ((len(spieler.hand) / 2) * cardSize[0])
        y_start = SCREEN_SIZE[1] - cardSize[1] - 30
        spieler.handRects.clear()
    if(spieler.number == 1):
        x_start = SCREEN_SIZE[0]/2 - ((len(spieler.hand) / 2) * cardSize[0])
        y_start = 10
        spieler.handRects.clear()
    if(spieler.number == 2):
        x_start = SCREEN_SIZE[0]/2 - ((len(spieler.hand) / 2) * cardSize[0])
        y_start = cardSize[1] + 10
        spieler.handRects.clear()
    if(spieler.number == 3):
        x_start = SCREEN_SIZE[0]/2 - ((len(spieler.hand) / 2) * cardSize[0])
        y_start = cardSize[1] + cardSize[1] + 10
        spieler.handRects.clear()

    for i in spieler.hand:
        z = getImage(i)
        spieler.handRects.append(z.get_rect(topleft=(x_start, y_start)))
        screen.blit(z, (x_start, y_start))
        x_start = x_start + cardSize[0]
    
    return

def removeCard(x,y):
    global firstMove
    for p in playerList:
        for index, box in enumerate(p.handRects):
            if box.collidepoint(x,y):
                if(p.number == aktuellerSpieler):
                        if(checkIfValidCard(p.hand, index)):
                            firstMove = 0
                            nextPlayer()
                            return p.hand.pop(index)
    return 0
                    
def checkIfValidCard(pHand, i):
    global firstMove
    cnt = 0
    if(firstMove):
        if pHand[i].farbe == "Kreuz" and pHand[i].zahl == 7: return True

    else:
        if(len(actRoundCards) == 0): return 1

        for c in pHand:
            if(c.farbe == actRoundCards[0].farbe):
                cnt += 1
        if(cnt == 0): 
            return 1
        else:
            if(pHand[i].farbe == actRoundCards[0].farbe):
                return 1
            else:
                return 0



def calcScore():
    for p in playerList:
        p.roundScore = 0
        tempScore = 0
        cnt = 0
        for c in p.stapel:
            tempScore += c.wert
            cnt += 1

        #Regel: Bei allen Stichen werden -90 Punkte gezählt
        if(cnt == 36):
            tempScore = -90
        
        #Regel: Bei 0 Stichen wird -5 genommen
        if(cnt == 0):
            tempScore -= 5

        p.roundScore += tempScore
        p.score += p.roundScore

        if(p.score < 0):
             p.score = 0

def printAndResetRoundScores():
    for p in playerList:
        print("Player {} hat {} Punkte diese Runder erzielt. Gesamt: {} Punkte".format(p.number, p.roundScore, p.score))
        p.roundScore = 0

def checkForRoundWinner():
    winner = actRoundCards[0]

    for i in actRoundCards:
        if(i.farbe == winner.farbe):
            if(i.zahl > winner.zahl):
                winner = i
    for p in playerList:
        if p.number == winner.owner:
            for c in actRoundCards:
                c.owner = winner.owner
                p.stapel.append(c)
                p.roundScore += c.wert
        
    actRoundCards.clear()
    nextPlayer(winner.owner)
    
    cnt = 0
    for p in playerList:
        if len(p.hand) == 0: cnt += 1
    
    drawBoard()

    if cnt == 4: 
        calcScore()
        printAndResetRoundScores()
        return -1
    
    drawBoard()
    return winner.owner

def askForNewGame():
    return easygui.ynbox('Shall I continue?', 'Title', ('Yes', 'No'))

def restartGame():
    initPlayers(0)
    drawBoard()

def main():
    initPlayers(1)     
    drawBoard()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Close your program if the user wants to quit.
                raise SystemExit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if event.button == 1:
                    c = removeCard(x,y)
                    if(c != 0):
                        actRoundCards.append(c)
                        if(len(actRoundCards) == 4):
                            if(checkForRoundWinner() == -1):
                                if(askForNewGame()):
                                    restartGame()
                    
        drawBoard()
        clock.tick(60)
    return

if __name__ == "__main__":
    main()

