# Write a Python code to calculate Combination (15,3)

# importing math
import math

# initializing
n = 15
r=3
nr= n-r

n = math.factorial(n)   #factorial of n
r = math.factorial(r)   # factorial of r
nr= math.factorial(nr)  # factorial of nr

# formula of combination
comb=int(n/(r*(nr)))

# output
print(comb)
