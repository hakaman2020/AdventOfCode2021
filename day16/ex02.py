def packet (msg_bin, start):
	version = int(msg_bin[0 + start: 3 + start],2)
	#print('version:',version)
	typeID = int(msg_bin[3 + start:6 + start],2)
	print('typeID:',typeID)
	cp = start + 6
	lit_list = []
	lit_value = -1
	if typeID == 4:
		done = False
		bitstring = ''
		while not done:
			if msg_bin[cp] == '0':
				done = True
			bitstring += msg_bin[cp + 1:cp + 5]
			cp += 5
		lit_value = int(bitstring,2)
		print('type4 literal value:',lit_value)
	else :
		lengthID = msg_bin[cp]
		cp += 1
		if lengthID == '0':
			bitstring = msg_bin[cp+0:cp+15]
			#print('bitstring:',bitstring)
			bit_length = int(bitstring,2)
			print('lenghtID 0 value:',bit_length)
			cp += 15
			cbl = 0
			while cbl < bit_length:
				#print('cbl:',cbl, bit_length)
				temp_cp, temp_value = packet(msg_bin,cp)
				cbl += temp_cp - cp
				cp = temp_cp
				lit_list.append(temp_value)
		else:
			bitstring = msg_bin[cp+0:cp+11]
			cp += 11
			number_sub = int(bitstring,2)
			print('lengthID 1 value:',number_sub)
			for i in range(number_sub):
				cp, temp_value = packet(msg_bin,cp)
				lit_list.append(temp_value)
	#print('packet type:',typeID,' ', lit_list)
	if typeID == 0:
		lit_value = sum(lit_list)
	elif typeID == 1:
		lit_value = lit_list[0]
		for i in range(len(lit_list)-1):
			lit_value *= lit_list[i+1]
	elif typeID == 2:
		lit_value = min(lit_list)
	elif typeID == 3:
		lit_value = max(lit_list)
	elif typeID == 5:
		if lit_list[0] > lit_list[1]:
			lit_value = 1
		else:
			lit_value = 0
	elif typeID == 6:
		if lit_list[0] < lit_list[1]:
			lit_value = 1
		else:
			lit_value = 0
	elif typeID == 7:
		if lit_list[0] == lit_list[1]:
			lit_value = 1
		else:
			lit_value = 0
	return cp, lit_value




with open('inputday16.txt') as file:
	msg = file.readline().rstrip('\n')

msg_bin = ''
for c in msg:
	msg_bin += bin(int(c,16)).lstrip('0b').zfill(4)
#print(msg_bin)

print(packet(msg_bin,0)[1])

