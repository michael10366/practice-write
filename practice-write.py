#practice write

data =[]
	
for i in range(1 ,100, 2):
	data.append(i)
print(data)

with open('test.txt', 'w') as f:
	for d in data:
		f.write(str(d) + '\n')
