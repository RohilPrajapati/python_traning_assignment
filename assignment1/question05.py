# Write a Python code to calculate LCM of (25,55)
a=25
b=25

# choose highest number:
if a>b:
    high=a
else:
    high=b

while True:
    if ((high%a==0) and (high%b==0)):
        lms= high
        break
    high+=1

# output
print(lms)
