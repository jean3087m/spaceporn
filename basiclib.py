#!/bin/bash/python3

#this module contain the basic constructors to the game elements 


import sys 
import pygame 
from pygame.locals import *
import datetime
import os

#local imports 
import spacelib 

class Layer:
    """class to make a interacion pool priority"""
    def __init__(self, layer_id=0, layer_name='', layer_pool=[]): #default init 
       self.setup(layer_id, layer_name, layer_pool)
    
    def layer_dict(self): #makes a dictionary out of a Layer object and return 
        return {'name':self.layer_name, 'id':self.layer_id}
    
    def __repr__(self): #printable version of the type Layer 
        return f'LAYER >> name :{ self.layer_name }\tid :{ self.layer_id }'
    
    def __eq__(self, other): #check if two Layer have the same name 
        if isinstance(other, Layer):
            if other.layer_name == self.layer_name:
                return True
            else:
                return False
        #raise type error in the case of a missing type 
        raise TypeError(f"[!] Error: cannot match diferent types 'Layer' : type { type(other) }")

    def setup(self, layer_id, layer_name, layer_pool): #sets this layer to a new configuration 
        self.layer_id = layer_id #by default it must be hexadecimal number 
        self.layer_name = layer_name  #a string type 
        self.layer_pool = layer_pool #this is the set to dectect with witch this layer can interact with 
        #the layer pool must be treated as a set 

    def collide(self, other): #retruns true if two layers can interact
        #the other is a Base class or child
        if other.layer.layer_name in self.layer_pool:
            return True
        return False 

class Base:
    """This is the bilding block of an game object"""
    #the Base van be innitialized by a path or by an attribute
    # the priority is the 'path' file 
    #the problem is that one of them becames redundant --> maybe change latter
    # this part is really bodering me    
    def __init__(self, _id, attrs={}, path=None):
        if attrs == {} and path == None:
            raise Error("[!] At least 'path' or 'attrs' must be initialized")
        if path == None:
            get_attrs = attrs
        else:
            get_attrs = spacelib.json_decode(path)
        self.setup(_id, get_attrs)
            
    def tofu_blit(self, surface): #this is a Tufu Mode blit to surface 
        pygame.draw.rect(surface, self.attrs['color'], self.rect) #draws a rectangle
    
    def collide(self, other):
        #the other is a Base class or child 
        if self.rect.colliderect(other.rect) and self.layer.collide(other): #checks if the base collide with another 
            return True
        return False

    def setup(self, _id, attrs):
        
        self._id = _id 
        self.attrs = attrs
        #the given attributes must be a dictionary were the arguments have the specifications 
        #in case of the basic arguments are not found it throws an assert error 
        assert  self.attrs['color'] , "[!] attrs argument must have a 'color' "
        assert  self.attrs['size'] , "[!] attrs argument must have a 'size' "
        assert  self.attrs['pos'] , "[!] attrs argument must have a 'pos' "
        assert  self.attrs['speed'] , "[!] attrs argument must have a 'speed' "
        
        #this makes the game be played in 'Tofu Mode'

        self.rect = pygame.Rect(self.attrs['pos'], self.attrs['size']) #makes an rectangle 
        try: #makes Layer to Base class 
            self.layer = Layer(self.attrs['layer_id'], self.attrs['layer_name'], self.attrs['layer_pool'])
        except:
            self.layer = Layer() #makes an empty layer

    
class Player(Base):
    """This defines the player"""#"Attend to your configuration!"
       
    def __init__(self, _id, attrs={}, path=None):
        super().__init__(_id, attrs, path) #initializes the mother class

    def move(self, delta_time):
        pass 

    #this looks a bit dumb --> change latter 
    def blit(self, surface, tofu_blit=False):
        if not tofu_blit:
            self.tofu_blit(surface)
        else:
            pass




class Log:
    """this is the player console log"""
    def __init__(self, font_name='comicsans', font_size=10, pos=(0, 0)):
        #make sure that the font mudule was initialized 
        assert pygame.font.get_init(), "[!] The font mudule must be initialized"

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
        #remeber to use 'os' for compatibility 
        with open(path, 'w') as f:
            f.write(f'[{ datetime.datetime.now() }]' + self.text)
    
    
        
    
    
    
        


        
         

        

        
    
