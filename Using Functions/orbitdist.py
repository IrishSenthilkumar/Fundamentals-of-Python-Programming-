'''
Created on 10 Sep 2018

@author: Irish
'''

from math import *

# User input for the coordinates of the spacecraft
spacecraftX = float(input("X Position of the stationary spacecraft : "))
spacecraftY = float(input("Y Position of the stationary spacecraft : "))

print("\n")

# User input for the starting coordinates of the satellite
satelliteX = float(input("X Position of the moving satellite : "))
satelliteY = float(input("Y Position of the moving satellite : "))

# Convert degrees to radians
theta = radians(60)

cosTheta = cos(theta)
sinTheta = sin(theta)

print("\n")

for increment in range(0, 7):
    distance = sqrt((spacecraftX - satelliteX)*(spacecraftX - satelliteX) + (spacecraftY - satelliteY)*(spacecraftY - satelliteY))
    print("Distance to satellite : {0:10.2f}".format(distance))
    
    satelliteX = satelliteX*cosTheta - satelliteY*sinTheta
    satelliteY = satelliteX*sinTheta + satelliteY*cosTheta




