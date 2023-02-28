#this version uses the mean in
def fuel_cost(distance):
	total = (distance * (1 + distance)/2)
	return(total)

f = [int(x) for x in open('inputday7.txt').readline().split(',')]
print(f)
count = len(f)
total = sum(f)
average = int(total / count)
print(count, total, average)
min_fuel = None
min_value = -1
fuels = []
fuel = 0
for y in f:
	fuel += fuel_cost(abs(average - y))
print(fuel)
