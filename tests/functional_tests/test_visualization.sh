test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

#test visualizations are creating files
run box_good python ../../src/box.py --filename ../test_data/test_data_file.csv --country Albania  --country_column 0  --emissions_column 29 --xlabel Emissions --ylabel Amount_of_Emissions --output_nm func_box_test.png
assert_equal func_box_test.png func_box_test.png 

#test exit code when incorrect input is given
run box_good python ../../src/box.py --filename ../test_data/test_data_file.csv --country albania  --country_column 0  --emissions_column 29 --xlabel emissions --ylabel amount_of_emissions --output_nm 
assert_no_stdout
assert_exit_code 2 


#test that giving a nonexistent command produces error
run box_good python ../../src/box.py --filename ../test_data/test_data_file.csv --country albania  --country_column 0  --emissions_column 29 --sillyCommand --xlabel emissions --ylabel amount_of_emissions --output_nm 'test_stder.png' 
assert_stderr

#test visualizations are creating files
run hist_good python ../../src/hist.py --filename ../test_data/test_data_file.csv --country Albania  --country_column 0  --emissions_column 29 --xlabel Emissions --ylabel Amount_of_Emissions --output_nm func_hist_test.png
assert_equal func_hist_test.png func_hist_test.png 

#test exit code when incorrect input is given
run hist_er python ../../src/hist.py --filename ../test_data/test_data_file.csv --country albania  --country_column 0  --emissions_column 29 --xlabel emissions --ylabel amount_of_emissions --output_nm 
assert_no_stdout
assert_exit_code 2 


#test that giving a nonexistent command produces error
run hist_err python ../../src/hist.py --filename ../test_data/test_data_file.csv --country albania  --country_column 0  --emissions_column 29 --sillyCommand --xlabel emissions --ylabel amount_of_emissions --output_nm 'test_stder.png' 
assert_stderr

#test visualizations are creating files
run corr_good python ../../src/correlation.py --filename ../test_data/test_data_file.csv --country Albania  --country_column 0  --emissions_column 29 --xlabel Emissions --ylabel Amount_of_Emissions --output_nm func_corr_test.png
assert_equal func_corr_test.png func_corr_test.png 

#test exit code when incorrect input is given
run corr_good python ../../src/correlation.py --filename ../test_data/test_data_file.csv --country albania  --country_column 0  --emissions_column 29 --xlabel emissions --ylabel amount_of_emissions --output_nm 
assert_no_stdout
assert_exit_code 2 


#test that giving a nonexistent command produces error
run corr_good python ../../src/correlation.py --filename ../test_data/test_data_file.csv --country albania  --country_column 0  --emissions_column 29 --sillyCommand --xlabel emissions --ylabel amount_of_emissions --output_nm 'test_stder.png' 
assert_stderr
