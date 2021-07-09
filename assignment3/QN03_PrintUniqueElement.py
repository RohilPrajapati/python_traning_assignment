# Print all the unique elements in the following list 
# fifa = ['Italy','Argentina','Germany','Brazil','France','Brazil','Italy','Spain','Germany','France']


# given list
fifa = ['Italy','Argentina','Germany','Brazil','France','Brazil','Italy','Spain','Germany','France']

# if u want alphabetical order if not comment it out
fifa.sort()

# creating new list to add the unique country
uniqueFifa=[]

# scan the fifa list and inserting it to uniqueFifa list
for country in fifa:
	if country is not uniqueFifa:
		uniqueFifa.append(country)

# output
print(uniqueFifa)