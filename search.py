import sqlite3
import requests
import json
from functions import *
import pandas as pd
import sqlalchemy 
print("Hi, and welcome to hotel search!")
print("            ")
#engine = sqlalchemy.create_engine('sqlite:///hotels.db')



data = find_hotel()
df = pd.DataFrame(data)
df.pop('shortName')
df.pop('coordenates')
df.pop('address')
print(df)
print("     ")
"""pd.read_sql('hotels', engine)

df.to_sql('locations', con=engine, if_exists='replace', index=False)
query_result = engine.execute("SELECT * FROM hotels;").fetchall()
print(pd.DataFrame(query_result))
#pd.read_sql('hotels', engine)"""


desired_hotel = get_hotel_rate()
df2 = pd.DataFrame(desired_hotel)
print("    ")
print("    ")



if df2.empty:
	print("There are currently no reservations available, sorry :( ")
else: 
	print(df2)
	

print("    ")
print("    ")