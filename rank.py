import sys
import input_output

#read the input arguments and remove argument in index 0 of the list
list_of_enterprises, list_of_files = input_output.create_file_list(sys.argv)
#read each file and fill data in enterprises classes
count_enterprise, list_of_enterprises = input_output.read_files_from_input(list_of_files,
 list_of_enterprises)
#Display the data statistics and summary
input_output.display_summary_by_companies(count_enterprise, list_of_enterprises)
input_output.display_favorable_answers(count_enterprise, list_of_enterprises)
input_output.display_valid_answers(count_enterprise, list_of_enterprises)
input_output.display_invalid_answers(count_enterprise, list_of_enterprises)