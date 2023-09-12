import my_utils as u

country='United States of America'
county_column = 0
fires_column = 3
file_name = 'Agrofood_co2_emission.csv'
fires = u.get_column(file_name,county_column,country,fires_column)
print(fires)
