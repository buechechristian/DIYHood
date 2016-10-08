
import sys, re, string

src = sys.argv[1]
dst = sys.argv[2]

src_file = open(src, 'r')
input_txt = src_file.read().decode('utf-8')
src_file.close()

txt = input_txt.lower()
txt = re.sub('\\.\\s*', '\n', txt)

lines = txt.split('\n')

filled_lines = []
for line in lines:
	if len(line) > 1:
		filled_lines.append(line)

output_text = string.join(filled_lines, '\n').encode('utf-8')

dst_file = open(dst, 'w')
dst_file.write(output_text)
dst_file.close()

