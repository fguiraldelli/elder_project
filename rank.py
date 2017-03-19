import sys
import fileinput
from enterprise import Enterprise
from question import Question
from collections import OrderedDict

def create_file_list_and_enterprise(list):
    """ Function that reads the inputed arguments and returns a two lists: 
    files and enterprises"""
    print (list)
    list.remove(list[0])
    list_of_enterprises = []
    for i in range(len(list)):
        list_of_enterprises.append(Enterprise())
    return list_of_enterprises, list

def count_answer_type(dict_type_question, answer):
    """Function that counts the correct answer and imcrements it"""
    if answer > -1 and answer < 2:
        dict_type_question['fav'] += 1
    elif answer > 3 and answer < 5:
        dict_type_question['unfav'] += 1
    else:
        dict_type_question['neutral'] += 1
    return dict_type_question

def init_question(answer):
    """Function that initiates new question"""

    dict_type_question ={'fav':0, 'neutral':0, 'unfav':0}
    return count_answer_type(dict_type_question, answer)

def read_files_from_input(list_of_files, list_of_enterprises):
    """Function that reads each file and store the data in a class 
    for each enterprise"""
    count_enterprise = 0
    count_invalid = 0
    dict_question = {}
    

    with fileinput.input(files=((list_of_files))) as f:
        for line in f:
            if fileinput.isfirstline():
                print(fileinput.filename())
                list_of_enterprises[count_enterprise].enterprise_name = line
                count_enterprise += 1 
            else:
                question_number, answer = map(int,line.split(' '))
                print(question_number,answer)
                if answer < 0 or answer > 4:
                    count_invalid += 1
                elif question_number not in dict_question.keys():
                    dict_question[question_number] = init_question(answer)
                else:
                    dict_question[question_number] = count_answer_type\
                    (dict_question[question_number], answer)
        dict_question = OrderedDict(sorted(dict_question.items()))
        print(dict_question)
        print ('INCONSISTENT: '+ str(count_invalid))
        count_invalid = 0
    for i in range(len(list_of_enterprises)):
        print (list_of_enterprises[i].enterprise_name)



#read the input arguments and remove argument in index 0 of the list
list_of_enterprises, list_of_files = create_file_list_and_enterprise(sys.argv)
read_files_from_input(list_of_files, list_of_enterprises)