f = [int(x) for x in open('inputday7.txt').readline().split(',')]
max_value = max(f)
min_value = min(f)
count = len(f)
print(max_value, min_value, count)
min_fuel = None
min_value = -1
for x  in range(min_value,max_value +1):
	total_fuel = 0
	for y in f:
		total_fuel += abs(x - y)
	if min_fuel != None:
		if total_fuel < min_fuel:
			min_fuel = total_fuel
			min_value = x
	else :
		min_fuel = total_fuel
		min_value = x
print(min_fuel, x)
