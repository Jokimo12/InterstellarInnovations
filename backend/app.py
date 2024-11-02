from flask import Flask, request, jsonify
from flask_cors import CORS
from weatherdata_getter import make_weather_request

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json  # Get JSON data from React
    location = data.get("city")
    budget = data.get("budget")
    preferences = data.get("preferences")
    temperature_data = make_weather_request(location)
    #call AI Model
    processed_data = trivology_model(temperature_data, location, budget, preferences)

    return jsonify({"result": processed_data})

if __name__ == '__main__':
    app.run(port=5000)  # Run Flask on port 5000
