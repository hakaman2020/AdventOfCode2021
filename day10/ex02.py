with open('inputday10.txt') as f:
	lines = f.read().splitlines()
error_lines =[]
active_delim = '()[]{}<>'
for line in lines:
	delimiters = []
	for delim in line:
		if delim in '{<([':
			delimiters.insert(0,delim)
		else:
			if delim != active_delim[active_delim.index(delimiters[0]) + 1]:
				error_lines.append(line)
				break
			else:
				del delimiters[0]
for x in error_lines:
	lines.remove(x)
scores = []
for line in lines:
	delimiters =[]
	for delim in line:
		if delim in '{<([':
			delimiters.insert(0,delim)
		else:
			del delimiters[0]
	score = 0
	for delim in delimiters:
		score *= 5
		score += "([{<".index(delim) + 1
	scores.append(score)
print(scores)
scores.sort()
print(scores[int(len(scores)/2)])