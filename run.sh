set -e
set -u
set -o pipefail

#1: runs correctly
python src/print_fires.py --filename Agrofood_co2_emission.csv  --country Albania  --country_column 0  --fires_column 1 --stats stdv

set +e
#2: produces type error
python src/print_fires.py --filename Agrofood_co2_emission.csv  --country Albania --country_column 0  --fires_column Albania

#3: produces out of range error
python src/print_fires.py --filename Agrofood_co2_emission.csv  --country Albania --country_column 500  --fires_column 1

set -e
