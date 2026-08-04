"""
np.split() for equal array
np.hsplit() for horizontal
np.vsplit() for vartically
"""
from os.path import split

import numpy as np

arr = np.array([10,20,30,40,5,6])
print(np.split(arr,2))
print(np.hsplit(arr,2))