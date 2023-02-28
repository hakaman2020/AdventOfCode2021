class node:
	def __init__(self, number):
		self.number = number
		self.visited = False
		self.min_dist = -1
		self.prev = [0,0]

	def set_min_dist(self, min_dist):
		self.min_dist = min_dist
	
	def set_prev(self, prev_node):
		self.prev = prev_node
	
	def set_visited(self, visited):
		self.visited = visited

def determine_directions(max_x,max_y,x,y):
	directions =[]
	if x - 1 >= 0:
		directions.append((-1,0))
	if x + 1 < max_x:
		directions.append((1,0))
	if y - 1 >= 0:
		directions.append((0,-1))
	if y + 1 < max_y:
		directions.append((0,1))
	return directions

def return_node_lowest_min_dist(graph):
	
	lowest_min_dist = -1
	lowest_node = [-1,-1]
	first_set = False

	for x in range(len(graph)):
		for y in range(len(graph[0])):
			if not graph[x][y].visited :
				if lowest_min_dist == -1 and first_set == False:
					first_set = True
					lowest_min_dist = graph[x][y].min_dist
					lowest_node[0], lowest_node[1] = x, y
				elif graph[x][y].min_dist != -1 and graph[x][y].min_dist < lowest_min_dist:
					lowest_min_dist = graph[x][y].min_dist
					lowest_node[0], lowest_node[1] = x, y
	return lowest_node

def print_graph(graph):
	#print graph
	for i in range(len(graph)):
		for j in range(len(graph[0])):
			print(graph[i][j].number,end='')
		print()

def print_graph_risk(graph):
	for i in range(len(graph)):
		for j in range(len(graph[0])):
			node = graph[i][j]
			print('[',str(node.number),',', str(node.min_dist).rjust(2),',',str(node.prev).rjust(6),']',end='')
		print()

def print_graph_visit(graph):
	for i in range(len(graph)):
		for j in range(len(graph[0])):
			print('[',str(graph[i][j].visited).rjust(6),']',end='')
		print()

def dijkstra(graph,max_x,max_y,node_coor):
	directions = determine_directions(max_x, max_y,node_coor[0],node_coor[1])
	current_node = graph[node_coor[0]][node_coor[1]]
	current_node.visited = True

	for x,y in directions:
		node_eval = graph[node_coor[0]+ x][node_coor[1] +y]
		if not node_eval.visited:
			new_min_dist = current_node.min_dist + node_eval.number
			if (node_eval.min_dist == -1) or (node_eval.min_dist > new_min_dist):
				node_eval.min_dist = current_node.min_dist + node_eval.number
				node_eval.prev = [node_coor[0],node_coor[1]]

with open('test.txt') as file:
	lines = file.read().splitlines()
graph = []
for line in lines:
	numbers = []
	for char in line:
		numbers.append(node(int(char)))
	graph.append(numbers)

max_x = len(graph)
max_y = len(graph[0])

#set starting node to min dist of 0
graph[0][0].min_dist = 0
#print(graph[0][0].min_dist)

#print_graph(graph)

next_coor = [0,0]
done = False
while not done:
	dijkstra(graph, max_x, max_y, next_coor)
	next_coor = return_node_lowest_min_dist(graph)
	if next_coor == [-1,-1]:
		done = True

print_graph_risk(graph)
#print_graph_visit(graph)
print(graph[max_x-1][max_y -1].min_dist)