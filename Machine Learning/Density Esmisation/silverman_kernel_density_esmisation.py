import random as ran
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

A=100
F=2#Fix t0 center window arond the spam. Make it about 2% as big as A

def create_data():#Create some data that is normal distrubutated in a complex way (alot of modes)

	X=[]

	for i in range(0,10000):

		whole=ran.randrange(-A,A)

		for j in range(0,2):

			if whole<-50:

				gaussian=ran.gauss(0,20)


			elif whole<50:

				gaussian=ran.gauss(0,40)

			else:

				gaussian=ran.gauss(0,10)


			X.append(whole+gaussian)
	return X

def gaussian(x, sig):
	return np.exp(-np.power(x, 2.) / (2 * np.power(sig, 2.)))


def silverman(X):

	#Define constants for function

	average=np.mean(X)

	standard=np.std(X)


	#Silvermans rule of thumb

	a=np.power(4*standard,5)
	b=len(X)*3
	h=np.power((a/b),(1/5))

	# Plot result

	fun=0

	x_axis = np.arange(-A+F, A-F, 0.01)

	y=0

	for x in X:

		y=y+stats.norm.pdf(x_axis, x, h)/len(X)

	len(x_axis)
	len(y)


	plt.plot(x_axis, y)
	plt.show()


X=create_data()
silverman(X)
