# Olof Nordenstorm 2021 june 30


# The basic idea of naive bayes is too assume that all the probabilites are disjoint
# With this assumpstions the program will be run
# The data set for this machine learning code should be in the following form
# (X,Y) Where X a list and Y is the what answer the list should entail
# X could be a mail with words a element in the list. And Y could be if that mail is Spam or "Ham" (Not spam)
# Define also a list that include all X and Y Data=[[X1,Y1][X2,Y2][X3,Y3],...].

# For the training i use some simple list just to train my Machine learning skills
# Henry us the name of the person who get mails, These mail are just random but try to refelect some real scenario

def Naive_bayes(Data):

	M=len(Data)

	data_word=[]


	#Find all the words loop


	for i in range(0,M):


		for j in (Data[i][0]):


			if j not in data_word:

				data_word.append(j)


	#Create two empty list of probabilites


	prob_word_ham=[]
	prob_word_spam=[]


	# Create a two list with the probabilites of the two list. 


	for i in range(0,len(data_word)):

		prob_word_spam.append(0)
		prob_word_ham.append(0)


	###Naive bayes Sum


	for i in range(0,M):

		for j in range(0,len(Data[i][0])):

			for k in range(0,len(data_word)):

				if data_word[k]==Data[i][0][j]:

					if Data[i][1]=="Spam":

							prob_word_spam[k]=prob_word_spam[k]+1
					else:

							prob_word_ham[k]=prob_word_ham[k]+1


	###Naive bayes normalisation

	N=len(prob_word_spam)

	for i in range(0,len(prob_word_spam)):

		prob_word_spam[i]=float(prob_word_spam[i])/N
		prob_word_ham[i]=float(prob_word_ham[i])/N


	return(data_word,prob_word_ham,prob_word_spam)




def predict(mail,data_word,prob_word_ham,prob_word_spam):
	ham_X=0
	spam_X=0

	for i in X:

		for j in range (0,len(data_word)):

			if i==data_word[j]:

				ham_X=ham_X+prob_word_ham[j]
				spam_X=spam_X+prob_word_spam[j]



	if ham_X>spam_X:
		print(X)
		print("The mail is not spam")

	else:
		print(X)
		print("The mail is spam")
def test():

	X=["henry","eat","free","pizza","now"]


	A=[["this","is","epic","i","promise"],"Spam"]
	B=[["this","is","serious","now","henry"],"Ham"]
	C=[["henry","is","now","serious","sick"],"Ham"]
	D=[["you","have","won","a","epic","reward"],"Spam"]
	E=[["this","is","the","only","oportunity"],"Spam"]
	F=[["henry","you","need","to","finish"],"Ham"]
	G=[["free","pizza","is","epic","now"],"Spam"]
	H=[["eat","hamburgers","for","free","now"],"Spam"]
	J=[["henry","where","are","you","know"],"Ham"]



	Data=[A,B,C,D,E,F,G,H,J]

	D,PH,PS=Naive_bayes(Data)

	###Data has been collected and probabilites are calculated now we only need to classify a new entity what we have learnet.

	X=["henry","serious","sick","now","need","?"]
	predict(X,D,PH,PS)

	X=["epic","eat","free","pizza","now"]
	predict(X,D,PH,PS)


test()




