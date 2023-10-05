[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher

-----Contents
my_utils :
-get_column(), which will read a file (csv type) get the value in the result column for values in query clolumn that match query value 
i.e. print number of fies in the United States
-returns a list of ints

print_fires.py : 
-will call get_column() with specified parameters that are taken from the command line
-returns a list of ints

run.sh :
-will run the print_fries.py


------to run the program:
to run use $bash run.sh

to change parameters, update the command line inputs in run.sh



----updates : 
-incorperating best practices 
-accepting command line argument inputs from the user
-documentation included via docustring
-.gitignore will ignore .DS_Store type files

----updates : 
-added functionality in my_utils.py to include mean, median and standard deviation 
-added command line optoinal parameter to print_fires.py to specify one of the above statistics
-created unit tests and functional tests
-put my_utils.py and print_fires.py in the src directory. Can still run run.sh from the main directory.

----updates : 
-updated directory structure for tests 

----to run unit tests: 
run the test_my_utils.py file from unit test directory

---- to run fucntional tests: 
run test_print_fires.sh from the functional test directory 
