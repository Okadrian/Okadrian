import random




def linear_sort(vector):

	#sort a vector of certain 

	"""This is just some test cases to check if input is valid"""

	if type(vector)!=list:
		print("not valid input")
		return None

	for j in vector:

		if type(j)!=int:
			print("not valid input")
			return None

		if j<0:
			print("not valid input")
			return None

	"""Test cases are done"""


	a=max(vector)

	hash_table={}

	for i in range (0,a+1):#Create the hash table

		hash_table[i]=0

	for j in range(0,len(vector)):#Add elements to hash table

		b=hash_table[(vector[j])]
		hash_table[vector[j]]=b+1

	sorted_lista=[]

	for k in range(0,a+1):

		for l in range(0,hash_table[k]):

			sorted_lista.append(k)

	return(sorted_lista)




def healthy():

	"""Test if the function is healthy"""

	v=[3,2,1,5,6,3]

	assert(linear_sort(v)==[1,2,3,3,5,6])

	v=[-3,-2,-1,-1,-1,-5,-5]

	assert(linear_sort(v)==None)

	v="A"

	assert(linear_sort(v)==None)

	v=[100,1,1,1,2,2,2]

	assert(linear_sort(v)==[1,1,1,2,2,2,100])

	v=[]

	for i in range(0,10):

		v.append(random.randint(0,5))

	print(linear_sort(v))

if __name__ == "__main__":
	
   healthy()


#k needs to be smaller or equal to n. If it way bigger then the time will be more dependent on k then on n
#If this is the case then this is not a efficent method in ordering the list.
#So given 

