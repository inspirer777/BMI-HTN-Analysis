# Import necessary libraries
import numpy as np
import pandas as pd
from tabulate import tabulate
from scipy.stats import chisquare, chi2_contingency

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
mydata = [x, y]
# Create header
headers = ["x", "y"]
# Display the table
print("Data table:")
print(tabulate(mydata, headers=headers, tablefmt="grid"))

# Section 3: Perform Chi-Square Test (1D array)
print("\nPerforming Chi-Square Test (1D)...")
chi2_result = chisquare(x)
print("Chi-Square Test Result (x):")
print(chi2_result)

# Section 4: DataFrames for Chi-Square Contingency Test
print("\nCreating DataFrames...")
x_df = pd.DataFrame({
    "id": [1, 2],
    "times": [10643, 976]
})
print("DataFrame x:")
print(x_df)

y_df = pd.DataFrame({
    "i": [1, 2, 3, 4, 1, 2, 3, 4],
    "t": [1935, 3416, 2676, 2616, 183, 275, 230, 288]
})
print("DataFrame y:")
print(y_df)

# Section 5: Chi-Square Contingency Test
print("\nPerforming Chi-Square Contingency Test...")
chi2_contingency_result = chi2_contingency(y_df, correction=True, lambda_=None)
print("Chi-Square Contingency Test Result:")
print(chi2_contingency_result)
