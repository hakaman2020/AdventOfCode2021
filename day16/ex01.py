

def packet (msg_bin, start,vc):
	#print(msg_bin[0+start:3+start])
	version = int(msg_bin[0 + start: 3 + start],2)
	print('version:',version)
	vc[0] += version
	typeID = int(msg_bin[3 + start:6 + start],2)
	print('typeID:',typeID)
	cp = start + 6
	if typeID == 4:
		done = False
		bitstring = ''
		while not done:
			#print(msg_bin[cp:cp+5])
			#print(msg_bin[cp])
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
			print('bitstring:',bitstring)
			bit_length = int(bitstring,2)
			print('lenghtID 0 value:',bit_length)
			cp += 15
			cbl = 0
			while cbl < bit_length:
				print('cbl:',cbl, bit_length)
				temp_cp = packet(msg_bin,cp,vc)
				cbl += temp_cp - cp
				cp = temp_cp
		else:
			bitstring = msg_bin[cp+0:cp+11]
			print('bitstring:',bitstring)
			cp += 11
			number_sub = int(bitstring,2)
			print('lengthID 1 value:',number_sub)
			for i in range(number_sub):
				cp = packet(msg_bin,cp,vc)
	return cp




with open('inputday16.txt') as file:
	msg = file.readline().rstrip('\n')

msg_bin = ''
for c in msg:
	msg_bin += bin(int(c,16)).lstrip('0b').zfill(4)
#print(msg_bin)
vc = [0]

packet(msg_bin,0,vc)

print(vc)

