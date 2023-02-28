numbers = {}
for i in range(3):
	for j in range (3):
		for k in range (3):
			sum =i + j + k + 3 
			if sum not in numbers:
				numbers[sum] = 1
			else:
				numbers[sum] += 1
print(numbers)