# Write a Python code to calculate Permutation (5,3)
# importing math
import math

# initializing
n=5
r=n-3

num_factorial = math.factorial(n)
r_factorial= math.factorial(r)

# finding permutation
per = int(num_factorial/r_factorial)

# output
print(per)
