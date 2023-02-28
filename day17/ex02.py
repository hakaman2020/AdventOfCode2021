def reach_target(xs, ys, x_max, x_min, y_max, y_min):
	reached = False
	done = False
	position = [0,0]
	while not done:
		#update position
		position[0] += xs
		position[1] += ys
		#check if it is in target 
		if position[0] > x_max or position[1] < y_min:
			done = True
			break
		if (position[0] >= x_min and position[0] <= x_max) and (position[1] >= y_min and position[1] <= y_max):
			reached = True
			done = True
			break
		#update speed
		if xs <= 0:
			xs = 0
		else:
			xs -= 1
		ys -= 1
	return reached

def det_min_x(x_min):
	found = False
	x = 0
	while not found:
		top = (x**2 + x)/2
		if top > x_min:
			found = True
			break
		x += 1
	return x


def sum_series(start, n):
	result = (n *(2*start - n + 1))// 2
	return result

with open('inputday17.txt') as file:
	line = file.readline().rstrip('\n')
split = line.split()
x_min, x_max = split[2].lstrip('x=').rstrip(',').split('..')
x_min = int(x_min)
x_max = int(x_max)
y_min, y_max = split[3].lstrip('y=').split('..')
y_min = int(y_min)
y_max = int(y_max)

count = 0

min_x = det_min_x(x_min)
for xs in range(min_x,x_max+1):
	for ys in range(y_min,abs(y_min +1)+1):
		if reach_target(xs,ys,x_max,x_min,y_max,y_min):
			count += 1
print(count)