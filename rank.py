import sys
import fileinput

#read the input arguments and remove argument in index 0 of the list
list = sys.argv
#list.remove(list[0])
print('\n')
print('\n')
list.remove(list[0])
print (list)
print('\n')
name = ""
with fileinput.input(files=((list))) as f:
	for line in f:
		if fileinput.isfirstline():
			name = line
		else:
			
	print (name)
