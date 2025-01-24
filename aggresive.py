import pandas as pd
import numpy as np 
a = np.array([1,2])
x = np.repeat(a, [10643, 976], axis=0)
print(x)

b = np.array([1,2,3,4,1,2,3,4])
y = np.repeat(b,[1935,3416,2676,2616,183,275,230,288],axis=0)
print(y)
len(x)
len(y)
# Creating the Series
sr = pd.Series(x,y)

# Create the Index
index_ = [['Fmale', 'Male'],['Democrat','Independent','Republican']]

# set the index
sr.index = index_

# Print the series
print(sr)
# encode the values
result = sr.factorize()

# Print the result
print(result)
a = np.array([1,2])
x = np.repeat(a, [10643, 976], axis=0)
print(x)

b = np.array([1,2,3,4,1,2,3,4])
y = np.repeat(b,[1935,3416,2676,2616,183,275,230,288],axis=0)
print(y)
