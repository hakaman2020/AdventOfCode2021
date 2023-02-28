#this one was a deceptive easy one
#all you have to do look at the y axis. 
# take the y_min of the target area and reduce it by one and the absolute value
# is the starting speed of y. This is because if you look at y only the y will 
#arrive back at y=0 at the starting speed + 1 but downwards thus negative. 
# With that in mind you can extrapolate that the max starting speed possible is 
# the absolute value of y_min of the target + 1 to not overshoot the target

def calculate_top(y_speed):
	return((y_speed**2 + y_speed)/2)
with open('test.txt') as file:
	line = file.readline().rstrip('\n')
split = line.split()

y_min, y_max = split[3].lstrip('y=').split('..')
y_min = int(y_min)
y_max = int(y_max)
print(y_min)
print(calculate_top(abs(y_min+1)))
