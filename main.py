import os
import time
import pygame
import Cards
import linker
from pygame.locals import *

SCREEN_SIZE = (1440, 900)
screen_width, screen_height = SCREEN_SIZE
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Emma färben")

background_image_filename = 'EmmaGame/Images/background.jpg'
iP_pass     = 'EmmaGame/Images/pass.jpg',

#Card Size = 130 * 200 px
#Herz
iP_Herz6   = 'EmmaGame/Images/herz6.png'
iP_Herz7   = 'EmmaGame/Images/herz7.png'
iP_Herz8   = 'EmmaGame/Images/herz8.png'
iP_Herz9   = 'EmmaGame/Images/herz9.png'
iP_Herz10  = 'EmmaGame/Images/herz10.png'
iP_Herz11  = 'EmmaGame/Images/herz11.png'
iP_Herz12  = 'EmmaGame/Images/herz12.png'
iP_Herz13  = 'EmmaGame/Images/herz13.png'
iP_Herz14  = 'EmmaGame/Images/herz14.png'

#Pig
iP_Pig6   = 'EmmaGame/Images/pig6.png'
iP_Pig7   = 'EmmaGame/Images/pig7.png'
iP_Pig8   = 'EmmaGame/Images/pig8.png'
iP_Pig9   = 'EmmaGame/Images/pig9.png'
iP_Pig10  = 'EmmaGame/Images/pig10.png'
iP_Pig11  = 'EmmaGame/Images/pig11.png'
iP_Pig12  = 'EmmaGame/Images/pig12.png'
iP_Pig13  = 'EmmaGame/Images/pig13.png'
iP_Pig14  = 'EmmaGame/Images/pig14.png'

#Kreuz
iP_Kreuz6   = 'EmmaGame/Images/kreuz6.png'
iP_Kreuz7   = 'EmmaGame/Images/kreuz7.png'
iP_Kreuz8   = 'EmmaGame/Images/kreuz8.png'
iP_Kreuz9   = 'EmmaGame/Images/kreuz9.png'
iP_Kreuz10  = 'EmmaGame/Images/kreuz10.png'
iP_Kreuz11  = 'EmmaGame/Images/kreuz11.png'
iP_Kreuz12  = 'EmmaGame/Images/kreuz12.png'
iP_Kreuz13  = 'EmmaGame/Images/kreuz13.png'
iP_Kreuz14  = 'EmmaGame/Images/kreuz14.png'

#Karo
iP_Karo6   = 'EmmaGame/Images/karo6.png'
iP_Karo7   = 'EmmaGame/Images/karo7.png'
iP_Karo8   = 'EmmaGame/Images/karo8.png'
iP_Karo9   = 'EmmaGame/Images/karo9.png'
iP_Karo10  = 'EmmaGame/Images/karo10.png'
iP_Karo11  = 'EmmaGame/Images/karo11.png'
iP_Karo12  = 'EmmaGame/Images/karo12.png'
iP_Karo13  = 'EmmaGame/Images/karo13.png'
iP_Karo14  = 'EmmaGame/Images/karo14.png'


#convert to images
#Herz
P_Herz6     = pygame.image.load(iP_Herz6).convert()
P_Herz7     = pygame.image.load(iP_Herz7).convert()
P_Herz8     = pygame.image.load(iP_Herz8).convert()
P_Herz9     = pygame.image.load(iP_Herz9).convert()
P_Herz10    = pygame.image.load(iP_Herz10).convert()
P_Herz11    = pygame.image.load(iP_Herz11).convert()
P_Herz12    = pygame.image.load(iP_Herz12).convert()
P_Herz13    = pygame.image.load(iP_Herz13).convert()
P_Herz14    = pygame.image.load(iP_Herz14).convert()

#Pig
P_Pig6     = pygame.image.load(iP_Pig6).convert()
P_Pig7     = pygame.image.load(iP_Pig7).convert()
P_Pig8     = pygame.image.load(iP_Pig8).convert()
P_Pig9     = pygame.image.load(iP_Pig9).convert()
P_Pig10    = pygame.image.load(iP_Pig10).convert()
P_Pig11    = pygame.image.load(iP_Pig11).convert()
P_Pig12    = pygame.image.load(iP_Pig12).convert()
P_Pig13    = pygame.image.load(iP_Pig13).convert()
P_Pig14    = pygame.image.load(iP_Pig14).convert()

#Kreuz
P_Kreuz6     = pygame.image.load(iP_Kreuz6).convert()
P_Kreuz7     = pygame.image.load(iP_Kreuz7).convert()
P_Kreuz8     = pygame.image.load(iP_Kreuz8).convert()
P_Kreuz9     = pygame.image.load(iP_Kreuz9).convert()
P_Kreuz10    = pygame.image.load(iP_Kreuz10).convert()
P_Kreuz11    = pygame.image.load(iP_Kreuz11).convert()
P_Kreuz12    = pygame.image.load(iP_Kreuz12).convert()
P_Kreuz13    = pygame.image.load(iP_Kreuz13).convert()
P_Kreuz14    = pygame.image.load(iP_Kreuz14).convert()

#Karo
P_Karo6     = pygame.image.load(iP_Karo6).convert()
P_Karo7     = pygame.image.load(iP_Karo7).convert()
P_Karo8     = pygame.image.load(iP_Karo8).convert()
P_Karo9     = pygame.image.load(iP_Karo9).convert()
P_Karo10    = pygame.image.load(iP_Karo10).convert()
P_Karo11    = pygame.image.load(iP_Karo11).convert()
P_Karo12    = pygame.image.load(iP_Karo12).convert()
P_Karo13    = pygame.image.load(iP_Karo13).convert()
P_Karo14    = pygame.image.load(iP_Karo14).convert()

'''
num_of_card     = 36 // Cards.playerCount
p2_num_of_card  = 36 // Cards.playerCount
p3_num_of_card  = 36 // Cards.playerCount
p4_num_of_card  = 36 // Cards.playerCount
start_turn = 1

card_clicked_list    = [0] * 36 // Cards.playerCount
p2_card_clicked_list = [0] * 36 // Cards.playerCount
p3_card_clicked_list = [0] * 36 // Cards.playerCount
p4_card_clicked_list = [0] * 36 // Cards.playerCount

org_player_card_x = SCREEN_SIZE[0]//2-4*P_Herz6.get_width()
player_card_x     = SCREEN_SIZE[0]//2-4*P_Herz6.get_width()
player_card_y     = 500
org_p2_card_y = 50 + P_Herz6.get_height()
p2_card_x     = SCREEN_SIZE[0]-5*P_Herz6.get_width()//2-10
p2_card_y     = 50 + P_Herz6.get_height()
org_p3_card_x = SCREEN_SIZE[0]//2-4*P_Herz6.get_width()
p3_card_x     = SCREEN_SIZE[0]//2-4*P_Herz6.get_width()
p3_card_y     = 50
org_p4_card_y = 50 + P_Herz6.get_height() 
p4_card_x     = P_Herz6.get_width()
p4_card_y     = 50 + P_Herz6.get_height()
org_display_card_x = SCREEN_SIZE[0]//2 - P_Herz6.get_width()//2
display_card_x     = SCREEN_SIZE[0]//2 - P_Herz6.get_width()//2
display_card_y     = 280
'''

def fill_background():
    '''
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))
    '''
    screen.blit(background, (0,0))




def displayCard():
    screen.blit(P_Herz6, (50,50))

background = pygame.image.load(background_image_filename).convert()
background = pygame.transform.scale(background, SCREEN_SIZE)

fill_background()
pygame.display.update()
displayCard()
pygame.display.update()
time.sleep(10)



def displayCard():
    screen.blit(P_Herz6, (250,50))
    screen.blit(P_Herz7, (180,50))
    return

def main():

    pass


if __name__ == "__main__":
    main()



