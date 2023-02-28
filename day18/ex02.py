def explode(numbers, levels):
	amount_numbers = len(numbers)
	i = 0
	exploded = False
	while i < amount_numbers and not exploded:
		if levels[i] == 5:
			lvalue = numbers[i]
			rvalue = numbers[i + 1]
			if i != 0:
				numbers[i-1] += lvalue
			if i != amount_numbers - 2:
				numbers[i + 2] += rvalue 
			numbers[i + 1] = 0
			levels[i +1 ] -= 1
			del numbers[i]
			del levels[i]
			exploded = True
		i += 1
	return exploded

def split(numbers, levels):
	amount_numbers = len(numbers)
	i = 0
	splitted = False
	while i < amount_numbers and not splitted:
		if numbers[i] > 9:
			lvalue = numbers[i] // 2
			rvalue = numbers[i] - lvalue
			new_level = levels[i] + 1
			numbers[i] = rvalue
			levels[i] = new_level
			numbers.insert(i,lvalue)
			levels.insert(i,new_level)
			splitted = True
		i += 1
	return splitted

def addition(numbers1,levels1, numbers2,levels2):
	numbers = numbers1 + numbers2
	levels = levels1 + levels2
	for i in range(len(levels)):
		levels[i] += 1
	return numbers, levels

def build_numbers(line, numbers, levels):
	level = 0
	number = 0
	for c in line:
		if c == '[':
			level += 1
		elif c == ',':
			continue
		elif c == ']':
			level -= 1
		else:
			numbers.append(int(c))
			levels.append(level)

def reduce(numbers, levels):
	done = False
	while not done:
		exploded = True
		while exploded:
			exploded = explode(numbers,levels)
		splitted = split(numbers,levels)
		if not exploded and not splitted:
			done = True		


def reduce_mag(numbers, levels, level):
	amount_numbers = len(numbers)
	i = 0
	while i < amount_numbers:
		if levels[i] == level and levels[i+1] == level:
			lvalue = numbers[i]
			rvalue = numbers[i +1]
			numbers[i+1] = 3* lvalue + 2 * rvalue
			levels[i + 1] -= 1
			del numbers[i]
			del levels[i]
			amount_numbers -= 1
		i += 1

def calc_magnitude(numbers, levels):
	magnitude = 0
	highest_level = max(levels)
	levels_copy = levels.copy()
	numbers_copy = numbers.copy()
	if highest_level > 1:
		for i in range(highest_level,1,-1):
			reduce_mag(numbers_copy, levels_copy, i)
	magnitude = 3* numbers_copy[0] + 2 * numbers_copy[1]
	return magnitude

with open('/home/hakaman/projects/aoc/day18/inputday18.txt') as file:
	lines = file.read().splitlines()

list_numbers = []
list_levels = []

for line in lines:
	numbers = []
	levels = []
	build_numbers(line, numbers,levels)
	list_numbers.append(numbers)
	list_levels.append(levels)

# for i in range(len(list_numbers)):
# 	print(list_numbers[i])
# 	print(list_levels[i])
# 	print()
amount_numbers = len(list_numbers)
print(amount_numbers)

highest_magnitude = -1

for i in range(amount_numbers):
	first_numbers = list_numbers[i]
	first_levels = list_levels[i]
	for j in range(amount_numbers):
		if j != i:
			current_sum, current_levels = addition(first_numbers,first_levels,list_numbers[j],list_levels[j])
			reduce(current_sum, current_levels)
			current_magnitude = calc_magnitude(current_sum, current_levels)
			if current_magnitude > highest_magnitude:
				highest_magnitude = current_magnitude

print(highest_magnitude)


# current_sum = list_numbers[0]
# current_levels = list_levels[0]
# for i in range(1, len(list_numbers)):
# 	current_sum, current_levels = addition(current_sum,current_levels,list_numbers[i],list_levels[i])
# 	reduce(current_sum,current_levels)

# print(current_sum)
# print(current_levels)

# print(calc_magnitude(current_sum, current_levels))