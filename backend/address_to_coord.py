import requests

def get_coordinates(address):
    api_key =   # Replace with your actual API key
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    else:
        print(f"Error: {data['status']}")
        if 'error_message' in data:
            print(f"Error Message: {data['error_message']}")
        return None

# Example usage
result = get_coordinates('204 Bellhaven Avenue')
if result is not None:
    l1, l2 = result
    print(f"Latitude: {l1}, Longitude: {l2}")
else:
    print("Could not fetch coordinates.")

