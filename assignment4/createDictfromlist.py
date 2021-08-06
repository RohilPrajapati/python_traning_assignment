# Students = ['jack’,’jill’,’david’,’silva’,’ronaldo’]
# Marks = ['55’,’56’,’57’,’66’,’76’]

Students = ['jack','jill','david','silva','ronaldo']
Marks = ['55','56','57','66','76']
dict = {}
for i in range(0,5):
	dict.update({Students[i]:Marks[i]})

print(dict)