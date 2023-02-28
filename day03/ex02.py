def bin_to_dec(binarystr):
	decimal_value = 0
	amount_of_bits = len(binarystr)
	for i in range(amount_of_bits):
		if binarystr[i] == '1':
			decimal_value += 2 ** (amount_of_bits - 1 - i)
	return decimal_value


def count_bit(lines, digitnbr):
	count = 0
	for i in range(len(lines)):
		if lines[i][digitnbr] == '1':
			count += 1
	return count

def remove(lines, bit, digitnbr):
	i = 0
	while i < len(lines):
		if lines[i][digitnbr] == bit:
			del lines[i]
		else:
			i += 1



with open('inputday3.txt') as file:
	lines = file.read()
lines = lines.splitlines()
lines2 = lines.copy()
size_lines = len(lines)
amount_of_bits = len(lines[0])
for i in range(amount_of_bits):
	amount_of_ones = count_bit(lines, i)
	amount_of_zeros = len(lines) - amount_of_ones
	print(amount_of_ones, amount_of_zeros, i)
	if amount_of_ones >= amount_of_zeros :
		print('remove zeros')
		remove(lines,'0',i)
	else:
		print('remove ones')
		remove(lines,'1',i)
	print(lines)
	if len(lines) <= 1:
		break
oxygen = int(bin_to_dec(lines[0]))
print("oxygen")
for i in range(amount_of_bits):
	amount_of_ones = count_bit(lines2, i)
	amount_of_zeros = len(lines2) - amount_of_ones
	print(amount_of_ones, amount_of_zeros, i)
	if amount_of_ones < amount_of_zeros :
		print('remove zeros')
		remove(lines2,'0',i)
	else:
		print('remove ones')
		remove(lines2,'1',i)
	print(lines2)
	if len(lines2) <= 1:
		break
co2 = int(bin_to_dec(lines2[0]))
print("oxy =",oxygen, "co2 =", co2," sum is", oxygen *co2)
