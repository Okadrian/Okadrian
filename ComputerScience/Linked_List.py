#Olof Nordenstorm Grundat21 inlaning uppgift 1.2, G och VG niva


class ListElement: # PRIVATE  The functions is W(1)
    """The goal of this class is to create node in a linked list. It has two inputs one for an element and one for a pointer that points on the next list"""
    def __init__(self,T=None,ListElement=None):
        """Defines the varibales"""
        self.__data=T
        self.__next=ListElement
    def return_data(self):
        """Return the element data. """
        return self.__data
    def return_next(self):
        """Returns the pointer"""
        return self.__next
    def change(self,T):
        """Changes the pointer to given input of T"""
        self.__next=T
    def is_class_member(self):
        """Return True"""
        return True


class LinkedList: # The functions is W(1)

    """ A singly linked list of elements of type T"""


    def __init__(self,first_element=None,last_element=None):
        """This is a private class, With two possible input one for the last and one for the first element in the list, 
        If nothing is added then the place will get filled up with none,
        The class implements a linked list and it also implements an healthy functions that test if the list is in good condidtion """
      
        self.__last = ListElement(last_element)
        self.__first = ListElement(first_element,self.__last)
        if first_element==None:
            self.__first=None
        if last_element==None:
            self.__last=None

        if first_element!=None:
            self.__size = int(1) # number of elements in list
            if last_element !=None:
                self.__size = int(2)
        else:
            self.__size=int(0)

    def addFirst(self,T):# The functions is W(1)
        """Add one element to the start of the list input is what the start should be"""
        new_element = ListElement(T,self.__first)
        self.__first=new_element
        self.__size=self.__size+1

    def addLast(self,T):# The functions is W(1)
        """Add one element to the end of the list and add one size to the list, input is what to end should be"""
        new_element=ListElement(T)

        if self.__last==None:
                self.__last=new_element
                self.__first.change(self.__last)
        else:
            self.__last.change(new_element)
            self.__last=new_element
        self.__size=self.__size+1



    def getFirst(self):# The functions is W(1)
        """Return the first element of the list, If there is no first return None"""
        if self.__first==None:
            return None
        if self.__first.return_data()!=None:
            data=self.__first.return_data()
            return self.__first.return_data()
        else:
            return None

    def getLast(self):# The functions is W(1)
        """Return the last value of the list, return None it the list is empty"""
    
        if self.__first==None:
            if self.__last==None:
                return None
        if self.__last.return_data()!=None:
            return self.__last.return_data()
        else:
            return None

    def get(self,T):#Get an index "T" value- The functions is W(n)
        """Return a certain value defineied in the list and if nothing exist in that place it should return None, 
        The input is the chosen place of the list you want to check  """

        if self.__first==None:
            if self.__last ==None:
                return None
        if self.__size==0:
            return None
        if T>self.__size:
            return None
        elif T<0:
            return None
        elif T==0:
            return self.__first.return_data()
        holder=self.__first.return_next()
        for j in range (1,self.__size):
            if j==T:
                return holder.return_data()
            holder=holder.return_next()

    def removeFirst(self):# The functions is W(1)
        """Remove the first element and return the removed value"""
        if self.__size==0:
            return None
        if self.__size==1:
            """This is what i think you wanted me to add <-----------------"""
            self.__first.change(None)
            self.__last=None
            return None
        value=self.__first.return_data()
        new_first=self.__first.return_next()
        self.__first=new_first
        self.__size=self.__size-1
        return value

    def clear(self):# The functions is W(1)
        """Remove all the elements in the list and set it size to zero"""

        self.__first=None
        self.__last=None
        self.__size=0


    def __size__(self):# The functions is W(1)
        """Return the size of the list"""

        return self.__size


    def string(self):# The functions is W(n)
        """ Has no input beyond self, return an string of the list elements with commas"""
        if self.__size==0:
            return "[]"
        list_string=[]
        element=self.__first.return_data()
        list_string.append(str(element))
        holder=self.__first.return_next()
        for i in range (1,self.__size):
            element=holder.return_data()
            holder=holder.return_next()
            list_string.append(str(element))
        list_string = ", ".join(list_string)
        list_string = ("[") + list_string + ("]")
        return list_string

    def healthy(self):# The functions is W(n)
        """This function is made to test if the list is working properly, The only input is the linked list, and then i run a series of test, 
        The test are if we got the right lentgh and if we got element in the beging and end. It return nothing, It test these thing by making
        assertments"""
        holder=self.__first
        """This is what i think you wanted me to add, This is the test code <-----------------"""
        if self.__size==0:
            assert (self.__first.return_next()==None)
            assert (self.__last==None)

        # Here i check if the function is of the right length
        m=0
        for i in range (0,self.__size):
            if holder.return_data()!=None:          
                m=m+1
                holder=holder.return_next()
            else:
                break
        assert (m==self.__size)
        if m==0:# Test if first and last is NONE. I use A=B=C=NONE
            assert (self.__first==self.__last)
            assert (self.__first==None)
        if m!=0:# Test that first is a member in the class
            assert (self.__first.is_class_member() == True)
            if m==1:# Test if we got only one member in list
                assert (self.__last == None)
            if m>1:# Test if we got a longer list then 1 Then the last element should be a member in the class and the refence arrow should be to None
                assert (self.__last.is_class_member() ==True)
                assert (self.__last.return_next()==None)




#Test code

def main():
    """This main function is made to test the function, W(n)"""
    """ I create a list with 1 and 2 as element and test length of the list. Before doing so i add an element to the first and last place"""
    L=LinkedList(1,2)#Data of type T
    L.addFirst(0)
    L.addLast(3)
    assert L.__size__()==4
    # Renove the first element, add one called first and one called last and try if we get the right size of the list still
    L.removeFirst()
    L.addFirst("first")
    L.addLast("last")
    assert L.__size__()==5
    # Assert that the first and last element is correct. With function that collect the last and first value
    assert L.getFirst()=="first"
    assert L.getLast()=="last"
    # Assert to chech what happens if we try to get element that dont exist and generic place in the list
    assert L.get(7)==None
    assert L.get(2)==2
    # Chech so the string functions work. Its suppose to return a string with a certain strucure to the user
    assert L.string()=="[first, 1, 2, 3, last]"
    # I use a function that is called healty to do one extra generall test
    L.healthy()
    #I empty the list
    L.clear()
    # I test all the methods so that they work on the empty list
    assert L.get(0)==None
    assert L.__size__()==0
    assert L.getFirst()==None
    assert L.getLast()==None
    assert L.removeFirst()==None
    assert L.string()=="[]"
    L.addFirst(3)
    assert L.__size__()==1
    assert L.string()=="[3]"

    L.removeFirst()
    L.healthy()
    N=LinkedList(1,2)
    N.removeFirst()
    N.removeFirst()
    N.healthy()



main()

