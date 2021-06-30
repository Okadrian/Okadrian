# K-mean Clusters

import random as ran
import numpy as np
from matplotlib import pyplot as plt

data_range=50

pi=3.1415926535897932

colour_list=["b","g","r","c","m","y","k","w"]

#Define you amount of clusters k more then 8 can not be plotted
Y=5

def metric(x,y): # The metric function of the space

	#Dimention need to be same of x and y

	n=len(x)

	d=[]#d is for distance

	for i in range(0,n):

		d.append(x[i]-y[i])

	return d

def create_data():# a function to define data that forms a spehere 

	X=[]


	for i in range(0,6):


		for j in range(0,100):

			r=ran.uniform(0,data_range)

			theta=ran.uniform(-pi,pi)


			l=[r*np.cos(theta),r*np.sin(theta)]

			X.append(l)

	return X# Create the data set to train on



def K_Cluster(X,k):# Find the best cluster
	clusters={}

	#Create clusters hash tabels
	for i in range (k):

		clusters[i]=[]

	centroids=[]

	#Create the centroids

	for i in range (k):

		centroids.append([])

		centroids[i] = X[i]

	#Create the initial clusters

	for data in X:

		euc_dist = []

		for i in range(k):

			d=metric(data,centroids[i])

			euc_dist.append(np.linalg.norm(d))

		clusters[euc_dist.index(min(euc_dist))].append(data)

	#Loops centroids and clusters to find the optimum

	for i in range(0,100):

		centroids=recalculate_centroids(centroids,clusters,k)

		clusters=recalculate_clusters(X,centroids,k)


	cluster=np.array(clusters)

	return centroids,clusters



def recalculate_clusters(X, centroids, k):

	clusters={}


	#Create clusters hash tabels

	for i in range (k):

		clusters[i]=[]

	#Create the clusters

	for data in X:

		euc_dist = []
		for i in range(k):


			d=metric(data,centroids[i])
			euc_dist.append(np.linalg.norm(data-centroids[i]))

		clusters[euc_dist.index(min(euc_dist))].append(data)

	return clusters

def recalculate_centroids(centroids, clusters, k):

	for i in range(k):

		centroids[i] = np.average(clusters[i],axis=0)

	return centroids

def draw_data(clusters,centroids,k):

	for i in range(0,k):

		for l in range(0,len(clusters[i])):

			colour=colour_list[i]

			x=clusters[i][l][0]
			y=clusters[i][l][1]
			plt.scatter(x, y)

			plt.scatter(x, y,s=50,c=colour,)
	for i in range(0,k):

		for l in range(0,len(centroids[i])):

			colour=colour_list[i]

			x=centroids[i][0]
			y=centroids[i][1]
			plt.scatter(x, y)

			plt.scatter(x, y,s=300,c="y", marker="*")

	plt.show()

X=create_data()

centroids,clusters=K_Cluster(X,Y)

draw_data(clusters,centroids,Y)


