def calculate_size(map, mark_map,x,y):
	max_x = len(map)
	max_y = len(map[0])
	mark_map[x][y] += 1
	if map[x][y] == 9:
		return 0
	size = 1
	directions = determine_directions(map,max_x,max_y,x,y)
	for i, j in directions:
		if mark_map[x+i][y+j] == 0:
			size += calculate_size(map, mark_map, x + i, y + j)
	return size

def determine_directions(map,max_x,max_y,x,y):
	directions =[]
	if x - 1 >= 0:
		directions.append((-1,0))
	if x + 1 < max_x:
		directions.append((1,0))
	if y - 1 >= 0:
		directions.append((0,-1))
	if y + 1 < max_y:
		directions.append((0,1))
	return directions

with open('inputday9.txt') as f:
	lines = f.readlines()
length = len(lines[0]) - 1

# create map
map = []
count = 0
for line in lines:
	count += 1
	mapline = []
	for y in range(length):
		mapline.append(int(line[y]))
	map.append(mapline)

#create mark_map
mark_map = []
for line in range(count):
	mark_map.append([0] * length)

#search for low points and calculate basin size
size_basins = []
for x in range(count):
	for y in range(length):
		low_point = True
		directions = determine_directions(map,count,length,x,y)
		for i,j in directions:
			if map[x + i][y + j] <= map[x][y]:
				low_point = False
		if low_point == True:
			size_basins.append(calculate_size(map,mark_map,x,y))
size_basins.sort(reverse=True)
print( size_basins[0] * size_basins[1] * size_basins[2])