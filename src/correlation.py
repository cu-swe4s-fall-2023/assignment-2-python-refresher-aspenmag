import matplotlib.pyplot as plt
import numpy as np
import print_fires as pf
import my_utils as u
import argparse

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
parser.add_argument('--urban_column',
                    type=int,
                    help='column number containing urban population',
                    required=False)
parser.add_argument('--emissions_column',
                    type=int,
                    help='column number containing total emissions',
                    required=False)
parser.add_argument('--stats',
                    type=str,
                    help='perform statistics; mean median or stdv',
                    required=False)
parser.add_argument('--xlabel',
                    type=str,
                    help='x label for correlation',
                    required=False)
parser.add_argument('--ylabel',
                    type=str,
                    help='y label for correlation',
                    required=False)
parser.add_argument('--output_nm',
                    type=str,
                    help='filename for output plot',
                    required=False)


def correlation_plt(a, b, xl, yl, output):
    """
    Create a correlation (scatter) plot of two variables
    inputs: a: x data set, nx1
            b: y dataset, nx1
            xl: x axis label, str
            yl: y axis label, str
            output: output file name, str
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(a, b)
    ax.set_ylabel(yl)
    ax.set_xlabel(xl)
    ax.set_title('Correlation')

    plt.savefig(str(output), bbox_inches='tight')


def main():
    args = parser.parse_args()
    try:
        urban_pop = u.get_column(args.filename, args.country_column,
                                 args.country, args.urban_column)
        emissions = u.get_column(args.filename, args.country_column,
                                 args.country, args.emissions_column)
    except PermissionError:
        print('Could not open (permissions error) ' + args.filename)
        sys.exit(1)
    except FileNotFoundError:
        print('Could not find ' + args.filename)
        sys.exit(1)
    except TypeError:
        print('Missing required argument')
        sys.exit(1)
    try:
        correlation_plt(urban_pop, emissions, args.xlabel,
                        args.ylabel, args.output_nm)
    except TypeError:
        print('Missing required argument')
        sys.exit(1)


if __name__ == '__main__':
    main()
