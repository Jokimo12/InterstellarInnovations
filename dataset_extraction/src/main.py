import googlemaps
import pandas as pd
import time

# Initialize the Google Maps client
API_KEY = 'My_Goggle_API_Key'  
gmaps = googlemaps.Client(key=API_KEY)

def get_tourist_attractions_in_Livigno():
    """
    Get tourist attractions in Rome using Google Places API, with pagination support.

    Returns:
    - DataFrame containing tourist attractions, ratings, and types.
    """
    # Coordinates for Rome
    latitude = 46.5457
    longitude = 10.2062
    radius = 5000  # Search radius in meters

    places = []

    # Perform a nearby search
    response = gmaps.places_nearby(location=(latitude, longitude), radius=radius, type='tourist_attraction')

    # Extract relevant data from response
    while True:
        for place in response['results']:
            places.append({
                'Name': place.get('name'),
                'Rating': place.get('rating', 'Not rated'),
                'Types': ', '.join(place.get('types', [])),
                'Latitude': place['geometry']['location']['lat'],
                'Longitude': place['geometry']['location']['lng'],
                'Address': place.get('vicinity')
            })
        # Check for next page token
        if 'next_page_token' in response:
            time.sleep(2)  # Wait a bit for the next page token to become valid
            response = gmaps.places_nearby(location=(latitude, longitude), radius=radius, type='tourist_attraction', page_token=response['next_page_token'])
        else:
            break

    # Convert to DataFrame
    df = pd.DataFrame(places)
    return df

# Example usage
tourist_attractions_Livigno_df = get_tourist_attractions_in_Livigno()
print(tourist_attractions_Livigno_df)

tourist_attractions_Livigno_df