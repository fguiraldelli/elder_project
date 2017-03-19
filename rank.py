import sys
import fileinput
import time
from enterprise import Enterprise
from question import Question
from collections import OrderedDict

def create_file_list(list):
    """ Function that reads the inputed arguments and returns a two lists: 
    files and enterprises"""
    list.remove(list[0])
    list_of_enterprises = []
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

def sort_survey(survey):
    return OrderedDict(sorted(survey.items()))

def filled_class(enterprise_name, survey, invalid_num, count_line):
    valid_num = count_line - invalid_num
    new_class = Enterprise(enterprise_name, valid_num, invalid_num, survey)
    return new_class

def read_files_from_input(list_of_files, list_of_enterprises):
    """Function that reads each file and store the data in a class 
    for each enterprise"""
    count_enterprise = 0
    with fileinput.input(files=((list_of_files))) as f:
        survey = {}
        enterprise_name = ''
        count_line = 0
        for line in f:
            line = line.strip()
            if fileinput.isfirstline():
                print('File line number First Line: '+str(fileinput.filelineno()))
                print('Line number First Line: '+str(fileinput.lineno()))
                if fileinput.filelineno() < fileinput.lineno():
                    list_of_enterprises.append(filled_class(enterprise_name,
                        survey, count_invalid, count_line))
                #time.sleep(5)
                survey = {}
                count_line = 0
                count_invalid = 0
                enterprise_name = line
                count_enterprise += 1 
            else:
                question_number, answer = map(int,line.split(' '))
                # print(question_number,answer)
                if answer < 0 or answer > 4:
                    count_invalid += 1
                elif question_number not in survey.keys():
                    survey[question_number] = init_question(answer)
                else:
                    survey[question_number] = count_answer_type\
                    (survey[question_number], answer)
            count_line += 1
            print('Line number: '+str(fileinput.lineno()))
            print('File line number: '+str(fileinput.filelineno()))
            # list_of_enterprises[count_enterprise-1].survey = survey
        list_of_enterprises.append(filled_class(enterprise_name,
            survey, count_invalid, count_line))
        for i in range(count_enterprise):
            list_of_enterprises[i].displayStatistics()

#read the input arguments and remove argument in index 0 of the list
list_of_enterprises, list_of_files = create_file_list(sys.argv)
read_files_from_input(list_of_files, list_of_enterprises)