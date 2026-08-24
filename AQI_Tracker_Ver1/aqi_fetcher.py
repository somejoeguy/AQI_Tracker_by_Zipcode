#This is aqi_fetcher.py

import requests
from dotenv import dotenv_values

config = dotenv_values("config_properties.env")
apiKey = config["apiKey"]

config = {}

locational_data = {
    "UserLocation": {
        "zip": "",
        "AQI": "N/A",
        "url": ""
    }
}

aqi_history = []

#Checks your API, undo the comments for API check in console.

#with open("config_properties.env") as f:
 #   for line in f:
  #      if "=" in line:
   #         key, value = line.strip().split("=", 1)
    #        config[key.strip()] = value.strip()

#print(config)

def update_user_aqi(zipcode):


    url = (
        f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=25&API_KEY={apiKey}"

    )

    locational_data["UserLocation"]["url"] = url

    response = requests.get(url).json()
    pm25_value = "N/A"

    pollutants = {}

    for item in response:
        if item["ParameterName"] == "PM2.5":
            pm25_value = item["AQI"]

    locational_data["UserLocation"]["AQI"] = pm25_value

    for item in response:
        name = item["ParameterName"]
        aqi = item["AQI"]
        pollutants[name] = aqi


def AQI_data(zipcode):

    aqi = locational_data["UserLocation"]["AQI"]
    report = f"AQI Report for ZIP Code: {zipcode}: \n \n"
    report += f"AQI is {aqi}\n"
    return report

