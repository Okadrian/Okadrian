# A simple classifier with a metric function that determines the classifiers abilities. 
#The classifier runs both nearest neighbor method with 1 and k data sets. 

# This machine learning program is made to classify things that has abilities that are on a spectrum

import random as ran

def most_frequent(List):
    counter = 0
    num = List[0]
      
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
  
    return num

def create_data():
	X=[]


	for i in range(0,1000):

		l=[ran.uniform(0,5),ran.uniform(0,5)]

		if l[0]+l[1]<3:

			y="safe"

		elif l[0]+l[1]>8:

			y="safe"

		else:

			y="dangerous"

		X.append([l,y])

	return X

def metric(x,y): #The metric function of the space

	#Dimention need to be same of x and y

	n=len(x)

	d=[]#d is for distance

	for i in range(0,n):

		d.append(x[i]-y[i])

	return d

def scalor_product(d): #The scalor product of the space 

	n=len(d)

	s=0

	for i in range(0,n):

		s=s+d[i]*d[i]

	return s

def nearest_neighbor(X,v):# Find the nearest neighbor of a point
	
	d=metric(X[0][0],v)

	s_old=scalor_product(d)

	for i in range(0,len(X)):

		d=metric(X[i][0],v)

		s_new=scalor_product(d)#Find the scalor product between all distance. 

		if s_new<s_old:

			match=X[i][1]#The return is value of the smallest scalor product

			point=X[i]

			s_old=s_new


	return match

def nearest_neighbor_k(X,v,k):# Find the nearest neighbor of a point

	s_list=[]

	s_list_match=[]

	for i in range(0,k):# Create an initial list of the seven closest neigbors

		d=metric(X[i][0],v)

		s=scalor_product(d)

		s_list.append(s)

		s_list_match.append(X[i][1])

	for i in range(0,len(X)):#loop through all the point

		m=max(s_list)

		index=s_list.index(m)

		d=metric(X[i][0],v)

		s=scalor_product(d)

		if s<m:#change one of the neigbors if we find a closer point

			s_list[index]=s

			s_list_match[index]=X[i][1]

	return most_frequent(s_list_match)

def test():
	v_1=[3,3]#Should be dangerous
	v_2=[1,2]#should be 50% dangerous and 50% safe
	v_3=[0,0]#Should be safe

	v_list=[v_1,v_2,v_3]

	X=create_data()


	for i in v_list:

		match=nearest_neighbor(X,i)

		print(match)

	for i in v_list:

		match=nearest_neighbor_k(X,i,7)

		print(match)


test()






