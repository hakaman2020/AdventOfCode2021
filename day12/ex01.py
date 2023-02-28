def create_path(cave, current_path,current_node,list_paths):
	new_path = current_path.copy()
	new_path.append(current_node)
	if current_node == 'end':
		list_paths.append(new_path)
		return
	for x in cave[current_node]:
		if x not in new_path:
			count = create_path(cave,new_path,x,list_paths)
		elif x in new_path and x.isupper():
			count = create_path(cave, new_path,x,list_paths)

with open('inputday12.txt') as file:
	lines = file.read().splitlines()
cave = {}
for line in lines:
	path = line.split('-')
	if path[0] in cave:
		cave[path[0]].append(path[1])
	else:	
		cave[path[0]] = []
		cave[path[0]].append(path[1])
	if path[1] in cave:
		cave[path[1]].append(path[0])
	else:
		cave[path[1]] =[]
		cave[path[1]].append(path[0])

print(cave)
current_path = []
list_paths = []
create_path(cave,current_path, 'start',list_paths)
print(len(list_paths))