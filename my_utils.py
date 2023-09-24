"""
Various functions
"""

import numpy as np
import sys


def get_column(file_name, query_column, query_value, result_column=0):
    """
    read a file and sort it to find specific values. Add values to
    an array and return the array.
    ---
    Parameters
    ---
    file_name : name of the file to parse, str
    query_column : column number to search for query value in, int
    query_value : value to look for in the query column, str
    result_column : value to be added to return array, int
    ---
    returns
    ---
    value_match : all values from the row contianing query value, list of int
    """
    value_match = []
    try:
        # store values we are searching for, if not, skip value
        with open(file_name, 'r') as f:
            for line in f:
                line_data = line.split(',')
                if line_data[query_column] == query_value:
                    value_match.append(int(line_data[result_column]))
    except PermissionError:
        print('Could not open (permissions error) ' + file_name)
        sys.exit(1)
    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)

    except IndexError:
        print('column out of range')
        sys.exit(1)
    except TypeError:
        print('column numbers should be type int')
        sys.exit(1)
    return(value_match)
