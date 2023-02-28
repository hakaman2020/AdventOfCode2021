def current_stats(pos, depth, aim):
	print(pos," ", depth," ", aim, "\n")


position = 0
depth = 0
aim = 0

with open("inputday2.txt") as file:
	lines = file.readlines()
for x in lines:
	linesplit = x.split()
	if linesplit[0] == 'forward':
		position += int(linesplit[1])
		depth += (aim * int(linesplit[1]))
	elif linesplit[0] == 'down':
		aim += int(linesplit[1])
	elif linesplit[0] == 'up':
		aim -= int(linesplit[1])
	current_stats(position, depth, aim)
print('depth is ', depth, 'and position is ', position,'product is ', depth * position)