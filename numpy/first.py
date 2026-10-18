# Numpy
# Numerical python
# python library
# AI,ML,D

#  numpy gets access to numpy array - increase the spead , for numerical operatior

import numpy as np

# print(np.__version__)

# --------------------------------------------------------

# list and array

my_list = [1, 2, 3, 4]
my_list = my_list * 2  # [1,2,3,4,1,2,3,4]  --> duplicates all the elements 

# print(my_list) 

#  in list we need to use map or for looop for to doubling the elements 

#using traditional for loop
# numbers = [1, 2, 3, 4]
# doubled = []

# for x in numbers:
#     doubled.append(x * 2)

# print(doubled)  
#  Output: [2, 4, 6, 8]

# using  for comprehension
# numbers = [1, 2, 3, 4]
# doubled = [x * 2 for x in numbers]

# print(doubled)  # Output: [2, 4, 6, 8]
# numbers = [1, 2, 3, 4]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)  
#  Output: [2, 4, 6, 8]


#using numpy array
array=np.array([1,2,3,4]) 
array=array*2 #[[2 4 6 8]] 
print(array)



