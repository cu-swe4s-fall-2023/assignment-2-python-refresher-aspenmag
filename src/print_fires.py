import my_utils as u
import argparse


"""
use get_column to read and search a file for the number of fires in a given
country. uses argparse to accept comand line arguments from the user.

output of get_columns is added stored in fires list.

"""

parser = argparse.ArgumentParser(
        description='arguments to parse agrofood_c02 csv using get_column',
        prog='print_fires')
parser.add_argument('--filename',
                    type=str,
                    help='name of the file to parse',
                    required=True)
parser.add_argument('--country',
                    type=str,
                    help='name of country',
                    required=True)
parser.add_argument('--country_column',
                    type=int,
                    help='column number containing countries',
                    required=True)
parser.add_argument('--fires_column',
                    type=int,
                    help='column number containing fires',
                    required=True)
parser.add_argument('--stats',
                    type=str,
                    help='perform statistics; mean median or stdv',
                    required=False)


def call_median(values):
    """
    call the median stats function
    """
    median = u.median(values)
    print('median of search: ', median)
    return median


def call_mean(values):
    """
    call the mean stats function
    """
    mean = u.mean(values)
    print('mean of search: ', mean)
    return mean


def call_stdv(values):
    """
    call the standard deviation stats function
    """
    stdv = u.stdv(values)
    print('standard deviation of search: ', stdv)
    return stdv


def main():
    args = parser.parse_args()
    try:
        fires = u.get_column(args.filename, args.country_column,
                             args.country, args.fires_column)
    except TypeError:
        print('Incorrect agrumnet type, check inputs')

    print(fires)
    # statistics-user input to call function
    try:
        if args.stats == 'mean':
            mean = call_mean(fires)
        if args.stats == 'median':
            median = call_median(fires)
        if args.stats == 'stdv':
            stdv = call_stdv(fires)
    except:  # noqa
        print('invalid stats input argument')
    

if __name__ == '__main__':
    main()
