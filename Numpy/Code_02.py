import numpy as np
import time
import sys

# Practising numpy array efficiency, best use for processing a large amount of numbers

size = 10000

# Two python lists of numbers
l1 = range(size)
l2 = range(size)

# numpy arrays to compare the two lists above
a1 = np.arange(size)
a2 = np.arange(size)

# processing python list
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("python list took: ",(time.time()-start*10000)) # a way to measure the time this code block has taken

# processing numpy array
start = time.time()
result = a1 + a2
print("numpy took:", (time.time()-start)*10000)



