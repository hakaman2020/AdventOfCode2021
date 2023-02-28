# using the with will open the file and close it
count = 0
with open('test.txt') as f:
	line = f.readline()
	prev_number = int(line)
	line = f.readline()
	next_number = int(line)
	while line != '':
		if (prev_number < next_number):
			count+=1
		prev_number = next_number
		line = f.readline()
		if (line != ''):
			next_number = int(line)
print(count)
