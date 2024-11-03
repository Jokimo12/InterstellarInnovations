import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast"

locations = [
    {"name": "Rome", "latitude": 41.9028, "longitude": 12.4964},
    {"name": "Milan", "latitude": 45.4642, "longitude": 9.1900},
    {"name": "Florence", "latitude": 43.7696, "longitude": 11.2558},
    {"name": "Naples", "latitude": 40.8518, "longitude": 14.2681},
    {"name": "Positano", "latitude": 40.6281,"longitude": 14.4855},
    {"name": "Cinque Terre", "latitude": 44.1460, "longitude": 9.6542},
    {"name": "Rimini", "latitude": 44.0678, "longitude": 12.5695},
    {"name": "Taormina", "latitude": 37.8512, "longitude": 15.2850},
    {"name": "Tropea", "latitude": 38.6762, "longitude": 15.8986},
    {"name": "Porto Cervo", "latitude": 41.1334, "longitude": 9.5398},
    {"name": "Cortina d'Ampezzo", "latitude": 46.5405, "longitude": 12.1357},
    {"name": "Courmayeur", "latitude": 45.7916, "longitude": 6.9659},
    {"name": "Madonna di Campiglio", "latitude": 46.2293, "longitude": 10.8258},
    {"name": "Livigno", "latitude": 46.5457, "longitude": 10.2062},
    {"name": "Selva di Val Gardena", "latitude": 46.5533, "longitude": 11.7637},
    {"name": "Bormio", "latitude": 46.4676, "longitude": 10.3742},
    {"name": "Venice", "latitude": 45.4371, "longitude": 12.3326}
]


params = {
    "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation_probability", "precipitation", "cloud_cover"],
    "forecast_days": 16,
    "timezone": "Europe/Rome"
}
'''

all_data = []

for location in locations:
    params["latitude"] = location["latitude"]
    params["longitude"] = location["longitude"]
    response = requests.get(url, params=params)
    data = response.json()
    hourly_data = data.get("hourly", {})
    df = pd.DataFrame(hourly_data)
    df["time"] = pd.to_datetime(df["time"])
    
    # Filter for daytime hours
    df = df[(df["time"].dt.hour >= 6)]
    
    # Add location name for reference
    df["location"] = location["name"]
    
    # Append to the list
    all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)

combined_df.to_json("italy_weather_data_forecast.csv", index=False)
'''

'''def make_weather_request(city):
    params = {
    "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation_probability", "precipitation", "cloud_cover"],
    "forecast_days": 16,
    "timezone": "Europe/Rome",
    "latitude": city[0],
    "longitude": city[1]
    }
    response = requests.get(url, params=params)
    data = response.json()
    hourly_data = data.get("hourly", {})
    df = pd.DataFrame(hourly_data)
    df["time"] = pd.to_datetime(df["time"])
    
    # Filter for daytime hours
    df = df[(df["time"].dt.hour >= 6)]

    return df
    '''

       






