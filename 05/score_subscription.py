import sys
import json
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer

# Check if the correct number of command-line arguments are provided
if len(sys.argv) != 2:
    print("Usage: python score_subscription.py '<json_input>'")
    sys.exit(1)

# Read the JSON input from the command line argument
json_input = sys.argv[1]

# Parse the JSON input into a Python dictionary
try:
    input_data = json.loads(json_input)
except json.JSONDecodeError:
    print("Invalid JSON format. Please provide a valid JSON.")
    sys.exit(1)

# Ensure that the necessary fields are present in the JSON input
required_fields = {"job", "duration", "poutcome"}
if not required_fields.issubset(input_data.keys()):
    print(f"Missing required fields. Please include: {required_fields}")
    sys.exit(1)

# Load the model and DictVectorizer (dv) from the pickle files
with open("model1.bin", "rb") as model_file:
    model = pickle.load(model_file)

with open("dv.bin", "rb") as dv_file:
    dv = pickle.load(dv_file)

# Check that the loaded objects are of the expected types
if not isinstance(model, LogisticRegression):
    print("Loaded model is not a LogisticRegression instance.")
    sys.exit(1)

if not isinstance(dv, DictVectorizer):
    print("Loaded dv is not a DictVectorizer instance.")
    sys.exit(1)

# Transform the input data using the DictVectorizer
input_vectorized = dv.transform([input_data])

# Predict the probability using the LogisticRegression model
predicted_proba = model.predict_proba(input_vectorized)[0, 1]

# Output the result
print(f"Predicted probability of subscription: {predicted_proba:.3f}")
