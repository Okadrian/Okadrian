def swap(vector, pos1, pos2):
	"""Simply swaps two places in a list and returns it"""
	vector[pos1], vector[pos2] = vector[pos2], vector[pos1]
	return vector

def linear_sort(vector):
	"""Sort a list in element smaller then 0 and elements bigger then zero. Does this in worst case time of W(n)"""


	if type(vector) is not list:#Test for propper input
		print( str(vector) +" Is not a list the function will return None")
		return None

	if len(vector)==0:#Test for propper input
		print("The list is empty return None")
		return None


	for i in range (0,len(vector)):#Test for propper input
		if isinstance(vector[i], float)==False and isinstance(vector[i], int)==False:

			print("The list is not only numbers "+str(vector[i])+ " That is in the place " + str(i) + " Is not a number. Numbers need to be written in int or float form")
			print("The function will return None")

			return(None)

	#Defines low, mid and len of list
	low, end = 0, len(vector)
	mid = 0


	# We got the following statement as the end of the loop.
	# vector[:low]<0
	# vector[low:mid]=0
	# vector[end:]>0
	# vector[end:] > 0

	# In the loop the place we are looking at is called mid. The program order the list by swapping mid with low or end-1.
	# If postive it swap with end-1 if low it swaps with mid. If the element is zero it leaves it be. 
	# As the loops loops we got an invariant statement about order. The list is always ordererd to the left of ele.
	# As the loops ends we got the statement mentioned before is true. 
	if type(vector)!=list:

		return(None)

	while mid < end:
		ele=vector[mid]

		if ele<0:

			swap(vector,low,mid)
			low=low+1
			mid=mid+1
			
		if ele==0:

			mid=mid+1

		if ele>0:

			swap(vector,mid,end-1)
			end=end-1


	return vector

def healthy():
	"""Test if the function is healthy"""
	v=[-3,5,0,-5,3,3-7,0]

	v=(linear_sort(v))

	assert(v==[-3, -5, -4, 0, 0, 3, 5])

	v=["A","C","D"]

	assert(linear_sort(v)==None)

	v=[5.1,-4.1,3.1,-2.1,1.1,0,-1.1,2.1,-3,1.,-4.1,5,1]

	v=linear_sort(v)

	assert(v==[-4.1, -4.1, -3, -2.1, -1.1, 0, 2.1, 1.1, 1.0, 3.1, 5, 1, 5.1])

	v=5

	assert(linear_sort(v)==None)

	v=[]

	assert(linear_sort(v)==None)


if __name__ == "__main__":
   healthy()





