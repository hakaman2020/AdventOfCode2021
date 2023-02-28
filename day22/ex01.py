import sys


def main():
	with open('/home/hakaman/projects/aoc/day22/inputday22.txt') as file:
		lines = file.read().splitlines()

	reboot = []

	for line in lines:
		add = True
		step = []
		temp = line.split()
		step.append(temp[0])
		coor = temp[1].split(',')
		for i in range(3):
			tempsplit = coor[i].split('..')
			first = int(tempsplit[0][2:])
			second = int(tempsplit[1])
			if abs(first) > 50 or abs(second) > 50:
				add = False
				break
			step.append(first)
			step.append(second)
		if add:
			reboot.append(step)

	# for i in range(len(reboot)):
	# 	print(reboot[i])

	#setup map
	map =[]
	cube_dim = 101
	for x in range(cube_dim):
		temp = []
		for y in range(cube_dim):
			line = [0] * cube_dim
			temp.append(line)
		map.append(temp)
	
	for step in reboot:
		for x in range(step[1]+50,step[2]+50+1):
			for y in range(step[3]+50,step[4]+50 + 1):
				for z in range(step[5]+50,step[6]+50+ 1):
					value = 0
					if step[0] == 'on':
						value = 1
					map[x][y][z] = value
	
	count = 0
	for x in range(101):
		for y in range(101):
			for z in range(101):
				if map[x][y][z] == 1:
					count += 1

	print(count)	


if __name__ == '__main__':
	sys.exit(main())