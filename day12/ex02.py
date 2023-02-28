def create_path(cave, current_path,current_node,list_paths,smt):
	new_path = current_path.copy()
	new_path.append(current_node)
	if current_node == 'end':
		list_paths.append(new_path)
		return
	for x in cave[current_node]:
		if x not in new_path:
			create_path(cave,new_path,x,list_paths,smt)
		elif x in new_path and x.isupper():
			create_path(cave, new_path,x,list_paths,smt)
		elif x in new_path and x.islower() and smt == True and x != 'start':
			create_path(cave,new_path,x,list_paths,False)

with open('inputday12.txt') as file:
	lines = file.read().splitlines()
cave = {}
count = 0
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
small_cave_token = True
create_path(cave,current_path, 'start',list_paths,small_cave_token)
print(len(list_paths))
