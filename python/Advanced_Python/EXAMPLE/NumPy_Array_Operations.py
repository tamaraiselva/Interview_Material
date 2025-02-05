import numpy as np

arr = np.arange(10)
arr[arr % 2 == 0] = -1
print(arr)
