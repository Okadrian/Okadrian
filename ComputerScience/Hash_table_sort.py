

# function to get unique values
def unique(list1):
	# intilize a null list
	unique_list = []

	# traverse for all elements
	for x in list1:
        # check if exists in unique_list or not
		if x not in unique_list:
			unique_list.append(x)
	return(unique_list)


def mode(vector):
	"""Mode is a functions that uses for loops and a hashtable to find the mode of the function. Does this in W(n) """
	if type(vector) is not list:#Test for propper input
		print( str(vector) +" Is not a list the function will return None")
		return None

	if len(vector)==0:#Test for propper input
		print("Empty list return None")
		return None

	for i in range (0,len(vector)):#Test for propper input

		if isinstance(vector[i], int)==False:

			print("The list is not only keys "+str(vector[i])+ " That is in the place " + str(i) + " Is not a key. keys need to be written in int or float form")
			print("The function will return None")

			return(None)


	vector_ent=unique(vector)

	hash_table={}

	for i in range (0,len(vector_ent)):#Create the hash table

		hash_table[vector_ent[i]]=1

	for i in range(0,len(vector)):#Add elements to hash table

		a=hash_table[vector[i]]

		hash_table[vector[i]]=a+1

	lista_key=[]
	lista_amount=[]

	for i in range (0,len(hash_table)):#Get all the data from the hash table in to list

		lista_key.append(vector_ent[i])
		lista_amount.append(hash_table[vector_ent[i]])

	maximun=max(lista_amount)

	mode_list=[]#Create new list to store the modes in

	for i in range (0,len(lista_amount)):#Add elements to the mode list

		if maximun==lista_amount[i]:

			mode_list.append(lista_key[i])

	return min(mode_list)


def healthy():
	"""Test if the function is healthy"""

	v=[3,2,1,1,1,5,5]

	assert(mode(v)==1)

	v=[-3,-2,-1,-1,-1,-5,-5]

	assert(mode(v)==-1)

	v=["A","B"]

	assert(mode(v)==None)

	v=[1.1,1.2]

	assert(mode(v)==None)

	v=[]

	assert(mode(v)==None)


if __name__ == "__main__":
	
   healthy()





