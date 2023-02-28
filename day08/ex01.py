# segments for 1, 4,7 and 8 are 2,4,3,7
f = open('inputday8.txt').readlines()
count = 0
for x in f:
	line = x.rstrip('\n').split()
	print(len(line))
	for i in range(4):
		segs= len(line[11+i])
		if segs == 2 or segs == 4 or segs == 3 or segs == 7:
			count += 1
print(count)