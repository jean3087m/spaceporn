#!/bin/bash/python3

#this is the main game python 3 file for spaceporn 
### author: carlos3087
### version: 1.0.1  
#python version: 3.7.x
#developed in 2018

#lib imports
import pygame 
from pygame.locals import *
import sys
import os 

#local imports
import basiclib #this module contains the biuildig blocks from player enemy and base classes 

###obs: Main not tested yet


class Main():
    """this class sets un runs the game"""
    def __init__(self):
        #this starts the application 
        pygame.init() #starts the pygame module
        pygame.font.init() #starts the pygame font module
        #make sure to latter add a configuration file 
        self.load()
        
    def load(self):
        pass


    def setup(self, path): #this path defines the setup --> name 'setup.json'
        
        #run game settings 
        self.gameover = False


        #screen setup
        self.SCREEN_SIZE = (800, 600)
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE) #sets the main screen 
        pygame.display.set_caption('Space Porn 101') #sets the text and icon to the window

        #time setup
        self.FPS = 60
        self.clock = pygame.time.Clock()

    def run(self): #runs one game loop

        time = self.clock.tick() / 100 # time in seconds since last iteration

        for event in pygame.event.get():
            if event.type == QUIT: #exits the game 
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN: #captures the right button of the mouse 
                pass

        self.screen.fill((0, 0, 0)) #fill the screen with the color black 

        pygame.display.update()
            

        

if __name__ == '__main__':
    main = Main()
    
