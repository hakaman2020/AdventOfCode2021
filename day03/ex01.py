amount_of_bits = 12
bits = [0] * amount_of_bits
count = 0

with open("inputday3.txt") as file:
	lines = file.readlines()
for x in lines:
	count += 1
	for i in range(amount_of_bits):
		if x[i] == '1':
			bits[i] += 1
print(count)
print(bits)

decimal_gamma = 0
decimal_epsilon = 0

for i in range(amount_of_bits):
	if bits[i] <= (count / 2):
		decimal_gamma += 2**(amount_of_bits -1 - i)
	else:
		decimal_epsilon += 2**(amount_of_bits -1 -i)
print(decimal_gamma)
print(decimal_epsilon)
print(decimal_epsilon * decimal_gamma)
