test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
#test print fires is not returning empty list
run print_fires_good python ../../src/print_fires.py --filename ../test_data/test_data_file.csv  --country Albania  --country_column 0  --fires_column 1 --stats stdv
assert_stdout
assert_exit_code 0 

#test exit code when incorrect input is given
run print_fires_bad python ../../src/print_fires.py --filename ../test_data/test_data_file.csv  --country lasdkfj  --country_column 0  --fires_column 1 --stats stdv
assert_stdout
assert_exit_code 0 

#test exit code when incorrect input is given
run print_fires_contyear python ../../src/print_fires.py --filename ../test_data/test_data_file.csv  --country Albania  --country_column 0  --fires_column 1 
assert_in_stdout 1992
assert_exit_code 0 

#test that giving a nonexistent command produces error
run print_fires_contyear python ../../src/print_fires.py --filename ../test_data/test_data_file.csv  --country Albania  --country_column 0  --fires_column 2 --stats divide
assert_stderr
