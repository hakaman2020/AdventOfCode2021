class bingocard:
	def __init__(self, numbers):
		self.nbr_matrix = numbers
		self.mark_matrix = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
		self.bingo = False

	def mark_number(self, number):
		if self.bingo == False:
			for i in range(5):
				for j in range(5):
					if self.nbr_matrix[i][j] == number:
						self.mark_matrix[i][j] = 1
						break

	def check_for_bingo(self):
		#check horizontal and vertical lines
		sum_horizontal = 0
		sum_vertical = 0
		for i in range(5):
			for j in range(5):
				sum_horizontal += self.mark_matrix[i][j]
				sum_vertical += self.mark_matrix[j][i]
			if sum_horizontal == 5 or sum_vertical == 5:
				self.bingo = True
				return True
			sum_horizontal = 0
			sum_vertical = 0
		
	def sum_unmarked(self):
		sum = 0
		for i in range(5):
			for j in range(5):
				if self.mark_matrix[i][j] == 0:
					sum += int(self.nbr_matrix[i][j])
		return sum
	
	def print_matrix(self):
		for i in range(5):
			for j in range(5):
				print(self.nbr_matrix[i][j], "(",self.mark_matrix[i][j],") ", end='')
			print("")

# read the number call out
file = open('inputday4.txt', 'r')
callout = ((file.readline()).rstrip('\n')).split(',')
print(callout)

# create the bingo cards
bingo_cards = []
line = file.readline()
while line !='':
	numbers = []
	for x in range(5):
		line = ((file.readline()).rstrip('\n')).split()
		numbers.append(line)
	#print(numbers)
	bingo_cards.append(bingocard(numbers))
	line = file.readline()

# start calling out the numbers
last_winning_bingo_board = None
last_number_of_last_winning_board = None
for x in callout:
	for y in bingo_cards:
		y.mark_number(x)
		if  y.bingo == False and y.check_for_bingo():
			last_winning_bingo_board = y
			last_number_of_last_winning_board = x

last_winning_bingo_board.print_matrix()
print('last number called for last winning board :',last_number_of_last_winning_board)
print('sum of unmarked =', last_winning_bingo_board.sum_unmarked())
print('product = ', int(last_number_of_last_winning_board) * int(last_winning_bingo_board.sum_unmarked()))

file.close()