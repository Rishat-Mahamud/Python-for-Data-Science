"""
reshape(row,col) specify new shape
if dimension match


"""
import numpy as np
from numpy.ma.core import reshape

arr = np.array([1,2,34,5,6,7])
reshape_arr = arr.reshape(2,3)
print(reshape_arr)