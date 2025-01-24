# Import necessary libraries
import numpy as np
from tabulate import tabulate
from scipy.stats import chisquare

# Section 1: Generate repeated arrays
print("Generating repeated arrays...")

# Array `a` with repeat counts
a = np.array([1, 2])
x = np.repeat(a, [10643, 976], axis=0)
print("Array x:")
print(x)

# Array `b` with repeat counts
b = np.array([1, 2, 3, 4, 1, 2, 3, 4])
y = np.repeat(b, [1935, 3416, 2676, 2616, 183, 275, 230, 288], axis=0)
print("Array y:")
print(y)

# Section 2: Create a table with the data
print("\nCreating table...")
# Assign data
mydata = [[val] for val in [x, y]]  # Ensure the structure is column-wise for tabulate
# Create header
headers = ["x", "y"]
# Display the table
print("Data table:")
print(tabulate(mydata, headers=headers, tablefmt="grid"))

# Section 3: Perform Chi-Square Test
print("\nPerforming Chi-Square Test...")
chi2_result = chisquare([len(x), len(y)])  # Chi-square test on lengths of x and y
print("Chi-Square Test Result:")
print(chi2_result)
