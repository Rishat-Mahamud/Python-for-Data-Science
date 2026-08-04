import numpy as np

arr_2d = np. array([[1,2,3,4],[5,6,7,8]])
print(arr_2d)

new_2d_arr = np.delete(arr_2d,0,axis=0)#1 for colm wise and 0 for row wise
print(new_2d_arr)