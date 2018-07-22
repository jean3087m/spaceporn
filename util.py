#!bin/bash/python3 
#here are some game objects 

import pygame 
from pygame.locals import *

#local imports 
import spacelib as sl

class Layer(): #remember that layer_pool is a set! 
	""""this is the game layer object.
	tells which game objects can interact with others"""

	def __init__(self, layer_tag, layer_pool=[]): #default initializer
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

	def pool_lenght(self): #retruns the lenght of the pool 
		return len(self.layer_pool)



class Basic():
	"""this is the basic building class of the game to represent
	phisical objects"""

	def __init__(self, _id, attrs):
		self.attrs = attrs
		self._id = _id

		#checks if the basic attributes exists
		#in case of lack of the basic attributes its throws an assert error 
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


	def move(self, time): #each child haves its own movement representation 
		pass

	def tofu_blit(self, surface): #draw the rectangle to the screen 
		#used to make a draw on the screen in case of toggle_tofu_mode=True 
		#also in case of no pictures were found 
		pygame.draw.rect(surface, self.attrs['color'], self.rect)


class Player(Basic):
	"""this is the player controller class"""

	def __init__(self, _id, attrs):
		super().__init__(_id, attrs) #gets from the mother class

	def move(self, time, mouse_pos): #time passed in seconds
		#mouse pos needs to be iterable 
		#makes a 2d vector that points from the player to the mouse position 
		new = sl.Vector2(mouse_pos[0], mouse_pos[1]) - sl.Vector2(self.rect.center[0], self.rect.center[1])
		#increments the new position to the vetoctor position
		new += new.unitary()*self.attrs['speed']*time
		#updates the player position 
		self.rect.center = new.x, new.y

	def blit(self, surface, toggle_tofu_mode=False): #draw the real player image (in this )
		if toggle_tofu_mode:
			self.tofu_blit(surface)
		else:
			pass 