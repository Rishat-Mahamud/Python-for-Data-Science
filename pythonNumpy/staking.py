"""
vstack() for row wise
hstack() for colm wise
"""
import numpy as np

arr_1 = np.array([10,20,30,40])
arr_2 = np.array([90,98,97,9])
print(np.vstack((arr_1,arr_2)))
print(np.hstack((arr_1,arr_2)))