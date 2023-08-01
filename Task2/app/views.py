import joblib
import pandas as pd
from flask import Blueprint, request, jsonify

views = Blueprint('views', __name__)
model = joblib.load(
    "./gdp_per_capita_predictor.joblib"
)

@views.route('/predict_gdp', methods=["POST"])
def home():
    try:
        # Get data from the request payload
        payload = request.get_json()
        input_data = payload

        # Convert the input data to a DataFrame
        input_df = pd.DataFrame(input_data, index=[0])

        # Predict using the loaded model
        predictions = model.predict(input_df)

        # Prepare the response
        response = {
            'prediction': predictions[0]
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400
