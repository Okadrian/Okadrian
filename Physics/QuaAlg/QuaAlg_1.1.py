# This is a module to assist linear algebra calculation with an extra focus on quantum mechanics
# 
#
# Matrix form defined by M[i][j]=
#[[3,5,7],
# [3,8,9],
# [1,6,8]]
# postions of 5 is i=0 and j=1 postion of 9 is i=1 and j=2
#
#
#
# If you want a compex matrix. Define K=[R,C]
# Where R is the real part and C is the complex part
# R and C is in the same form as the ordinary matrix

import math

def scal_vec(v,s):#Multiplication between vector and scalor

	n_v=[]

	for i in range(0,len(v)):

		n_v.append(s*v[i])

	return n_v

def scal_mat(M,s):#Multiplication between matrix and scalor

	M_new=[]

	for j in range(0,len(M)):

		M_new.append([])

		for k in range(0,len(M)):

			M_new[j].append(s*M[j][k])

	return M_new

def scalar_prod(v_1,v_2):#This is a function to take two vectors and return the scalar product

	if len(v_1)==len(v_2):

		result=0

		for i in range(0,len(v_1)):# It multplies the two places in place i and add that to the old result in palce i-1

			result=result+v_1[i]*v_2[i]

	else:

		print("vector size error")

		return None

	return result


def matrix_prod(M_1,M_2):#Multplies two matrix

	if matrix_prod_possible(M_1,M_2)==True:#Test if the matrix dimention is correct for multplication

		M_N=[]

		for j in range(0,len(M_1)):

			M_N.append([])

			for k in range(0,len(M_2)):

				v_2=column_vector(M_2,k)# Take the column of this vector in space k

				M_N[j].append(scalar_prod(M_1[j],v_2))# Makes a scalor product between vector M_1 in row j and M_2 coloumn k. 
													  #Just like in the definiton. Create a new matrix with a element in that space

	else:

		print("These matrix can not be multplied in this order")

		return None

	return M_N

def matrix_add(M_1,M_2):# Add two matrix to eachother

	M=[]

	if len(M_1)==len(M_2):

		for i in range(0,len(M_1)):

			M.append([])

			for k in range(0,len(M_1)):

				M[i].append(M_1[i][k]-M_2[i][k])

	return M

def matrix_prod_possible(M_1,M_2):#Check if matrix size of M_1 and M_2 are of right size to multiply

	if len(M_1[1])==len(M_2):

		return True

	else:

		return False

def column_vector(M,c):#Return a column vector in a matrix. 

	v=[]

	for i in range(0,len(M[c])):#Look at all element in a row

		v.append(M[i][c])

	return(v)

def commute_matrix(M_1,M_2):#Check if matrix A, B commute or not. 

	M_3=matrix_prod(M_1,M_2)#A*B=M_3

	M_4=matrix_prod(M_2,M_1)#B*A=M_4

	commuter=matrix_add(M_3,M_4)#AB-BA=commuter

	return commuter

def check_matrix(M):#Check if matrix is properly made. No other variable then int or float in a space of the matrix

	int_or_float=True

	for j in range(0,len(M)):

		for k in range(0,len(M)):

			if type(M[j][k])!=int and float:#Very simple code goes throgh all element if one element is not a int or float set that to false and tell the user.

				int_or_float=False

	if int_or_float==True:

		print("This matrix is possible")

		return True

	else:

		print("This is not a possbile matrix")

		return False

def mat_sym(M):#Check if matrix is symmetric or not

	symmetric=True

	for i in range(0,len(M)):

		for j in range (0,len(M[1])):
			
			if M[j][i]!=M[i][j]: #If it not symmetric in one place set symmetric to false. Else it is true se start of code

				symmetric=False

	if symmetric==True:

		print("This matrix has a real Symetric part")

		return True

	else:

		print("This matrix does not have a real Symetric part")

		return False

def scal_com_mat(K):#Multplication between an complex matrix and a scalor

	R=scal_mat(K[0],s)#Scalor multplied with matrix real part

	C=scal_mat(K[1],s)#Scalor multplied with matrix complex part

	return [R,C]

def mat_her(K): 
	#Check if matrix is hermitian 
	# This process has to step. First check if the real part K[0] is symmetic
	# And then the second part of checking that the other part is conujugate symmetric.

	Real=mat_sym(K[0])# Real is true if matrix symmetric

	M=K[1]

	Imaginary=True

	for i in range(0,len(M)):#Here we test conjugate summetry

		for j in range (0,len(M[1])):
			
			if M[j][i]!=M[i][j]*-1:

				if j!=i:

					Imaginary=False

	if Imaginary==True:

		print("This is a sveski linear complex matrix")

	else:

		print("This is not a sveski complex matrix")

	if Imaginary==Real==True:

		print("This is a hermitian operator")

		return True

	else:

		print("This is not a hermitian operator")

		return False

def spin_mat(ro,theta):
	#Return the spin matrix, I just use the definiton of the spin matrix
	#Information about the definition can of the spin matrix can be found on wikipedia and in quantum book

	R=[[math.cos(theta),math.sin(theta)*math.cos(ro)],[math.sin(theta)*math.cos(ro),-math.cos(theta)]]
	C=[[0,-math.sin(theta)*math.cos(ro)],[math.sin(theta)*math.cos(ro),0]]

	return [R,C]

def print_matrix(M):#Prints matrix takes in a input returns nothing prints only for the user. The function is mostly useful for complex matrix
	if type(M[0][0])==list:#Check if matrix is of the komplex type

		for i in range(0,len(M[0][0])):#Check size of row 

			row=[]

			for k in range(0,len(M[1])):#Chech size of coloum

				real=M[0][i][k]#Takes Data

				komplex=M[1][i][k]

				element=[]

				#Some if statement to make the matrix look prety
				#if real or imaginary does not exist dont print it

				if real!=0:

					element.append(real)

				if komplex!=0:

					if real!=0:

						element.append("+")

						element.append(komplex)

						element.append("i")

					else:

						element.append(komplex)
						element.append("i")

				#Add one element into one string

				res = ' '.join([str(item) for item in element]) 

				#Append the element to the row

				row.append(res)

			print(row)		

	else:#If matrix was not complex just print

		for i in range(0,len(M)):

			print(M[i])




def healthy():


	M_1=[[1,2],[3,4]]
	M_2=[[5,6],[7,8]]

	#Test matrix product 

	M_3=matrix_prod(M_1,M_2)
	M_4=matrix_prod(M_2,M_1)

	assert([[19, 22], [43, 50]]==M_3)

	assert([[23, 34], [31, 46]]==M_4)


	#Test scalor times a matrix

	M_5=scal_mat(M_1,5)

	assert (M_5==[[5,10],[15,20]])

	#Test if matrix is proper print "This matrix is possible and return Trye"

	M_POS=[[1,2],[3,4]]

	assert(True==check_matrix(M_POS))

	#Test if matrix is proper print "This is not a possible matrix "

	M_False=[[1,2],[1,"A"]]

	assert(False==check_matrix(M_False))


	#Calculate the commuter of the matrix

	commute=commute_matrix(M_1,M_2)

	assert ((commute)==[[-4, -12], [12, 4]])

	#Calculate one more commuter

	M_1=[[1,2],[3,4]]

	M_2=[[1,2],[3,4]]

	commute=commute_matrix(M_1,M_2)

	assert ((commute)==[[0, 0], [0, 0]])

	#Test if symmetric matrix symmetic

	Sym=[[1,2],[2,3]]

	assert (mat_sym(Sym)==True)

	#Test if a not symmetric matrix symmetic

	assert (mat_sym(M_1)==False)

	S=[[1,2],[2,3]]
	C=[[1,-2],[2,3]]

	#Create a complex matrix

	K=[S,C]

	assert (mat_her(K)==True)

	S=[[1,2],[2,3]]
	C=[[1,2],[2,3]]

	K=[S,C]

	# Test if that matrix is hermation is should not be

	assert (mat_her(K)==False)

	#Test is a spin matrix is hermiatian. It should always be hermiatian

	Spin=spin_mat(math.pi/2,math.pi/2)#Spin matrix is always hermiation in Quantum therfore it is a perfect test case

	assert (mat_her(Spin)==True)


if __name__ == "__main__":

	healthy()


