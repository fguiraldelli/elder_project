import fileinput
from enterprise import Enterprise
from collections import OrderedDict

def create_file_list(list_of_files):
    """ Function that reads the inputed arguments and returns a two lists: 
    files and enterprises"""
    list_of_files.remove(list_of_files[0])
    list_of_enterprises = []
    return list_of_enterprises, list_of_files

def count_answer_type(dict_type_question, answer):
    """Function that counts the correct answer and imcrements it"""
    if answer >= 0 and answer <= 1:
        dict_type_question['fav'] += 1
    elif answer >= 3 and answer < 5:
        dict_type_question['unfav'] += 1
    else:
        dict_type_question['neutral'] += 1
    return dict_type_question

def init_question(answer):
    """Function that initiates new question"""

    dict_type_question ={'fav':0, 'neutral':0, 'unfav':0}
    return count_answer_type(dict_type_question, answer)

def filled_class(enterprise_name, survey, invalid_num, count_line):
    """Function that stores raw data in each class"""
    valid_num = count_line - invalid_num
    new_class = Enterprise(enterprise_name, valid_num, invalid_num, survey)
    return new_class

def sort_list(list_to_sort):
    """Function that sorts list in ascending order"""
    return sorted(list_to_sort, key=lambda k: k[0])

def sort_descending_fav_list(list_to_sort):
    """Function that sorts list in descending order"""
    return sorted(list_to_sort, key=lambda k: k[1], reverse=True)

def display_summary_by_companies(count_enterprise, list_of_enterprises):
    """Function that displays the summary for all companies in 
    descending order of favorable answer by percentage"""
    print('\nSummary by companies:\n')
    for i in range(count_enterprise):
        list_of_enterprises[i].display_summary()

def display_favorable_answers(count_enterprise, list_of_enterprises):
    """Function that displays the favorable answer ordered by id and 
    the companies ordered in descending order of favorable asnwer by 
    percentage"""
    print('Fav answers by questions:')
    fav_list = []
    fav_dict = {}
    question_id = list_of_enterprises[count_enterprise-1].get_ids_from_survey()
    for i in question_id:
        fav_list = []
        for j in range(count_enterprise):
            fav_list.append(list_of_enterprises[j].get_fav_answer_by_id(i))
        fav_dict[i] = sort_descending_fav_list(fav_list)
    fav_dict = OrderedDict(sorted(fav_dict.items()))
    # Display question id and enterprise percentage
    for k,v in fav_dict.items():
        print('\n{}: '.format(k), end='')
        for i in range(count_enterprise-1):
            print('{} {}% fav, '.format(v[i][0], v[i][1]), end='')
        i = count_enterprise-1
        print('{} {}% fav '.format(v[i][0], v[i][1]), end='')
    print('\n')

def display_valid_answers(count_enterprise, list_of_enterprises):
    """Function that displays valid answers in alphabetic order"""
    print('Valid answers:\n')
    valid_num_list = []
    for i in range(count_enterprise):
        valid_num_list.append(list_of_enterprises[i].get_valid_answer())
    for enterprise, valid_num in sort_list(valid_num_list):
        print('{}: {}'.format(enterprise, valid_num))
    print('\n')

def display_invalid_answers(count_enterprise, list_of_enterprises):
    """Function that displays invalid answers in alphabetic order"""
    print('Invalid answers:\n')
    invalid_num_list = []
    for i in range(count_enterprise):
        invalid_num_list.append(list_of_enterprises[i].get_invalid_answer())
    for enterprise, invalid_num in sort_list(invalid_num_list):
        print('{}: {}'.format(enterprise, invalid_num))
    print('\n')

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
                if fileinput.filelineno() < fileinput.lineno():
                    list_of_enterprises.append(filled_class(enterprise_name,
                        survey, count_invalid, count_line))
                survey = {}
                count_line = 0
                count_invalid = 0
                enterprise_name = line
                count_enterprise += 1 
            else:
                question_number, answer = map(int,line.split(' '))
                if answer < 0 or answer > 4:
                    count_invalid += 1
                elif question_number not in survey.keys():
                    survey[question_number] = init_question(answer)
                else:
                    survey[question_number] = count_answer_type\
                    (survey[question_number], answer)
            count_line += 1
        list_of_enterprises.append(filled_class(enterprise_name,
            survey, count_invalid, count_line))
    return count_enterprise, list_of_enterprises