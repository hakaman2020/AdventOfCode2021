def count_diff(unique):
	most_common_count = -1
	least_common_count = -1
	for char in unique:
		count = unique[char]	
		if most_common_count == -1:
			most_common_count = count
		elif count > most_common_count:
			most_common_count = count
		if least_common_count == -1:
			least_common_count = count
		elif count < least_common_count:
			least_common_count = count
	return (most_common_count - least_common_count)

with open('inputday14.txt') as file:
	lines = file.read().splitlines()

length_file = len(lines)
polymer = list(lines[0])
template = {}
unique_pairs ={}
unique = {}
for recipe_line in range (2,length_file):
	recipe = lines[recipe_line].split(' -> ')
	template[recipe[0]] = recipe[1]
	unique_pairs[recipe[0]] = [recipe[0][0] + recipe[1], recipe[1] + recipe[0][1], 0, 0]
	if recipe[1] not in unique:
		unique[recipe[1]] = 0

for i in unique:
	unique[i]= lines[0].count(i)
length_polymer = len(polymer)
for i in range(length_polymer - 1):
	unique_pairs[polymer[i] + polymer[i +1]][2] +=1

# print(unique)
# print(unique_pairs)
insertion_count = 40
for i in range(insertion_count):
	for pair in unique_pairs:
		pair1, pair2, amount, temp = unique_pairs[pair]
		unique_pairs[pair1][3] += amount
		unique_pairs[pair2][3] += amount
		unique[pair1[1]] += amount
	for pair in unique_pairs:
		unique_pairs[pair][2] = unique_pairs[pair][3]
		unique_pairs[pair][3] = 0
print(count_diff(unique))
