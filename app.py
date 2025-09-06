from flask import Flask, request, jsonify
import pandas as pd
import os
from utils.data_loader import load_all_data
from recommend.tenant import recommend_properties_for_tenant
from recommend.landlord import recommend_tenants_for_property

app = Flask(__name__)

DATA_DIR = "data"

@app.route('/upload-data', methods=['POST'])
def upload_data():
    # Accept CSV files for each model
    for key in ['users', 'properties', 'bookings', 'likes', 'reviews']:
        file = request.files.get(key)
        if file:
            file.save(os.path.join(DATA_DIR, f"{key}.csv"))
    return jsonify({"status": "success"})

@app.route('/recommend/tenant/<user_id>', methods=['GET'])
def recommend_for_tenant(user_id):
    data = load_all_data(DATA_DIR)
    recommendations = recommend_properties_for_tenant(user_id, data)
    return jsonify({"user_id": user_id, "recommendations": recommendations})

@app.route('/recommend/landlord/<property_id>', methods=['GET'])
def recommend_for_landlord(property_id):
    data = load_all_data(DATA_DIR)
    matches = recommend_tenants_for_property(property_id, data)
    return jsonify({"property_id": property_id, "matches": matches})

if __name__ == '__main__':
    app.run(debug=True)
    