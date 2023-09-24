#1: runs correctly
python print_fires.py --filename Agrofood_co2_emission.csv  --country Albania  --country_column 0  --fires_column 1

#2: produces type error
python print_fires.py --filename Agrofood_co2_emission.csv  --country Albania --country_column 0  --fires_column Albania

#3: produces out of range error
python print_fires.py --filename Agrofood_co2_emission.csv  --country Albania --country_column 500  --fires_column 1
