# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  Image Processing-Path Planning (Prashikshan 2018)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Task3
*  Filename: imgLib.py
*  Version: 1.0.0  
*  
*  Author: Prashikshan Team.
*
**************************************************************************
"""
#Complete the both function mentioned below, and return the desired outputs
#Additionally you may add your own methods here to help both methods mentioned below
###################Do not add any external libraries#######################
import cv2
import numpy as np

# detectCellVal detects the numbers/operatorsm,
# perform respective expression evaluation
# and stores them into the grid_map 
# detectCellVal(img,grid_map)
# Find the number/operators, perform the calculations and store the result into the grid_map
# Return the resultant grid_map
def detectCellVal(img_gray,grid_map):
	#your code here

	#loop over each grid row no.
        for i in range(14):
		#loop over each grid column no.
                for j in range(14):
                        # to check the presence of '1' in the grid by comparing pixel value of blue of the central part of the grid
                        # which should be less than 128 i.e. not white or black as the centre of '0' is white and '1' is black
			if img_gray[i*50+25][j*50+25][0] < 128:
				grid_map[i][j]=1# assigning the corresponding element in grid_map as '1'
				
	return grid_map
############################################################################################
# solveGrid finds the shortest path,
# between valid grid cell in the start row 
# and valid grid cell in the destination row 
# solveGrid(grid_map)
# Return the route_path and route_length
def solveGrid(grid_map):
	route_length=0
	route_path=[]
	#your code here

	min_route_length = 28# to store the minimum route length as 28
	path_per_i = []# to store the shortest path for each element of the starting row
	count = []# to store the length of the shortest path for each element of the starting row
	xnd = []# list of lists to store the values of x for each iteration for each element of the starting node
	ynd = []# list of lists to store the values of y for each iteration for each element of the starting node

	#loop over each element of the starting row
	for i in range(14):

		x = 13# to store row no.
		y = i# to store column no./
		visit = np.zeros((14,14))# to store if a parrticular element is visited during a particular iteration or not
		xn = []# list to store the values of x for each iteration with this value of i
		yn = []# list to store the values of y for each iteration with this value of i
		path = []# to store the path as indices storing the values of x and y separated by '/' for each element of grid_map visited by the code
		p_iteration = 0# to store the no.of elements present in xn or yn and initialised to '0'
		path.append(str(p_iteration)+'/')# path to the 1st element i.e. the starting element 'i' itself is added to the list 'path'
		xn.append(x)# row no. of 1st element is added to list 'x'
		yn.append(y)# column no. of 1st element is added to list 'y'
		iteration_count=0# stores the total no. of elements visited and initialised to '0'
		count.append(0)# count for the ith element of the starting row is initialised to '0'
		path_per_i.append('')# shortest path for ith element is initialised to '' 
		

		# to check if the ith element of the starting row is a valid starting point i.e. equals to '1' or not
		if grid_map[x][y] == 1:

			no_of_breaks = 0# initialised to 0 for each occurence of '1' in the starting row and updated to 1 if a break occurs for any value of 'i' with '1'

			# to run the loop until a valid ending point('1') in the ending row is not reached for which the value of x(row no.) becomes 0
			while x!=0:

				# to check if the current element has got an element at its "adjacent upper-left diagonal" or not
				if y!=0:
                                        # to check if that element is '1' and non-visited or not
					if grid_map[x-1][y-1] == 1 and visit[x-1][y-1] != 1:
						xn.append(x-1)# adding the elments's row no. to xn
						yn.append(y-1)# adding the element's column no. to yn
						visit[x-1][y-1] = 1# marking the element as visited
						iteration_count = iteration_count+1# incrementing the no. of visited elements
						path.append(path[p_iteration]+str(iteration_count)+'/')# adding the path of the element to the list 'path'

				# to check if the "upper element adjacent" to the current element is '1' and non-visited or not
				if grid_map[x-1][y] == 1 and visit[x-1][y] != 1:
					xn.append(x-1)# adding the elments's row no. to xn
					yn.append(y)# adding the element's column no. to yn
					visit[x-1][y] = 1# marking the element as visited
					iteration_count = iteration_count+1# incrementing the no. of visited elements
					path.append(path[p_iteration]+str(iteration_count)+'/')# adding the path of the element to the list 'path'

				# to check if the current element has got an element at its "adjacent upper-right diagonal" or not
				if y!=13:
					# to check if that element is '1' and non-visited or not
					if grid_map[x-1][y+1] == 1 and visit[x-1][y+1] != 1:
						xn.append(x-1)# adding the elments's row no. to xn
						yn.append(y+1)# adding the element's column no. to yn
						visit[x-1][y+1] = 1# marking the element as visited
						iteration_count = iteration_count+1# incrementing the no. of visited elements
						path.append(path[p_iteration]+str(iteration_count)+'/')# adding the path of the element to the list 'path'

				# to check if the current element has got an element at its "adjacent left" or not
				if y!=0:
					# to check if that element is '1' and non-visited or not
					if grid_map[x][y-1] == 1 and visit[x][y-1] != 1:
						xn.append(x)# adding the elments's row no. to xn
						yn.append(y-1)# adding the element's column no. to yn
						visit[x][y-1] = 1# marking the element as visited
						iteration_count = iteration_count+1# incrementing the no. of visited elements
						path.append(path[p_iteration]+str(iteration_count)+'/')# adding the path of the element to the list 'path'

				# to check if the current element has got an element at its "adjacent right" or not
				if y!=13:
					# to check if that element is '1' and non-visited or not
					if grid_map[x][y+1] == 1 and visit[x][y+1] != 1:
						xn.append(x)# adding the elments's row no. to xn
						yn.append(y+1)# adding the element's column no. to yn
						visit[x][y+1] = 1# marking the element as visited
						iteration_count = iteration_count+1# incrementing the no. of visited elements
						path.append(path[p_iteration]+str(iteration_count)+'/')# adding the path of the element to the list 'path'

				# to check if the current element has got an element at its "adjacent lower-left diagonal" or not
				if y!=0 and x!=13:
					# to check if that element is '1' and non-visited or not
					if grid_map[x+1][y-1] == 1 and visit[x+1][y-1] != 1:
						xn.append(x+1)# adding the elments's row no. to xn
						yn.append(y-1)# adding the element's column no. to yn
						visit[x+1][y-1] = 1# marking the element as visited
						iteration_count = iteration_count+1# incrementing the no. of visited elements
						path.append(path[p_iteration]+str(iteration_count)+'/')# adding the path of the element to the list 'path'

				# to check if the current element has got an element at its "adjacent bottom" or not
				if x!=13:
					# to check if that element is '1' and non-visited or not
					if grid_map[x+1][y] == 1 and visit[x+1][y] != 1:
						xn.append(x+1)# adding the elments's row no. to xn
						yn.append(y)# adding the element's column no. to yn
						visit[x+1][y] = 1# marking the element as visited
						iteration_count = iteration_count+1# incrementing the no. of visited elements
						path.append(path[p_iteration]+str(iteration_count)+'/')# adding the path of the element to the list 'path'

				# to check if the current element has got an element at its "adjacent lower-right diagonal" or not
				if x!=13 and y!=13:
					# to check if that element is '1' and non-visited or not
					if grid_map[x+1][y+1] == 1 and visit[x+1][y+1] != 1:
						xn.append(x+1)# adding the elments's row no. to xn
						yn.append(y+1)# adding the element's column no. to yn
						visit[x+1][y+1] = 1# marking the element as visited
						iteration_count = iteration_count+1# incrementing the no. of visited elements
						path.append(path[p_iteration]+str(iteration_count)+'/')# adding the path of the element to the list 'path'

				# when no path exists for the ith element of the s************************************************************tarting row to reach the destiantion row, length of xn stays unchanged and
				# ultimately when p_iterations come to the last element, it breaks the while loop and go for the next element of the starting row
				if p_iteration == len(xn)-1:
					no_of_breaks = no_of_breaks + 1# no_of_breaks updated to 1 due to occurence of a break in the path to the destination row
					break# to go out of the while loop for the next value of 'i'

				p_iteration = p_iteration+1# incrementing the iteration
				x = xn[p_iteration]# assigning new row no. from list 'xn'
				y = yn[p_iteration]# assigning new column no. from list 'yn'

			k = 0
			# for each 'i', loop is run over the list containing row no.s
			for k in range(iteration_count+1):
				# to check the presence of an element having row no. as '0' i.e. present in the destination row
				if xn[k]==0:
					path_per_i[i] = path[k]# path of the selected element of the destination row is alloted as the shortest path for that value of 'i'
					break# After having obtained one shortest path, the for loop is exit

			# to check if the shortest path is obtained
			if path_per_i[i] == path[k]:
				# a for loop is run over the shortest path obtained in order to calculate the total no. of elements or steps taken to reach the destination row
				for l in path_per_i[i]:
					if l == '/':
						count[i]=count[i]+1# incrementing the count with each occurence of '/' which symbolizes the occurence of another step

		xnd.append(xn)# adding the list of row no.s(xn) for each value of 'i' to the list 'xnd'
		ynd.append(yn)# adding the list of column no.s(yn) for each value of 'i' to the list 'ynd'

		# if a path with count 14 is obtained for a particular value of 'i',
		# the for loop is exit as the shortest path is already found having the least value for count which can't be less than 14
		if count[i] == 14:
			break

	# to check for the presence of atleast one shortest path
	if no_of_breaks != 1:
		
		# loop over the entire starting row
		for i in range(14):
			# to check for the presence of path from a particular element in the starting row
			if count[i] != 0:
				# to check if 'i' has a count of 14 which would mean the shortest path for the entire array
				if count[i] == 14:
					min_i = i# ith element of tha starting row is taken as the element having the shortest path
					min_route_length = 13# minimum route length is assigned with a value 13 as no. of steps to obtain the count 14 must be 13
					break
				# if the count for that value of 'i' is not 14
				else:
					# to check if the count for this value of 'i' is less than the current minimum route length
					if min_route_length > count[i]:
						min_i = i# ith element of tha starting row is taken as the element having the shortest path
						min_route_length = count[i]-1# minimum route length is assigned with a value 13 as no. of steps to obtain the count must be 'count-1'

		main_path = path_per_i[min_i]# path obtained is assigned as the main path
		route_length = min_route_length# minmum route length obtained is assigned as the route_length
		#if the minimum route length was updated
		if min_route_length != 28:
			c = 0# to store the integer values(indices) for each element
			# loop over the entire path
			for i in main_path:
				# just calculate for numbers
				if i != '/':
					c = c*10 + int(i)
				# when '/' occurs, the previous no. ends
				else:
					route_path.append('('+str(ynd[min_i][c]+1)+','+str(xnd[min_i][c]+1)+')')# the column no. and row no. are added to the route_path as string elements
					c = 0# initialised to '0' for obtaining the new no.
					
	return route_path, route_length
############################################################################################
