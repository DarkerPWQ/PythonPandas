# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([1,3,4,np.nan,6,8,"pwq"])
print s
df3 = pd.DataFrame(np.random.randn(10,5),index = ['a', 'b', 'c', 'd', 'e','a', 'b', 'c', 'd', 'e'],columns=['a', 'b', 'c', 'd', 'e'])#colums理解为字段名称，根据实战测试，必须要对应长度，不然报错
print df3
# arr1 = np.random.randn(2,4)
# print(arr1)
# print('******************************************************************')
# arr2 = np.random.rand(2,4)
# print(arr2)
# d = np.arange(8)#创建一个数字列表list
# print d
#
# dates = pd.date_range('20130101', periods=6)
# print dates

