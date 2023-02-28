with open('inputday10.txt') as f:
	lines = f.read().splitlines()
errors = []
score = 0

active_delim = '()[]{}<>'
for line in lines:
	delimiters = []
	for delim in line:
		#print('current ', delim)
		if delim in '{<([':
			delimiters.insert(0,delim)
		else:
			if delim != active_delim[active_delim.index(delimiters[0]) + 1]:
				errors.append(delim)
				if delim == ')':
					score += 3
				elif delim == ']':
					score += 57
				elif delim == '}':
					score += 1197
				elif delim == '>' :
					score += 25137
				break
			else:
				del delimiters[0]
print(errors)
print(score)		