



def linear_sort(vector):

	a=max(vector)

	hash_table={}

	for i in range (0,a+1):#Create the hash table

		hash_table[i]=0

	for j in range(0,len(vector)-1):#Att elements to hash table

		print(vector[j])

		b=hash_table[(vector[j])]
		hash_table[vector[j]]=b+1

	sorted_lista=[]

	for k in range(0,a):

		for l in range(0,hash_table[k]):

			sorted_lista.append(k)

	return(sorted_lista)


print(linear_sort([43,23,24,43,43,65,754,543,324,5435]))

print(linear_sort([1,2,54,64,34,654,432,65,65,65,33,2,2,2]))







