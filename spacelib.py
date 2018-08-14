#!/bin/bash/python3
# this module contains helpful functions to deal with archives and stuff 
 
import json
import os 
import sys 
import pygame 
from pygame.locals import *

###this part handles  json files 
###
### both 'json_decode' and 'json_encode' were tested  
###

#takes a json file and decodes it to a dict 
#for the purpose of this game, the json file must only contains 
#a set of attributes for on character 
def json_decode(path): #path to '.json' file 
    if os.path.exists(path):
        with open(path, 'r') as file:
            get = json.loads(str(file.read())) #gets a string and decodes it 
        return get #returs a dictionary 
    else:
        raise FileNotFoundError(f'[!] File { path } not found')

#encodes a dict to a json file 
def json_encode(obj, path, mode='w'): #path to '.jon' file 
    if not isinstance(obj, dict): #checks if the object is a dictionary
        raise TypeError(f"[!] Object { obj } must be a dictionary")

    if os.path.exists(path):
        with open(path, mode) as file:
            if mode == 'w': #overwrite the file
                new = json.dumps(obj, indent=4) #makes dict object to a indented string. UTF-8 
                file.write(new) #writes to the file 
            elif mode == 'rw': #appends to this file
                get = json.loads(file.read()) #reads the file and gets a dict object 
                for key, value in obj:
                    get[key] = value #stores all the keys and values from the riginal object in the file object
                new = json.dumps(get, indent=4) #makes a dict object to an indent string . UTF-8
                file.write(new) #writes to the path file
    else:
        #make sure to do a new path option in case of 'w' mode
        raise FileNotFoundError(f'[!] File { path } not found')



###############################################################################
###this next session is about get and parse the dialog lines from the characters 
###in the game in a formated text

###the dialog lines must be writen like: 
###1: the same dialog goes in the same line
###

#takes a path and returns a list of dialogs from the characters  
def text_get(path): 
    pass 

#max_char defines how many characters coes in the same line 
def text_parse(text, max_char=28):
    pass 

##################################################################################
###this part loads images
###
###default image format is '.png' 
#these funtions assume that the surface alpha are on 
#obs: not tested
def image_get(path): #takes an path and returns an image 
    image = pygame.image.load(path)
    return image 

def load_images(*list_path): #takes multiple paths and returns a list of images   
    new = []
    for path in list_path:
        new.append(image_get(path))
    return new 


