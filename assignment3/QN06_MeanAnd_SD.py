# Calculate the mean and standard deviation of the following list:
# Numbers = [1,2,3,5,88,99,55,33,41,52]

from math import *

Numbers = [1,2,3,5,88,99,55,33,41,52]

N = len(Numbers)
total = sum(Numbers)

mean = total/N

# output for mean
print(mean)

# for standar deviation

x_sub_mean=[]

for x in Numbers:
	x_sub_mean.append(x-mean)

print(x_sub_mean)
total = sum(x_sub_mean)
print(total)
total = total**2

SD= sqrt(total/N)
print(float(SD))