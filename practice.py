import pandas as pd
import json

r = {'rates': [{'provider': 'HotelsCom2', 'host': 'Hotels.com', 'rate': '244', 'taxes': '39'}, {'provider': 'StayForLong', 'host': 'StayForLong', 'rate': '267', 'taxes': '16'}, {'provider': 'ZenHotels', 'host': 'ZenHotels.com', 'rate': '272', 'taxes': '12'}, {'provider': 'Expedia', 'host': 'Expedia.com', 'rate': '244', 'taxes': '39'}, {'provider': 'BookingCom', 'host': 'Booking.com', 'rate': '244', 'taxes': '39'}, {'provider': 'Splitty', 'host': 'Traveluro', 'rate': '229', 'taxes': '64'}, {'provider': 'Priceline', 'host': 'Priceline', 'rate': '244', 'taxes': '39'}, {'provider': 'BookingeDreamsWL', 'host': 'eDreams', 'rate': '244', 'taxes': '39'}, {'provider': 'TravelocityEWS', 'host': 'Travelocity', 'rate': '244', 'taxes': '39'}, {'provider': 'CtripTA', 'host': 'Trip.com', 'rate': '250', 'taxes': '40'}, {'provider': 'OrbitzEWS', 'host': 'Orbitz.com', 'rate': '244', 'taxes': '39'}, {'provider': 'HiltonImages', 'host': 'Embassy Suites', 'rate': '244', 'taxes': '39'}, {'provider': 'Agoda', 'host': 'Agoda.com', 'rate': '244', 'taxes': '39'}, {'provider': 'FindHotel', 'host': 'FindHotel', 'rate': '244', 'taxes': '39'}, {'provider': 'Urbano', 'host': 'Hurb', 'rate': '244', 'taxes': '39'}]}
df = pd.DataFrame(columns=['PROVIDER', 'HOST', 'RATE','TAXES'], index=range(len(r)))

for i in r.values():
    list = i
parsed_list = []
counter = 0

for item in list:
    parsed_list = ("[%s, %s, %s, %s]" % (item['provider'], item['host'], item['rate'], item['taxes']))
    res = parsed_list.strip('][').split(', ')
    df.loc[counter] = res
    counter += 1

print(df)
#print(parsed_list)
second_list = [{'provider','host','rate','taxes'}]
#list.insert(0, second_list)
#print(list)

#for i in list:
   # print(i)

"""df = pd.DataFrame(list[1:],columns=list[0])
print(df)"""

"""df1 = pd.DataFrame(list, columns = ['Provider', 'Host', 'Rate','Taxes'])
print(df1)"""