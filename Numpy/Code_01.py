import numpy as np
import time
import sys

# Creating a list which has 1000 elements
l = range(1000)
print(sys.getsizeof(10)*len(1)) # printing the size of the list

#Creating a numpy array specifying the size
array = np.arange(1000)
print(array.size*array.item)
