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


def main():
    args = parser.parse_args()
    try:
        fires = u.get_column(args.filename, args.country_column,
                             args.country, args.fires_column)
    except TypeError:
        print('Incorrect agrumnet type, check inputs')

    print(fires)


if __name__ == '__main__':
    main()
