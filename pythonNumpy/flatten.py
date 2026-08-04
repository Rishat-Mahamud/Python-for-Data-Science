"""
.ravel() -> view
.flatten()->copy
"""
import numpy as np


arr_2d = np.array([[1,2,3,4,5], [4,5,6,7,7]])
print(arr_2d.flatten())
print(arr_2d.ravel())
