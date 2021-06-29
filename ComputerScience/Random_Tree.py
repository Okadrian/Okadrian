#Olof Nordenstorm, grundat21, Treap_code

import random


class Treap(): # W(n)=(1)is the worst case complexity

	"""Here a random treap is implemented. The init function only definers that we got an empty treap with element size 0 since there is zero elements"""

	def __init__(self):

		self.__element_size = 0
		self.__root = None

	def AddNode(self,T): # W(n)=(log(n))is the worst case complexity
		"""Here we add elements to the treap. The treap elements are only added it there is no element like that element in hte treap"""
		if type(T)==str:


			if self.__root != None:

				self.__root = self._Advanced_Add_Treap(T,self.__root)

			else:

				self.__root = _Treap_Node(T)
				self.__element_size =self.__element_size+ 1
		else:

			print ("Not valid input. Input should not be of the  ",type(T), "It should be a string, Therefore nothing will be added")

			
	def _Advanced_Add_Treap(self,T,current_node):# W(n)=(log(n))is the worst case complexity
		"""There is three goal of this method, 
		1 make sure the node is not already in the treap if it do nothing
		2 add the node if it was not in the list
		3 make sure the treap is balanced with the random method.
		This will be achievied with the aid of recusion. The method will visit node, if the child node is the same as the one we want to add
		nothing will happen if. If it is not the same we will add a node. We will go through the entries of the treaps with a classical binarty 
		search algortim """
		#element size is only change in the add part of the fuctions. The add part is named. This make sure the element size is the true size of the tree
		if T < current_node._data:

			#Here we add the node if it got an empty space or do a recusion if it is not empty
			if current_node._left != None:#Add part

				current_node._left = self._Advanced_Add_Treap(T,current_node._left)


			else:

				self.__element_size =self.__element_size+ 1
				current_node._left = _Treap_Node(T)

				# Last we check the priority of the nodes to see if we should rotatete or not rotate the branch off the treap
			if current_node._prio<current_node._left._prio:

				tempo_1_node = current_node #We add a temporary node in order to store the data of the old upper one in the treap
				tempo_2_node = current_node._left #We create one more temporary node to store the left node
				current_node._left = None # We empty the old root
				tempo_1_node._left = tempo_2_node._right # we take the values off the old child and add it to the parent
				current_node=tempo_2_node # Make the new current node the old child
				current_node._right=tempo_1_node # Make the right node of that old the old parent with an added list of children of the the old child

		elif T > current_node._data:

			if current_node._right != None:#Add part

				current_node._right = self._Advanced_Add_Treap(T,current_node._right)

			else:

				self.__element_size =self.__element_size+ 1
				current_node._right = _Treap_Node(T)

			if current_node._prio<current_node._right._prio:

				tempo_1_node = current_node 
				tempo_2_node = current_node._right
				current_node._right = None 
				tempo_1_node._right = tempo_2_node._left
				current_node=tempo_2_node 
				current_node._left=tempo_1_node 

		return current_node

	def size(self):# W(n)=(1)is the worst case complexity

		"""Return the size of the treap"""

		return self.__element_size

	def string_in_order(self):# W(n)=(log(n))is the worst case complexity

		"""Enters the class and activate the method print in order. 
		I seperate the methods in order to use the private self.__root"""

		if self.__root!=None:

			string_list=self.get_data([],self.__root)

			string_list.sort()
			string_list=str(string_list).strip('[]')

			return string_list

		else:

			return "[]"

	def get_data(self,list_string,current_node):# W(n)=(log(n))is the worst case complexity
		"""The algoritim get data that string_in_order order"""
		if current_node!= None:

			self.get_data(list_string,current_node._left)

			list_string.append(current_node._data)

			self.get_data(list_string,current_node._right)

			return list_string

class _Treap_Node():

    """ Here nodes with a given value T is added, T should be a letter, The node can also have refences to the next element,  """

    def __init__(self,T):# W(n)=(1)is the worst case complexity

        self._prio = random.randint(0,10^5)
        self._data = T
        self._left = None
        self._right = None

        
def healthy():#W(n)=log(n)
	"""Make asserstion to check if the code works"""

	MyTreap=Treap()
	assert(MyTreap.size()==0)
	assert(MyTreap.string_in_order()=="[]")
	MyTreap.AddNode(3)

	#Test for diffrent letters 
	MyTreap.AddNode("A")
	MyTreap.AddNode("C")
	MyTreap.AddNode("B")
	MyTreap.AddNode("D")
	MyTreap.AddNode("F")
	MyTreap.AddNode("E")
	MyTreap.AddNode("Z")
	MyTreap.AddNode("X")
	MyTreap.AddNode("Q")
	MyTreap.AddNode("19")
	MyTreap.AddNode(5)
	MyTreap.AddNode(5.5)
	MyTreap.AddNode([5,"A"])

	#Size and string test
	assert(MyTreap.size()==10)
	assert(MyTreap.string_in_order()=="'19', 'A', 'B', 'C', 'D', 'E', 'F', 'Q', 'X', 'Z'")

	MyTreap.AddNode("WAOW")#Test to add long string
	print(MyTreap.size())
	#Size and string test
	assert(MyTreap.size()==11)
	assert(MyTreap.string_in_order()=="'19', 'A', 'B', 'C', 'D', 'E', 'F', 'Q', 'WAOW', 'X', 'Z'")




healthy()
