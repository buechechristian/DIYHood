from os import listdir
from os.path import isfile, join

import sys, string, re

path = sys.argv[1]

filepaths = [f for f in listdir(path) if isfile(join(path, f))]

output = ''

for filepath in filepaths[1:]:
	file = open(path + filepath, 'r')
	lines = file.read().decode('utf-8').split('\n')
	file.close()
	std_lines = []
	for line in lines:
		std_line = ''
		for c in line:
			if ord(c) < 128:
				std_line = std_line + c
			elif ord(c) == 8217:
				std_line = std_line + '\''
			elif ord(c) == 160:
				std_line = std_line + '-'
			elif ord(c) == 8230:
				std_line = std_line + '...'
			else:
				std_line = std_line + ' '
		std_lines.append(std_line)
	all_input = string.join(std_lines, '\n')
	all_input = all_input.lower()
	# all_input = re.sub(r'\.\s*', '\n', all_input)
	all_input = re.sub(r'!', '.', all_input)
	all_input = re.sub(r';', ',', all_input)
	all_input = re.sub(r'>', ' ', all_input)
	all_input = re.sub(r'&', 'and', all_input)
	all_input = re.sub(r'[0-9]+', 'many', all_input)
	all_input = re.sub(r'\ +', ' ', all_input)

	output_lines = []
	for line in all_input.split('\n'):
		if len(line) > 1:
			output_lines.append(line)

	if len(output) > 1:
		output = output + '\n'
	output = output + string.join(output_lines, '\n')

print output
