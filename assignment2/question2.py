# Write a program to calculate direction and magnitude of the vector described by the following points.
# A = (20,30)
# B = (30,40)

from math import *

A=(20,30)
B=(30,40)

# magnitude operation

mag = sqrt(((B[0]-A[0])**2)+((B[1]-A[1])**2))
print(mag)

# directive operation

direct = degrees(atan((B[1]-A[1])/(B[0]-A[0])))
print(direct)
