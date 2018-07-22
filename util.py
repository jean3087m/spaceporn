#!bin/bash/python3 
#here are some game objects 

import pygame 
from pygame.locals import *

#local imports 
import spacelib as sl

class Layer(): #remember that layer_pool is a set! 
	""""this is the game layer object.
	tells which game objects can interact with others"""

	def __init__(layer_tag, layer_pool=[]): #default initializer
		self.layer_tag = layer_tag #this layer 
		self.layer_pool = set(layer_pool) #which objects can interact with this layer_tag 
		#make layer a set avoids redundancies 

	def add_to_pool(self, new):
		self.layer_pool.add(new) #adds to the pool set 

	def remove_from_pool(self, older):
		self.layer_pool.remove(older) #removes fromm the pool


	def interacts_with(self, basic_object): #checks if 2 objects 
		if isinstance(basic_object, Basic):
			if basic_object.layer.layer_tag in self.layer_pool: #tests if one object is in the others pool
				return True
			return False
		else:
			raise TypeError("[!] object must be Basic type")



class Basic():
	"""this is the basic building class of the game to represent
	phisical objects"""

	def __init__(self, _id, attrs):
		self.attrs = attrs
		self._id = _id

		#checks if the basic attributes exists
		#in case of lack of the basic attributes its throws an error 
		assert "size" in self.attrs, "[!] size attribute is not in attrs"
		assert "pos" in self.attrs, "[!] pos attribute is not in attrs"
		assert "color" in self.attrs, "[!] color attribute is not in attrs"
		assert "speed" in self.attrs, "[!] speed attribute is not in attrs"
		assert "layer_tag" in self.attrs, "[!] layer_tag attribute is not in attrs"
		assert "layer_pool" in self.attrs, "[!] layer_pool attribute is not in attrs"

		print("[*] basic object constructed sucessfully") #just runs if the assert statements are ok

		#makes the rect representation of the game object 
		self.rect = pygame.Rect(tuple(self.attrs['pos']), tuple(self.attrs['size'])) 
		#it is made like this because the layer tag and pool could change throughout game 
		self.layer = Layer(self.attrs['layer_tag'], self.attrs['layer_pool'])


	def move(self, time):
		pass

	def blit(self, surface): #draw the rectangle to the screen 
		pygame.draw.rect(surface, self.attrs['color'], self.rect)


