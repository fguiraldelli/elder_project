This document explains the composition of zip file and how to build and run the program:

The zip file rank.zip is composed of the following files:

- Readme.txt;
- rank.py - this file is a main type file, that make the calls for other files that executes the logic of the program;
- input_output.py - this file handles the inputs and outputs of the program and instantiate the class enterprise;
- enterprise.py - this file is the class Enterprise, this class stores the values nedeed for counting and calculatingof values to show summary, favorable answers, valid and invalid answers;
- unittest_input_output.py - this file make some unit tests in input_output.py file;
- unittest_enterprise.py - this file run some unit tests in class Enterprise;

DEVELOPER AND RUNNING ENVIRONMENTS

This program was developed and runned in the followed environment:
 - Ubuntu 16.04 OS System (Linux distribution);
 - Python 3.5.2 (programming language) - All imported libraries are part of the standard installation package of this python version.

HOW TO BUILD AND RUN PROGRAM

To run this program, you must type the following command:

"python3 rank.py [full path of files]" like example bellow:

python3 rank.py input_files/it_services_iqMO2z.txt input_files/mybank_zqweSt.txt input_files/logistic_company_AbOzZl.txt

HOW TO RUN TESTS

To run tests, you must type following command to execute both tests:

"python3 -m unittest -v unittest_input_output.py unittest_enterprise.py"

Or with you prefer run tests separately execute the following commands:

"python3 -m unittest -v unittest_input_output.py" to execute tests in input_output.py

"python3 -m unittest -v unittest_enterprise.py"

ABOUT COPYRIGHT

This is not a licensed code, so anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

ABOUT THE AUTHOR

Francisco Guiraldelli is a software engineer with a degree in Computer Science from the Federal University of São Carlos in July 2015. He is currently a master's degree student in Computer Science at the same University.