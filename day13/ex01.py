def count_dots(paper):
	col = len(paper[0])
	row = len(paper)
	count = 0
	for i in range(row):
		for j in range(col):
			if paper[i][j] == '*':
				count += 1
	return count

def fold(paper,axis,number):
	col = len(paper[0])
	row = len(paper)

	folded_paper = []
	if axis == 'y':
		for i in range(row//2):
			folded_paper.append(['.'] * col)
		for y in range(row//2):
			for x in range(col):
				folded_paper[y][x] = paper[y][x]
		for y in range(1,row//2+1):
			for x in range(col):
				if paper[number+y][x] == '*':
		 			folded_paper[number-y][x] = paper[number+y][x]
	elif axis == 'x':
		for i in range(row):
			folded_paper.append(['.'] * (col //2))
		for y in range(row):
			for x in range(col//2):
				folded_paper[y][x] = paper[y][x]
		for y in range(row):
			for x in range(1,col//2 +1):
				if paper[y][number + x] == '*':
					folded_paper[y][number-x] = paper[y][number+x]

	return folded_paper

def print_paper(paper):
	for y in range(len(paper)):
		for x in range(len(paper[0])):
			if paper[y][x] == '*':
				print(paper[y][x],end='')
			else:
				print(' ',end='')
		print()

with open('inputday13.txt') as file:
	lines = file.read().splitlines()
dots =[]
folds = []
max_x = 0
max_y = 0
for line in lines:
	if line != '':
		if line[0].isdigit():
			x,y = line.split(',')
			x = int(x)
			y = int(y)
			if x > max_x:
				max_x = x
			if y > max_y:
				max_y = y
			dots.append((x,y))
		elif line[0].isalpha():
			axis, number = line.split('=')
			folds.append((axis[-1],int(number)))
#the folding is done always in half
#first fold is 655 thus the max_x = 655 * 2 = 1310
#second fold is 447 thus the max_y = 447 * 2 = 894
max_x = 1310
max_y = 894
paper =[]
for i in range(max_y+1):
 	paper.append(['.']*(max_x+1))

for x, y in dots:
	paper[y][x] = '*'
first_fold = True
for axis, number in folds:
	paper = fold(paper, axis, number)
	if first_fold:
		first_fold = False
		print('count dots after first fold:',count_dots(paper))
print('folded paper after the folds:')
print_paper(paper)
