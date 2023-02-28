def full_pattern_found(pattern1, pattern2):
	for x in pattern1:
		if x not in pattern2:
			return False
	return True

def decypher(digit_patterns_list):
	digit_patterns = ["x"] * 10
	segments_5 = []  # for the patterns of 2,3,5
	segments_6 = []  # for the patterns of 0,6,9
	
	# set 1,4,5 and 8 because of their unique pattern length
	for i in digit_patterns_list:
		length = len(i)
		if length == 2:
			digit_patterns[1] = i
		elif length == 3:
			digit_patterns[7] = i
		elif length == 4:
			digit_patterns[4] = i
		elif length == 7:
			digit_patterns[8] = i
		elif length == 5:
			segments_5.append(i)
		elif length == 6:
			segments_6.append(i)
	# determine the 0,6 and 9
	for x in segments_6:
		if full_pattern_found(digit_patterns[4], x) == True:
			digit_patterns[9] = x
		elif full_pattern_found(digit_patterns[1], x) == False:
			digit_patterns[6] = x
		else:
			digit_patterns[0] = x
	#determine the 2, 3 and 5
	#determin the 3
	for x in segments_5:
		print(x, digit_patterns[9], digit_patterns[1])
		if full_pattern_found(digit_patterns[1],x) == True:
			digit_patterns[3] = x
		elif full_pattern_found(x, digit_patterns[9]) == True:
			digit_patterns[5] = x
		else:
			digit_patterns[2] = x	
	print(digit_patterns)
	return digit_patterns

def convert_output_patterns(output, digit_patterns):
	result = 0
	for i in range(4):
		for x in range(10):
			if len(output[i]) == len(digit_patterns[x]):
				if full_pattern_found(output[i],digit_patterns[x]):
					result += x * (10 ** (3 -i))
				
	return result

#read in patterns
input_list = open('inputday8.txt').read().splitlines()
digit_patterns_list = []
final_patterns_segment = []
#divide the patterns between input and output
for x in input_list:
	parts = x.split('|')
	digit_patterns_list.append(parts[0].split())
	final_patterns_segment.append(parts[1].split())
#decypher pattern
count = len(digit_patterns_list)
total_count = 0
for i in range(count):
	digit_patterns = decypher(digit_patterns_list[i]) 
	result = convert_output_patterns(final_patterns_segment[i],digit_patterns)
	total_count += result
print(total_count)	