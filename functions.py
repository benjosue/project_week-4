import requests
import json 
import sqlite3

def find_hotel():
    
    url = "https://hotel-price-aggregator.p.rapidapi.com/search"

    city_input = input("Enter city of desired stay:    ")
    querystring = {"q":city_input}
    print("    ")
    print("    ")
    headers = {
	"X-RapidAPI-Key": "0ceacf4ba5msh85fc64cdf73f882p1a35fdjsn5c1ff6ca4a33",
	"X-RapidAPI-Host": "hotel-price-aggregator.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()            
 
    return data

def get_hotel_rate():

    selected_hotelId = input("Enter the hoteId that correlates to your desired location:    ")
    checkIn =  input("Enter your desired check in date in the following format, year-month-day (XXXX-XX-XX):     ")
    checkOut = input("Enter your desired check out date in the following format, year-month-day (XXXX-XX-XX):    ")
    
    url = "https://hotel-price-aggregator.p.rapidapi.com/rates"
    api_key = "0ceacf4ba5msh85fc64cdf73f882p1a35fdjsn5c1ff6ca4a33"
    

    payload =    {
    "hotelId": selected_hotelId,
    "checkIn": checkIn,
    "checkOut": checkOut
    }

    headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "hotel-price-aggregator.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    hotel_stats = response.json()

    for key in hotel_stats:
        if key == 'rates':
            return hotel_stats[key]


    
 