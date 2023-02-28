# this is the implementation of Zachery of the second exercise of day 1 of AOC
with open("input.txt", "r") as f:
	Lines = f.readlines()

counter = 0
for i in range(1997):
	if Lines[i] < Lines[i + 3]:
		counter += 1
print(counter)