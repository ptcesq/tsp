import pandas as pd 
import numpy as np 

df = pd.read_csv('./data/cities.csv') 

cities = df.set_index('city_state').transpose().to_dict(orient='list')

##
from haversine import haversine 

