import sys

def insert(temp, current_player, pair, c_amount, roll, amount,player_wins):
	new_pair = [pair[0], pair[1],pair[2],pair[3]]
	new_pair[current_player] += roll
	if new_pair[current_player] >= 6:
		player_wins[current_player] += (c_amount * amount)
		return
	new_pair =(new_pair[0],new_pair[1])
	if new_pair in temp:
		temp[new_pair] += (c_amount * amount)
	else:
		temp[new_pair] = (c_amount * amount)


def main():
	with open('test.txt') as file:
		lines = file.read().splitlines()
	p1 = int(lines[0].split()[-1])
	p2 = int(lines[1].split()[-1])

	config = {}
	# p1 = 0
	# p2 = 0
	config[(p1,0,p2,0)] = 1
	current_player = 0
	player_wins = [0,0]
	# for i in range(3):
	while config != {}:
		temp = {}
		for pair in config:
			# insert(temp,current_player, pair,config[pair],1, 1,player_wins)
			# insert(temp,current_player, pair,config[pair],2, 1,player_wins)
			# insert(temp,current_player, pair,config[pair],3, 1,player_wins)

			insert(temp,current_player, pair,config[pair],3, 1,player_wins)
			insert(temp,current_player, pair,config[pair],4, 3,player_wins)
			insert(temp,current_player, pair,config[pair],5, 6,player_wins)
			insert(temp,current_player, pair,config[pair],6, 7,player_wins)
			insert(temp,current_player, pair,config[pair],7, 6,player_wins)
			insert(temp,current_player, pair,config[pair],8, 3,player_wins)
			insert(temp,current_player, pair,config[pair],9, 1,player_wins)

		config = temp
		# print('length config:',len(config),'player', current_player + 1)
		# print("\nplayer", current_player +1)
		print(config)
		current_player = (current_player + 1) % 2
	# print(len(config))
	print(player_wins)
	return 0


if __name__ == '__main__':
    sys.exit(main())