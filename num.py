import numpy as np
import time
arr=np.array([1,2,3])
start=time.time()
arr*2
end=time.time()
print(arr,-start+end)

start2=time.time()
for i in range(len(arr)):
    arr[i]*=2
end2=time.time()
print (arr,-start2+end2)