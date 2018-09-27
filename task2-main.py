# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  Image Processing- Path Planning (Prashikshan 2018)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Task_i
*  Filename: task2-main.py
*  Version: 1.0.0  
*  
*  Author: Prashikshan 2018.
*
**************************************************************************
"""
##################You are not allowed to add any external library here or methods in this file################## 
import sys
import cv2
import numpy as np
import pickle
from imgLib import *
########################################################################################
# This file will test your getCellVal.py with different test cases
# To compile the file, on the console type 
# python task2-main.py N
# where N is the total number of images to be read, strating from 1, Total 7 in your case
# At the end, you will see the results of the test cases verified.
#=============================================================
#					Task begins			
						 
#User providing the number of images files to be tested
############Do not delete this part of the code, you may add your own snippets here####################
N_images=int(sys.argv[1])
grid_line_x = 15
grid_line_y = 15
m=700/(grid_line_x-1)
n=700/(grid_line_y-1)
###Stores the route lengths detected in all the test images, maximum N route lengths only
route_length_result=[[0 for i in range(grid_line_y-1)] for j in range(N_images)]
###Stores the route paths detected in all the tested images, maximum N route paths only
route_path_result=[[]for k in range(N_images)]
###Stores the numbers detected for all the tested images, maximum N images
grid_map_result = [ [ [0 for i in range(grid_line_y-1)] for j in range(grid_line_x-1) ] for k in range(N_images) ]

######################Test case verification######################
############Do not edit this part of the code####################
def testCases(grid_map_result, route_length_result):
	grid_map_solution = pickle.load( open( "D:/ROBOTICS SOCIETY/MazeSolver_IP/Task4/Experiment-20180706T092510Z-001/Experiment/grid_map_solution.p", "rb" ) )                    ##Insert the complete path to grid._map_solution.p here##
	route_length_solution = pickle.load( open( "D:/ROBOTICS SOCIETY/MazeSolver_IP/Task4/Experiment-20180706T092510Z-001/Experiment/route_length_solution.p", "rb" ) )            ##Insert the complete path to route_length_solution.p here##
	# route_path_solution = pickle.load( open( "route_path_solution.p", "rb" ) )
	grid_error=0
	route_length_error=0
	flag=0
	for l in range(0, N_images):
		print ('Testing task2_img_',l+1,'.jpg')
		for i in range(0, grid_line_y-1):
			if(grid_map_solution[l][i]==grid_map_result[l][i]):
				print ("Row ",i+1,"is correct")
			else:
				print ("Row ",i+1,"is wrong")
				flag=1
				grid_error=grid_error+1
		if(flag==0):
			print ("Grid Cells for task2_img_",l+1,".jpg verified successfully, Testing for Route length")
			if(route_length_solution[l]==route_length_result[l]):
				print ("Route length for task2_img_",l+1,".jpg is correct")
			else:
				print ("Route_length for task2_img_",l+1,".jpg is incorrect")
				route_length_error=route_length_error+1
		else:
			print ("Grid cells' values are incorrectly identified, route length will not be verfied unless cells' values are correctly identified")
			flag=0
	print ("=======================================================================")
	print ("Grid Cells verification completed with ",grid_error,"errors")
	print ("Route length verification completed with ",route_length_error,"errors")
	if(route_length_error==0 and grid_error==0 and N_images>=7):
		print ("Test passed successfully. \n You can upload your submissions now. Good Luck")
######################end of method###############################
#######################Test images are passed here##########################
for k in range(1,N_images+1):
	grid_map = [ [ 0 for i in range(grid_line_y-1) ] for j in range(grid_line_x-1) ]
	imgpath='D:/ROBOTICS SOCIETY/MazeSolver_IP/Task4/Experiment-20180706T092510Z-001/Experiment/task2sets/task2_img_'+str(k)+'.jpg'                                      ##Insert the complete path to task2sets folder here in place of F:/Prashikshan 2018/Task_i/Experiment/task2sets/##
	route_length=0#stores the length of the valid route found in the image
	route_path=[] #stores the valid route_path found in the image
	img_rgb = cv2.imread(imgpath)
	img_gray = img_rgb
	#img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	#calling detectCellVal method to identify numbers in the grid cells and storing those in the grid_map array
	grid_map=detectCellVal(img_gray,grid_map)
	#calling solveGrid method to create a route betwwen the start row and the destination row, returning the route as route_path and length of the route as route_length
	route_path,route_length=solveGrid(grid_map)
	grid_map_result[k-1]=grid_map
	route_length_result[k-1]=route_length
	route_path_result[k-1]=route_path
	#printing the grid_map
	print (grid_map)
	#printing the results of the route detected in the image
	if(route_length==0):
		print ("No path found")
	else:
		print (" route length", route_length)
		print (" route path", route_path)
		
	#draw the route path found on the image, similar to what is shown in the Task description pdf
	########################Insert your code snippet here for drawing the route path on the image#####
	#your code here
	c = 0
	if route_length != 0:
		for i in range(route_length+1):
			for j in route_path[i]:
				if j.isdigit():
					c= c*10+int(j)
				elif j == ',':
					a = c
					c = 0
				elif j == ')':
					b = c
					c = 0
				else:
					c = 0
			if i!=0:
				img_rgb = cv2.line(img_rgb,(x*50-25,y*50-25),(a*50-25,b*50-25),(255,0,0),2)
			x = a
			y = b
			
	###############################your code snippet ends#############################################
	cv2.imshow('task2_img_'+str(k),img_rgb)
	cv2.imwrite('outputs/task2_img_'+str(k)+'.jpg',img_rgb)
	cv2.waitKey()#press escape to continue
########################Test Cases are verified here, do not edit this code#########################
print ("<--------------Starting Test Cases verification-------------->")
testCases(grid_map_result, route_length_result)
#=============================================================
# Your Task ends here