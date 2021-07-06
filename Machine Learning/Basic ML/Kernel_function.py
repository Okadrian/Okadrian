"""Kernel function """

# This is just a fast way to add dimenstion to all the data in a function through a kernel scalor method. 
# I just simple add one dimenstion in order to make more advanced analysis with for an example a SVM "Support Vector Machines"



X=[[2,3],[4,3],[3,4],[6,3],[1,2]]
def kernel_scalor(X):

	New_X=[]

	for i in range(0,len(X)):

		s=0

		New_X.append([])



		for j in range (0,len(X[0])):

			New_X[i].append(X[i][j])

			s=s+X[i][j]*X[i][j]

		New_X[i].append(s)


	return New_X



New_X=kernel_scalor(X)

print(New_X)





