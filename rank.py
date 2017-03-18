import sys
import fileinput
from enterprise import Enterprise
from question import Question

#read the input arguments and remove argument in index 0 of the list
list = sys.argv
list.remove(list[0])

#Create a list of enterprises classes
list_of_enterprises = []
number_of_enterprises = len(list)
for i in range(number_of_enterprises):
    list_of_enterprises.append(Enterprise())
#Read each file and store the data in a class for each enterprise
count_enterprise = 0
count_invalid = 0
with fileinput.input(files=((list))) as f:
    for line in f:
        if fileinput.isfirstline():
            list_of_enterprises[count_enterprise].enterprise_name = line
            count_enterprise += 1 
        else:
            k, v = map(int,line.split(' '))
            if v < 0 or v > 4:
                count_invalid += 1
            print(k, v)
    print ('INCONSISTENT: '+ str(count_invalid))
    count_invalid = 0
for i in range(number_of_enterprises):
    print (list_of_enterprises[i].enterprise_name)