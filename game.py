import random
import sys
import pygame
from pygame.locals import *


FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = '/gallery/sprits/bird.png'
BACKGROUND = '/gallery/sprits/backgroung.png'
PIPE =  '/gallery/sprits/pipe.png'

def welcomeScreen():
    
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['massage'].getwidth())/2)
    messagey = int(SCREENHEIGHT*0.13) 
    basex = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (evemt.type== K_ESCAPE):
                pygame.quit()
                sys.exit()


            elif event.type==KEYDOWN and(event.key=K_Sp)
    pass

if __name__ == "__main__":

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('FLAPPY BIRD BY ANUJA')
    GAME_SPRITES['numbers'] =(
        pygame.image.load('gallery/sprits/0.png').convert_alpha(),
        pygame.image.load('gallery/sprits/1.png').convert_alpha(),
        pygame.image.load('gallery/sprits/2.png').convert_alpha(),
        pygame.image.load('gallery/sprits/3.png').convert_alpha(),
        pygame.image.load('gallery/sprits/4.png').convert_alpha(),
        pygame.image.load('gallery/sprits/5.png').convert_alpha(),
        pygame.image.load('gallery/sprits/6.png').convert_alpha(),
        pygame.image.load('gallery/sprits/7.png').convert_alpha(),
        pygame.image.load('gallery/sprits/8.png').convert_alpha(),
        pygame.image.load('gallery/sprits/9.png').convert_alpha(),
    )

    GAME_SPRITES['massage'] = pygame.image.load('gallery/sprits/welcome.jpg').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('gallery/sprits/base.png').convert_alpha()
    GAME_SPRITES['pipe'] =(
        pygame.image.load('gallery/sprits/pipe.png').convert_alpha(),180,
pygame.image.load(PIPE).convert_alpha())
    
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.mp3')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.mp3')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.mp3')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.mp3')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.mp3')

    
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
        