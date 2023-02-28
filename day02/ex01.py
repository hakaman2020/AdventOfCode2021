position = 0
depth = 0

with open("inputday2.txt") as file:
	lines = file.readlines()
for x in lines:
	linesplit = x.split()
	if linesplit[0] == 'forward':
		position += int(linesplit[1])
	elif linesplit[0] == 'down':
		depth += int(linesplit[1])
	elif linesplit[0] == 'up':
		depth -= int(linesplit[1])
print('depth is ', depth, 'and position is ', position,'product is ', depth * position)