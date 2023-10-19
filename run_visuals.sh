python src/correlation.py --filename Agrofood_co2_emission.csv  --country Albania  --country_column 0  --urban_column 26 --emissions_column 29 --xlabel Urban_Population --ylabel Emissions --output_nm upop_emis_cor.png

python src/hist.py --filename Agrofood_co2_emission.csv  --country Albania  --country_column 0  --emissions_column 29 --xlabel Emissions --ylabel Frequency --output_nm emis_hist.png

python src/box.py --filename Agrofood_co2_emission.csv  --country Albania  --country_column 0  --emissions_column 29 --xlabel Emissions --ylabel Amount_of_Emissions --output_nm emis_box.png