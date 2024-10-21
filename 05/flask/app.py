from flask import Flask, request, jsonify
import os
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer

# Initialize the Flask app
app = Flask(__name__)
model_path = 'model2.bin'
dv_path = 'dv.bin'

with open(model_path, 'rb') as f_model:
    model = pickle.load(f_model)

with open(dv_path, 'rb') as f_dv:
    dv = pickle.load(f_dv)

# Check that the loaded objects are correct
if not isinstance(model, LogisticRegression):
    raise ValueError("Loaded model is not a LogisticRegression instance.")

if not isinstance(dv, DictVectorizer):
    raise ValueError("Loaded dv is not a DictVectorizer instance.")

# Define the route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the POST request
    input_json = request.get_json()

    # Ensure the necessary fields are present in the input
    required_fields = {"job", "duration", "poutcome"}
    if not required_fields.issubset(input_json.keys()):
        return jsonify({"error": f"Missing required fields: {required_fields}"}), 400

    # Transform the input data using the DictVectorizer
    input_vectorized = dv.transform([input_json])

    # Make a prediction using the model
    predicted_proba = model.predict_proba(input_vectorized)[0, 1]

    # Return the predicted probability as a JSON response
    return jsonify({"subscription_probability": predicted_proba})

# Start the Flask app (Gunicorn will handle the actual running in production)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)

