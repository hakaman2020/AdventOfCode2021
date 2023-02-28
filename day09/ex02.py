def calculate_size(map,x,y,test_map):
		length = len(map[0])
		width = len(map)
		if map[x][y] == 9:
			return 0
		center = map[x][y] 
		test_map[x][y] +=1
		size = 1
		#corners
		if x == 0 and y == 0:
			if center < map[x+1][y] and test_map[x+1][y] == 0:
				size += calculate_size(map,x+1,y,test_map)
			if center < map[x][y+1] and test_map[x][y+1] == 0:
				size += calculate_size(map,x,y+1,test_map)
		elif x == 0 and y == length -1:
			if center < map[x][y-1] and test_map[x][y-1] == 0:
				size += calculate_size(map,x,y-1,test_map)
			if center < map[x+1][y] and test_map[x+1][y] == 0:
				size += calculate_size(map,x+1,y,test_map)
		elif x == width -1 and y == 0:
			if center < map[x-1][y] and test_map[x-1][y] == 0:
				size += calculate_size(map,x-1,y,test_map)
			if center < map[x][y+1] and test_map[x][y+1] == 0:
				size += calculate_size(map,x,y+1,test_map)
		elif x == width -1 and y == length -1:
			if center < map[x-1][y] and test_map[x-1][y] == 0:
				size += calculate_size(map,x-1,y,test_map)
			if center < map[x][y-1] and test_map[x][y-1] == 0:
				size += calculate_size(map,x,y-1,test_map)
		#sides
		elif x == 0:
			if center < map[x+1][y] and test_map[x+1][y] == 0:
				size += calculate_size(map,x+1,y,test_map)
			if center < map[x][y-1] and test_map[x][y-1] == 0:
				size += calculate_size(map,x,y-1,test_map)
			if center < map[x][y+1] and test_map[x][y+1] == 0:
				size += calculate_size(map,x,y+1,test_map)
		elif x == width - 1:
			if center < map[x-1][y] and test_map[x-1][y] == 0:
				size += calculate_size(map,x-1,y,test_map)
			if center < map[x][y-1] and test_map[x][y-1] == 0:
				size += calculate_size(map,x,y-1,test_map)
			if center < map[x][y+1] and test_map[x][y+1] == 0:
				size += calculate_size(map,x,y+1,test_map)
		elif y == 0:
			if center < map[x][y+1] and test_map[x][y+1] == 0:
				size += calculate_size(map,x,y+1,test_map)
			if center < map[x-1][y] and test_map[x-1][y] == 0:
				size += calculate_size(map,x-1,y,test_map)
			if center < map[x+1][y] and test_map[x-1][y] == 0:
				size += calculate_size(map,x+1,y,test_map)
		elif y == length -1:
			if center < map[x][y-1] and test_map[x][y-1] == 0:
				size += calculate_size(map,x,y-1,test_map)
			if center < map[x-1][y] and test_map[x-1][y] == 0:
				size += calculate_size(map,x-1,y,test_map)
			if center < map[x+1][y] and test_map[x+1][y] == 0:
				size += calculate_size(map,x+1,y,test_map)
		#center
		else:
			if center < map[x+1][y] and test_map[x+1][y] == 0:
				size += calculate_size(map,x+1,y,test_map)
			if center < map[x-1][y] and test_map[x-1][y] == 0:
				size += calculate_size(map,x-1,y,test_map)
			if center < map[x][y+1] and test_map[x][y+1] == 0:
				size += calculate_size(map,x,y+1,test_map)
			if center < map[x][y-1] and test_map[x][y-1] == 0:
				size += calculate_size(map,x,y-1,test_map)
		return size

with open('inputday9.txt') as f:
	lines = f.readlines()
length = len(lines[0]) - 1
# create map
map = []
x = 0
for line in lines:
	x += 1
	mapline = []
	for y in range(length):
		mapline.append(int(line[y]))
	map.append(mapline)

#create test_map
test_map = []
for line in range(x):
	test_map.append([0] * length)


size_basins= []
#search for low points
for i in range(x):
	for y in range(length):
		center = map[i][y]
		# corners
		if (i == 0 and y == 0):
			if (map[i + 1][y] > center and map[i][y +1] > center):
				size_basins.append(calculate_size(map,i,y,test_map))
		elif(i == 0 and y == length -1):
			if (map[i + 1][y] > center and map[i][y - 1] > center):
				size_basins.append(calculate_size(map,i,y,test_map))
		elif (i == x -1 and y == 0):
			if (map[i -1][y] > center and map[i][y +1] > center):
				size_basins.append(calculate_size(map,i,y,test_map))
		elif (i == x -1 and y == length -1):
			if (map[i - 1][y] > center and map[i][y -1] > center):
				size_basins.append(calculate_size(map,i,y,test_map))
		#sides
		elif i == 0:
			if (map[i+1][y] > center and map[i][y-1] > center and map[i][y+1] > center):
				size_basins.append(calculate_size(map,i,y,test_map))
		elif i == x -1:
			if (map[i-1][y] > center and map[i][y-1] > center and map[i][y+1] > center):
				size_basins.append(calculate_size(map,i,y,test_map))
		elif y == 0:
			if (map[i][y +1] > center and map[i-1][y] > center and map[i+1][y] > center):
				size_basins.append(calculate_size(map,i,y,test_map))
		elif y == length - 1:
			if (map[i][y -1] > center and map[i-1][y] > center and map[i+1][y] > center):
				size_basins.append(calculate_size(map,i,y,test_map))
		#center
		else :
			if map[i][y-1] > center and map[i][y+1] > center and \
			map[i-1][y] > center and map[i+1][y] > center:
				size_basins.append(calculate_size(map,i,y,test_map))
print(size_basins)
size_basins.sort(reverse=True)
print(size_basins)
total = 1
for i in range(3):
	total *= size_basins[i]
print(total)
# for i in range(x):
# 	print(test_map[i])
