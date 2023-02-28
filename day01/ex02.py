# using the with will open the file and close it
count = 0
with open('input.txt') as f:
	line = f.readline()
	first = int(line)
	line = f.readline()
	second = int(line)
	line = f.readline()
	third = int(line)
	total1 = first + second + third
	line = f.readline()
	while line != '':
		fourth = int(line)
		total2 = second + third + fourth
		if (total1 < total2):
			count += 1
		line = f.readline()
		if (line != ''):
			second, third = third, fourth
			third = fourth
			total1 = total2
print(count)
