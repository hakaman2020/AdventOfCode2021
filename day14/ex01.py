#this version is the inefficient version. use the ex02_efficient version
#This simulate all the polymer insertion. You don't have to because all you need 
#is the created polymers. Look for the other one for a more efficent code for 
#this puzzle
def insert_polymer(polymer, template):
	size = len(polymer)
	to_be_inserted = []
	for i in range(size -1):
		poly = polymer[i] + polymer[i+1]
		to_be_inserted.append(template[poly])
	for i in range(size-1,0,-1):
		polymer.insert(i,to_be_inserted.pop())

with open('inputday14.txt') as file:
	lines = file.read().splitlines()

lenght_file = len(lines)
polymer = list(lines[0])
template = {}
unique = {}
for recipe_line in range (2,lenght_file):
	recipe = lines[recipe_line].split(' -> ')
	template[recipe[0]] = recipe[1]
	if recipe[1] not in unique:
		unique[recipe[1]] = 0

for i in unique:
	unique[i]= lines[0].count(i)
# print(template)
print('unique:',unique)
for day in range(10):
	insert_polymer(polymer,template)
print('done')
print(polymer)
most_common_count = -1
least_common_count = -1
for char in unique:
	count = polymer.count(char)
	if most_common_count == -1:
		most_common_count = count
	elif count > most_common_count:
		most_common_count = count
	if least_common_count == -1:
		least_common_count = count
	elif count < least_common_count:
		least_common_count = count
print(most_common_count - least_common_count)
