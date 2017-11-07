import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([1,3,4,np.nan,6,8,"pwq"])
print s
df3 = pd.DataFrame(np.random.randn(10,5),columns=['a', 'b', 'c', 'd', 'e'])
print df3
# arr1 = np.random.randn(2,4)
# print(arr1)
# print('******************************************************************')
# arr2 = np.random.rand(2,4)
# print(arr2)
d = np.arange(8)
print d
