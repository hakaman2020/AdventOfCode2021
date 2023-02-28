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

risk = 0
#search for low points
for i in range(x):
	for y in range(length):
		center = map[i][y]
		# corners
		if (i == 0 and y == 0):
			if (map[i + 1][y] > center and map[i][y +1] > center):
				risk += center + 1
		elif(i == 0 and y == length -1):
			if (map[i + 1][y] > center and map[i][y - 1] > center):
				risk += center + 1
		elif (i == x -1 and y == 0):
			if (map[i -1][y] > center and map[i][y +1] > center):
				risk += center + 1
		elif (i == x -1 and y == length -1):
			if (map[i - 1][y] > center and map[i][y -1] > center):
				risk += center + 1
		#sides
		elif i == 0:
			if (map[i+1][y] > center and map[i][y-1] > center and map[i][y+1] > center):
				risk += center + 1
		elif i == x -1:
			if (map[i-1][y] > center and map[i][y-1] > center and map[i][y+1] > center):
				risk += center + 1
		elif y == 0:
			if (map[i][y +1] > center and map[i-1][y] > center and map[i+1][y] > center):
				risk += center + 1
		elif y == length - 1:
			if (map[i][y -1] > center and map[i-1][y] > center and map[i+1][y] > center):
				risk += center + 1
		#center
		else :
			if map[i][y-1] > center and map[i][y+1] > center and \
			map[i-1][y] > center and map[i+1][y] > center:
				risk += center +1
print(risk)
