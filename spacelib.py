#!bin/bash/python3 

#this a is a lib about archive manipulatiion 
#json manipulation
#linear algebra and calculus 


import json
import sys 
import os 
import random

################json handler functions#####################

###obs:
###change the encode type later
###the writen files are disformated 

###obs 2: for caompatibility issues aways uses 'os.path.join' and 'os.path.split' 

def get_object_attribute(name, path): #by default path must be to file type '.conf'
	#gets the attribute of a '.conf' file and returns 
	#retruns the general attribute of an 'name' object 
	#obs: does'nt retruns an specific attribute but a complete attribute dict 
	if os.path.exists(path):
		with open(path, 'r') as f:
			try:
				get = f.read() #rads all the file
				print(f'[*] file { path } red sucessfully')
			except Exception:
				get = "{}" #returns an empty dict string 
				print("[!] couldn't read file")
			finally:
				return json.loads(get)[name] #returns an dictionary of the name chosen attributes 
	else:
		raise FileNotFoundError("[!] file doesn't exists") #raises error file not found 


def write_object_attribute(name, name_dict, path):
	#writes an object to a file '.conf' (default type)
	#name_dict format must be dict 
	#name is a string 
	#appends to the file : {name:name_dict}

	if os.path.exists(path):
		token = '{}'
		with open(path, 'r') as f: #reads the files for append the new attribute 
			token = json.loads(f.read()) #makes all the file to a dictionary 
			print(f'[*]file { path } red sucessfully')
		with open(path, 'w') as f:
			token[name] = name_dict
			f.write(json.dumps(token)) #makes the dict obj to a '.conf' file 
			print(f'[*] file { path } writen sucessfully')
	else:
		raise FileNotFoundError("[!] file doesn't exists")


##########################################################################


######################linear algebra space tools#########################

class Vector2:
	"""defines a 2D vector representation"""

	def __init__(self, x=0, y=0):
		#default init 
		self.x = x
		self.y = y

	def __repr__(self): #fromated str representation
		return f'Vector2 <X={ self.x }, Y={ self.y }>'

	def __add__(self, other): #adds to another vector 
		if isinstance(other, Vector2):
			return Vector2(self.x + other.x, self.y + other.y) 
		else:
			raise TypeError("[!] type must be Vector2")

	def __sub__(self, other): #subtracts by another vector 
		if isinstance(other, Vector2):
			self.__add__((-1)*other)
		else:
			raise TypeError("[!] type must be Vector2")

	def __rmul__(self, scalar): #multiplication by 'real' numbers 
		return Vector2(scalar*self.x, scalar*self.y)

	def __mul__(self, scalar): #multiplication by int numbers 
		return Vector2(scalar*self.x, scalar*self.y)

	def __truediv__(self, scalar):
		if scalar == 0:
			raise ZeroDivisionError("[!] seriuos pal!?")
		else:
			self.__rmul__(1 / scalar) #divides number by true division  

	def dot(self, other):
		if isinstance(other, Vector2):
			return other.x*self.x + other.y*self.y
		else:
			raise TypeError("[!] type must be Vector2")

	def module(self): #returns the vectors mudule  
		return (self.x**2 + self.y**2)**(1/2)

	def unitary(self): #returns the unitary vector pointing to the same direction 
		return self / self.module()


#####################################################################################
			


















