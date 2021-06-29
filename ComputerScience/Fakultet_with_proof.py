#Olof Nordenstorm Grundat21 inlaning uppgift 3.1

def Fakultet(n):#This is a function that make the produckt sum of an input and return it. It defiend for all postive whole nombers 
				# The functions is O(n)
				# It uses recusion to in order to multply all the numbers

	if type(n)==int:

		if n<0:
			print("This is not a valid input, since it is negativ")


		elif n==1:

			return n

		elif n == 0:

			return 1

		else:

			return n*Fakultet(int(n-1))
	else:
		print("This is not a valid input since is not a integer, returns None")
		return None


""""""
def healthy():
	"""This main function is only made for bug testing. I test postive, negativ numbers and zero. I also test an non int input.  """

	assert (Fakultet(4)==24)

	assert (Fakultet(0)==1)#Special cafe for Fakultet function is should return 1. Therefore it is good to extra check

	assert (Fakultet(-3)==None)
	
	assert (Fakultet("Grundat21")==None)

if __name__ == "__main__":
   healthy()

#Proof we test if Fakultet(0) is true. We see this in the code since if Fakultet(n=0)=1 whitch is true. 



#We assume that Fakultet(k) is true if all Fakultet(i) where i<k is true. Also assume that i and k are whole real numbers



#Our assumtions says Fakultet(i)=i!



#Lets say we want Fakultet(k) Then the algortim return Fakultet(i)*k. Where i is one less then k. Fakultet(i)=(k-1)! and since (k-1)!*k=k!. 



#The statement is true for any arbitary chosen k. And therefore the functions works by induction. Q.E.D








