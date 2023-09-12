import numpy as np
def get_column(file_name, query_column, query_value, result_column):
    value_match = []
    with open(file_name,'r') as f:
        for line in f:
            line_data = line.split(',')
            if line_data[query_column] == query_value:
                value_match.append(line_data[result_column])
    return(value_match)
