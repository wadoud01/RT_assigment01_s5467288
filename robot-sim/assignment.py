from __future__ import print_function

import time
from sr.robot import *


a_th = 2.0
"""Threshold for the control of the linear distance"""

d_th = 0.4
""" float: Threshold for the control of the orientation"""

silver = True
""" boolean: variable for letting the robot know if it has to look for a silver or for a golden marker"""

R = Robot()
""" instance of the class Robot"""
var = 0 #a variable used to exit the loops when required conditions are met
list_silver = []
list_golden = []
k = 0 # counter used to do progress 6 time only


def drive(speed, seconds):
    """
    Function for linear velocity
    speed (int): the speed of the wheels
    seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds): #function for motors of the robot
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_silver_token(): #function to detect and return the distance, angle, and ID of the Silver token Only

    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER:
            dist=token.dist # returning the distance of the silver token 
	    rot_y=token.rot_y # returning the angle of the silver token 
	    cods=token.info.code # returning the ID of the silver token 
    if dist==100:
	return -1, -1,-1
    else:
   	return dist, rot_y, cods

def find_golden_token():

    dist=150
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD:
            dist=token.dist 
	    rot_y=token.rot_y
	    codg =token.info.code # returning the ID of the golden token 
    if dist==150:
	return -1, -1,-1
    else:
   	return dist, rot_y, codg

def track_silver(): #this fuction only for silver tokens
	print("looking for a new Silver box")
	var = 0
	while (var == 0):# we use var as an condition to exit the loop
		dist, rot_y, cods = find_silver_token()# we look for markers
		if cods not in list_silver: # if the ID is new then do same progress only
			if dist == -1:
				print("not Close yet")
			elif dist <d_th: # if over exceed the threashold lets grab
				print("Lets grab it....")
				R.grab()
				print("Silver", cods, "was grabbed successfully")
				list_silver.append(cods) # we add the id to list so we can avoid the same token next time
				var = 1
			elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
				drive(25, 0.5)
			elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
				print("Left a bit...")
				turn(-2, 0.5)
			elif rot_y > a_th:
				print("Right a bit...")
				turn(+2, 0.5)
		else: # if there is no token detected in R.see() then turn little bit to detecte
			print("Looking for Silver token")
			turn(20, 0.5)
			var=0

def track_golden():
	print("Let's pair it  with the new nearist Golden box")
	var = 1
	while (var == 1): # we use var as an condition to exit the loop
		dist, rot_y, codg = find_golden_token()  # we look for markers
		if codg not in list_golden:
			if dist==-1:
				print("Coming to the golden")
			if dist <0.6:
				R.release()
				print("Paired with Golden", codg, "was done successfully")
				list_golden.append(codg) # we add the id to list so we can avoid the same token next time
				var = 0
			elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
				drive(25, 0.5)
			elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
				turn(-2, 0.5)
			elif rot_y > a_th:
				turn(+2, 0.5)
		else:# if there is no token detected in R.see() then turn little bit to detecte
			print("looking for golden")
			turn(20, 0.5)
			var=1




for k in range (6):#Our main function
	track_silver() #Start tracking silver first
	track_golden() #then we track the golden one
	drive(-15, 1)  #we drive backwards after releasing
	turn(22, 2.3) #we turn 180 degrees to strat a new check
	k += k # we upgrade the counter until 6 then we are finished
print("Mession was made successfully") #mession is done successfully


