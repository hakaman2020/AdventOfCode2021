import sys

def rolling(current_pos, current_score, current_player, player_wins, roll):
	temp_pos = current_pos.copy()
	temp_score = current_score.copy()
	new_pos = ((temp_pos[current_player] - 1 + roll) % 10) + 1
	temp_score[current_player] += new_pos
	temp_pos[current_player] = new_pos
	if temp_score[current_player] >= 21:
		dimensions = 0
		if roll == 3 or roll == 9:
			dimensions = 1
		elif roll == 4 or roll == 8:
			dimensions = 3
		elif roll == 5 or roll == 7:
			dimensions = 6
		elif roll == 7:
			dimensions = 7
		player_wins[current_player] += dimensions
		return
	current_player = (current_player + 1) % 2
	for i in range(3,10):
		rolling(temp_pos, temp_score, current_player, player_wins, i)

def main():
	with open('/home/hakaman/projects/aoc/day21/test.txt') as file:
		lines = file.read().splitlines()
	p1_pos = int(lines[0].split()[-1])
	print(p1_pos)
	p2_pos = int(lines[1].split()[-1])
	print(p2_pos)

	player_wins = [0 , 0]
	current_pos = [p1_pos, p2_pos]
	current_player = 0
	current_score = [0,0]

	for i in range(3,10):
		rolling(current_pos, current_score, current_player, player_wins, i)
	if player_wins[0] > player_wins[1]:
		print(player_wins[0])
	else:
		print(player_wins[1])
	return 0


if __name__ == '__main__':
    sys.exit(main())