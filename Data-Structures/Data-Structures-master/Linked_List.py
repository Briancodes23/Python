
#Implementing the node class data structure
#Sub class of the Linked List wont be used by user
class node:
    def _init_(self,data=None):
        self.data = data
        self.next = None

class linked list:
      def_init_ (self):
      self.head = node()

#Adding a new data point at the end of the list using the append function
def append(self, data):
    new_node = node(data)
    cur = self.head #Creating a variable to store the node we are currently looking at
    while cur.next != None: #itrating while the next element of the current node is not equal to none
        cur = cur.next
    cur.next = new_node #at the last element of the list, so setting the last node to the new_node


#A function to find the length of the linked list & useful to find the size of the data structure
def length(self):
    cur = self.head #another node to point to the current node and set to head
    total = 0
    while cur.next != None: #iterating the nodes
        total += 1 #incrementing the total by one
        cur = cur.next
    return total


#A function to show the current contents of the list & to test the length and append functions
def display(self):
    elems = []              #list of elements seen
    cur_node = self.head   #Setting a current node for the variable looking at
    while cur_node.next != None:
    cur_node = cur_node.next
    elems.append(cur_node.data)  #appending the data of the current node to list of elements(elems) seen
print elems

my_list = linked_list()

my_list.display()

my_list.append(1)
my_list.append(2)

my_list.display()


#An extractor function to pull out a datapoint at a certain index from the linkedlist
def get (self,index): #pass in the index in which we want to extract the data from
    if index >= self.data(): #checking the index the user passed is not out of the range of the linked list, using conditions
       print "ERROR: 'GET' Index out of range!"
       return None

    cur_idx = 0             #variable to contain the index looking at
    cur_node = self.head    #variable to contain the node looking at
    while True:
        cur_node = cur _node.next
        if cur_idx == index: return cur_ node.data  #if the current node is equal to the index provided by the user, then i know i'm at the datapoint to extract
        cur_idx += 1                                 #otherwise incrementing the current index by one


#To ensure the new get function is working properly
my_list = linked list()

my_list.append(1) #appending/adding on data
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display.()

print "element at 2nd index: %d" & my_list.get(2)


#An erase function to erase a node at a certain provided index
def erase(self,index):
    if index >= self.length(): #checking the index the user provided is not longer than the actual linked list already have
       print "ERROR: 'Erase'  Index out of range!"
       return
    cur_idx = 0
    cur_node = self.head
    while True:
        last_node = cur_node  #saving the current node as the last node
        cur_node = cur_node.next
    if cur_idx == index:      #checking the program is at the index the user provided
    last_node.next = cur_node.next
    return
    cur_idx += 1              #if not at the current node the user provided will be incrementing the current index by 1

my_list = linked_list()

my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

my_list.erase(1)

my_list.display()











