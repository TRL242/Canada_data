import requests
import os
from twilio.rest import Client


BANK_OF_CANADA_ENDPOINT = "https://www.bankofcanada.ca/valet"
STATS_CANADA_ENDPOINT = "https://www150.statcan.gc.ca/t1/wds/rest/getCubeMetadata"
GLASSDOOR_ENDPOINT = "http://api.glassdoor.com/api/api.htm?v=1&format=json&t.p=120&t.k=fz6JLNDfgVs&action=employers&q=pharmaceuticals&userip=192.168.43.42&useragent=Mozilla/%2F4.0"

#
# #=============================BANK OF CANADA==================================#
# stock_params = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK_NAME,
#     "outputsize": "compact",
#     "datatype": "json",
#     "apikey": STOCK_API_KEY,
# }
#
# response = requests.get(STOCK_ENDPOINT, params=stock_params)
# response.raise_for_status()
# stock_data = response.json()["Time Series (Daily)"]
# stock_data_list = [value for (key,value) in stock_data.items()]
# yesterday_data = stock_data_list[0]
# yesterday_closing_price = yesterday_data["4. close"]
# #print(yesterday_closing_price)
#
#
# day_before_yesterday_data = stock_data_list[1]
# day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
#
#
# #=============================STATS CANADA==================================#
# stock_params = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK_NAME,
#     "outputsize": "compact",
#     "datatype": "json",
#     "apikey": STOCK_API_KEY,
# }
#
# response = requests.get(STOCK_ENDPOINT, params=stock_params)
# response.raise_for_status()
# stock_data = response.json()["Time Series (Daily)"]
# stock_data_list = [value for (key,value) in stock_data.items()]
# yesterday_data = stock_data_list[0]
# yesterday_closing_price = yesterday_data["4. close"]
# #print(yesterday_closing_price)
#
#
# day_before_yesterday_data = stock_data_list[1]
# day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


#=============================GLASSDOOR==================================#

glassdoor_params = {
    "v": 1,
    "format": "json",
    "t.p": ###,
    "t.k": ###,
    "userip": "24.69.129.244",
    "useragent": 24.69.129.244,
    "action": 24.69.129.244,
    "action": 24.69.129.244,
}
response = requests.get(url=GLASSDOOR_ENDPOINT, params=glassdoor_params)

glassdoor_data = response.json()
print(glassdoor_data)



# response = requests.get(GLASSDOOR_ENDPOINT, params=stock_params)
# response.raise_for_status()
# stock_data = response.json()["Time Series (Daily)"]
# stock_data_list = [value for (key,value) in stock_data.items()]
# yesterday_data = stock_data_list[0]
# yesterday_closing_price = yesterday_data["4. close"]
# #print(yesterday_closing_price)
#
#
# day_before_yesterday_data = stock_data_list[1]
# day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]