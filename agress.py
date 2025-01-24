import numpy as np
from tabulate import tabulate


a = np.array([1,2])
x = np.repeat(a, [10643, 976], axis=0)
print(x)

b = np.array([1,2,3,4,1,2,3,4])
y = np.repeat(b,[1935,3416,2676,2616,183,275,230,288],axis=0)
print(y)


## create table
# assign data
mydata = [x,y]
# create header
head = ["x", "y"]
# display table
print(tabulate(mydata, headers=head))

from scipy.stats import chisquare
chisquare([x,y])
