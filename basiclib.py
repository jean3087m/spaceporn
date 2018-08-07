import sys 
import pygame 
from pygame.locals import *
import datetime
import os

class Layer:
    """class to make a interacion pool priority"""
    def __init__(self, layer_id=0, layer_name=''): #default init 
        self.layer_id = layer_id #by default it must be hexadecimal number 
        self.layer_name = layer_name  #a string type 
    
    def layer_dict(self): #makes a dictionary out of a Layer object and return 
        return {'name':self.layer_name, 'id':self.layer_id}
    
    def __repr__(self): #printable version of the type Layer 
        return f'LAYER >> name :{ self.layer_name }\tid :{ self.layer_id }'
    
    def __eq__(self, other): #check if two Layer have the same param 
        if isinstance(other, Layer):
            if other.layer_id == self.layer_id and other.layer_name == self.layer_name:
                return True
            else:
                return False
        #raise type error in the case of a missing type 
        raise TypeError(f"[!] Error: cannot match diferent types 'Layer' : type { type(other) }")

    def setup(self, layer_id, layer_name): #sets this layer to a new configuration 
        #"Attend to your configuration!"
        self.layer_id = layer_id
        self.layer_name = layer_name

class Base:
    """This is the bilding block of an game object"""
    def __init__(self, _id, attrs):
        self._id == _id 
        self.attrs = attrs
        #the given attributes must be a dictionary were the arguments have the specifications 
        #in case of the basic arguments are not found it throws an assert error 
        assert  self.attrs['color'] , "[!] attrs argument must have a 'color' "
        assert  self.attrs['size'] , "[!] attrs argument must have a 'size' "
        assert  self.attrs['pos'] , "[!] attrs argument must have a 'pos' "
        assert  self.attrs['color'] , "[!] attrs argument must have a 'speed' "
        #this makes the game be played in 'Tofu Mode'

        self.rect = pygame.Rect(self.attrs['pos'], self.attrs['size']) #makes an rectangle 
        try: #makes Layer to Base class 
            self.layer = Layer(self.attrs['layer_id'], self.attrs['layer_name'])
        except:
            self.layer = Layer() #makes an empty layer

    def tofu_blit(self, surface): #this is a Tufu Mode blit to surface 
        pygame.draw.rect(surface, self.attrs['color'], self.rect) #draws a rectangle 
    

class Player(Base):
    """this is the player class"""
    def __init__(self, _id, attrs):
        super().__init__(_id, attrs) #gets from the mother class 

class Log:
    """this is the player console log"""
    def __init__(self, font_name='comicsans', font_size=10, pos=(0, 0)):
        self.font = pygame.font.SysFont(font_name, font_size) #makes a font 
        self.text = ''
        self.color = pygame.color.Color(255, 255, 255, 50) #color white with transparency
        self.image_font = self.font.render(self.text, 0, self.color)
        self.pos = pos

        #change this latter to have a terminal like Log 
    
    def blit(self, surface):
        #draws the image font to the surface 
        surface.blit(self.image_font, self.color)
    
    def change_text(self, new_text):
        self.text = new_text #saves the new text
        self.image_font = self.font.render(self.text, 0, self.color) #chnages the font image

    def save_log(self, path): #saves the text to the path 
        with open(path, 'w') as f:
            f.write(f'[{ datetime.datetime.now() }]' + self.text)

        
    
    
    
        


        
         

        

        
    
