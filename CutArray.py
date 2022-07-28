import numpy as np
##Half Array
def halfArray(Ary):
    if Ary.shape[0]%2!=0:
        raise TypeError("Array shape should be Even")
    res=np.reshape(Ary,(2,int(Ary.shape[0]/2)))
    return res
A=np.array([1,2,3,4,5,6,2,2,4,5])
print(halfArray(A))
