from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load model and associated files
with open('nearest_neighbors_model.pkl', 'rb') as f:
    knn_model = pickle.load(f)

with open('feature_columns.pkl', 'rb') as f:
    feature_columns = pickle.load(f)

with open('types_encoder.pkl', 'rb') as f:
    types_encoder = pickle.load(f)
    
print(type(types_encoder))

def trivology_model(location, budget, preferences):
    preferences_encoded = types_encoder.transform(preferences)  # Assumes 'preferences' is a list

    input_data = pd.DataFrame(columns=feature_columns)
    input_data.loc[0] = np.zeros(len(feature_columns))  # Initialize with zeros
    
    input_data['location'] = location
    input_data['budget'] = budget
    input_data['preferences'] = preferences_encoded

     #Make prediction/recommendation using the KNN model
    distances, indices = knn_model.kneighbors(input_data)
    recommendations = indices[0]  # Example of retrieving recommendation indices

    return recommendations

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json  # Get JSON data from React
    location = data.get("city")
    budget = data.get("budget")
    preferences = data.get("preferences")
    print(preferences)
    #call AI Model
    processed_data = trivology_model(location, budget, preferences)

    return jsonify({"result": processed_data})

if __name__ == '__main__':
    app.run(port=5000)  # Run Flask on port 5000
