def get_line(start, end):
    """Bresenham's Line Algorithm
    Produces a list of tuples from start and end
 
    >>> points1 = get_line((0, 0), (3, 4))
    >>> points2 = get_line((3, 4), (0, 0))
    >>> assert(set(points1) == set(points2))
    >>> print points1
    [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
    >>> print points2
    [(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
    """
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
 
    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)
 
    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
 
    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1
 
    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1
 
    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
 
    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points

def draw_on_map(points, map):
	for x in points:
		map[x[1]][x[0]] += 1

f = open("inputday5.txt")
lines = f.readlines()

#process the lines into coordinates
coordinates = []
for x in lines:
	holder = []
	x = x.split()
	xsplit = x[0].split(',')
	holder += xsplit
	xsplit = x[2].split(',')
	holder += xsplit
	coordinates.append(holder)

#print(coordinates)
map_size = 1000
map = []
for i in range(map_size):
	map.append([0]*map_size)

for x in coordinates:
	#if(x[0] == x[2] or x[1] == x[3]):
	points = get_line( (int(x[0]),int(x[1])),(int(x[2]),int(x[3])))
	#print(points)
	draw_on_map(points, map)

for i in range(map_size):
	for j in range(map_size):
		print(map[i][j],end='')
	print("")

#count everything above 2
count = 0
for i in range(map_size):
	for j in range(map_size):
		if map[i][j] > 1 :
			count += 1
print('count is', count)
f.close()