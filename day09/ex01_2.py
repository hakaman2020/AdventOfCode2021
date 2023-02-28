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

risk = 0
#search for low points
for x in range(count):
	for y in range(length):
		low_point = True
		directions = determine_directions(map,count,length,x,y)
		for i,j in directions:
			if map[x + i][y + j] <= map[x][y]:
				low_point = False
		if low_point == True:
			risk += map[x][y] + 1
print(risk)


		