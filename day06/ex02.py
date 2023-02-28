#it is the same program as ex01 but with 256 instead of 80 days
f = open('inputday6.txt')
input =f.readline().rstrip('\n').split(',')
day = [0]*9
for x in range(9):
	day[x] = input.count(str(x))
amount_of_days = 256 
for x in range(amount_of_days):
	day[0],day[1],day[2],day[3],day[4],day[5],day[6],day[7],day[8] = \
		day[1],day[2],day[3],day[4],day[5],day[6],day[7] + day[0],day[8],day[0]
print(sum(day))
f.close()