
def spread(map,x,y):
	directions =[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
	for i, j in directions:
		if map[x+i][y+j] > 0:
			map[x+i][y+j] += 1

def next_day_set(map):
	length = len(map[0])
	for x in range(1,len(map) -1):
		for y in range(1,length -1):
			map[x][y] += 1

def check_energy(map,amount_of_flashes):
	flashed = False;
	length = len(map[0])
	for x in range(1,len(map) -1):
		for y in range(1,length -1):
			if map[x][y] > 9:
				flashed = True
				map[x][y] = 0
				amount_of_flashes += 1
				spread(map,x,y)
	return flashed, amount_of_flashes

#open file and create the map
with open("inputday11.txt") as file:
	lines =file.read().splitlines()
length = len(lines[0])
map = []
map.append([-1] * (length + 2))
for line in lines:
	numbers = []
	numbers.append(-1)
	for i in line:
		numbers.append(int(i))
	numbers.append(-1)
	map.append(numbers)
map.append([-1] * (length + 2))

#simulate the days
days = 100
amount_of_flashes = 0
for day in range(days):
	next_day_set(map)
	flashed = True
	while flashed:
		flashed, amount_of_flashes = check_energy(map, amount_of_flashes)
		
#print the map
for x in range(1,len(map)-1):
	for y in range(1,length+1):
		if map[x][y] == -1:
			print('x',end='')
		else:
			print((map[x][y]),end='')
	print()
print('amount of flashes after',day +1  , 'days:',amount_of_flashes)