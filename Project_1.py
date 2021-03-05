#Task 1

#giving area of circle by taking input from user.

from math import pi

r = float(input ("\nInput the radius of the circle : "))

print ("\nThe area of the circle with given radius " + str(r) + " is: " + str(pi * r**2))


#Task 2

#giving extension of file which is inputed by user.

i = input("\nInput the file name : ")

ext = i.split(".")

print("\nThe extension of this file is : " + repr(ext[-1]))