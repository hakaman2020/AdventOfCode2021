class test_node:
	def __init__(self, number):
		self.number = number
	
nodes = []
for i in range(10):
	nodes.append(test_node(i))
last_node = nodes[2]
last_node.number = 5
print(last_node.number)
nodes[2].number = 9
print(last_node.number)