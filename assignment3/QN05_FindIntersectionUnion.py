# A = [‘a’,’b’,’c’,’d’] B = [‘1’,’a’,’2’,’b’]
# Find  and 

# given list
A = ['a','b','c','d'] 
B = ['1','a','2','b']

# new list for storing union and intersection
union = []
intersection = []

# finding union and storing it to union list
for a in A:
	if a not in union:
		union.append(a)
for b in B:
	if b not in union:
		union.append(b)
print(union)

# finding intersection and storing it to intersection list
for a in A:
	for b in B:
		if a == b:
			intersection.append(a)

# output for intersection
print(intersection)
