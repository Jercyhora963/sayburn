fhand = open('../ex_05_01/ex_05_01.py')
for line in fhand:
	line = line.rstrip
	if not line.startswith('num'):
		continue
	print(line)
