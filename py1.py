# import requests

# url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

# querystring = {"city":"Seattle"}

# headers = {
# 	"X-RapidAPI-Key": "456ef42d3bmsha76e2021d578ad6p1047dfjsnab34a3f2d63e",
# 	"X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())
import requests

url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

querystring = {"city":"Seattle"}

headers = {
	"X-RapidAPI-Key": "4ace5af660msh4d6beb6b7f3e616p17036bjsna5dd10f93d16",
	"X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())