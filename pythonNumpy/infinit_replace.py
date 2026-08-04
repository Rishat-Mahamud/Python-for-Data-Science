#np.isinf(array)10^1000
#1/0

import numpy as np

arr = np.array([4,8,np.inf,5,-np.inf,6])
print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr,posinf=3000,neginf=-10000)
print(cleaned_arr)