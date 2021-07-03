# Ask enter to enter two numbers (say, a and b). Generate two random numbers between those two numbers and find a combination of these two newly generated random numbers.

# formula for combination is c = n!/r!(n-r)!


import math         # importing math module
import random       # importing random module
# taking input from user
a= int(input("Enter the starting number"))
b= int(input("Enter the ending number"))

# generating random number

num1= random.randint(a,b)
num2 = random.randint(a,b)

# factorizing the number
num1fac= math.factorial(num1)       # n!
num2fac= math.factorial(num2)       # r!

# testing
print(num1)
print(num2)

# swaping the value if the num1 is smaller then num2
if num1<num2:
    num1,num2=num2,num1

# (n-r)
subnum=num1-num2

# factorizing the subnum -- (n-r)!
subnum2fac = math.factorial(subnum)

# combination formula
comb=int(num1fac/(num2fac*(subnum2fac)))

# output
print(comb)
