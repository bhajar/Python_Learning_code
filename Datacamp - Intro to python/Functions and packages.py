# Functions

# lots of functions out of the box like print and type
# there are also str(), float(), bool(), int(), list()
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

help(max)
?max

?complex
?sorted

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)

# other methods for which we may need to create functions
# Python objects also come with methods

# index is a method and not a function
# count is also a method 
# all python objects have methods associated with them 
# Everything in python is an object and every object has methods
# index is a method with lists and strings
# append is another method

# string to experiment with: room
room = "poolhouse"

# Use upper() on room: room_up
room_up = room.upper() # using upper does not change room!

# Print out room and room_up
print(room); print(room_up)

# Print out the number of o's in room
print(room.count("o"))


# List methods
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 14.5 appears in areas
areas.count(14.5)

# append, remove, reverse

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)


# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse() # this changes the order for good

# Print out areas
print(areas)

# Packages
# installing can be a bitch on windows
# anaconda might have packages preinstalled

import numpy as np # to import the whole package

from numpy import array # to only import a single function from a package


# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * math.pi * r

# Calculate A
A = math.pi * r**2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))


# more selective import from package

from math import pi
# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon if 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)

# scipy has a subpackage linalg; we want to use the function inv

from scipy.linalg import inv as my_inv # just calling the function a different name





































