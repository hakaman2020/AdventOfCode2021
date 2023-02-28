#this was an in process program in which I tried to get the solution through recursion
#but I couldn't get it to work so I changed to a different approach. 
def process_line(line,cp,part):
	if line[cp] == '[':
		cp += 1
		list = []
		first, cp = process_line(line,cp,1)
		if len(first) == 1:
			first = first[0]
		list.append(first)
		cp += 1
		second, cp = process_line(line,cp,2)
		if len(second) == 1:
			second = second[0]
		list.append(second)
		cp +=1
		return list, cp
	else:
		if part == 1:
			sep = ','
		else:
			sep = ']'
		number = line[cp:].split(sep,maxsplit=1)[0]
		cp += len(number)
		return [int(number)], cp

def addition(number1, number2):
	list = []
	list.append(number1)
	list.append(number2)
	return list

def explode(list,level,lvalue,rvalue,exploded):
	if level == 5:
		print('explode')
		return list[0], list[2], True
	#first part
	if len(list[0]) == 2:
		lvalue, rvalue, exploded = explode(list[0],level + 1, lvalue, rvalue, exploded)
		if lvalue != 0 and rvalue != 0 and exploded:
			print(lvalue)
	#second part
	if len(list[1]) == 2:
		lvalue, rvalue, exploded = explode(list[1],level + 1, lvalue, rvalue, exploded)
	return lvalue, rvalue, exploded
	


with open('/home/hakaman/projects/aoc/day18/test.txt') as file:
	lines = file.read().splitlines()

numbers = []
for line in lines:
 	numbers.append(process_line(line,0,1)[0])
print(numbers)

sum = []
for number in numbers:
	if sum ==[]:
		sum= number
	else:
		sum = addition(sum, number)
	print(sum)
print(sum)