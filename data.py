import requests
import os



BANK_OF_CANADA_ENDPOINT = "https://www.bankofcanada.ca/valet"
STATS_CANADA_ENDPOINT = "https://www150.statcan.gc.ca/t1/wds/rest/getCubeMetadata"
LINKEDIN_ENDPOINT = "https://api.linkedin.com/v2/{service}/{resourceIdentifier}"

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

linkedin_params = {
    "active": true,
    "client_id": "xxxxxxxx",
    "authorized_at": 1493055596,
    "created_at": 1493055596,
    "status": "active",
    "expires_in": 1497497620,
    "scope": "r_liteprofile,r_emailaddress,w_member_social"
}
response = requests.get(url=LINKEDIN_ENDPOINT, params=linkedin_params)

indeed_data = response.json()
print(indeed_data)



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