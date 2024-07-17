import requests

url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

querystring = {"city":"Atmakur"}

headers = {
	"X-RapidAPI-Key": "09f9ee34ccmsh2a3d0be0f89ff81p10ad72jsn6b824fb7399e",
	"X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())