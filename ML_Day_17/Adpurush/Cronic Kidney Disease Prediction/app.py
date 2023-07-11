import pickle
from flask import Flask, render_template, request
import PyPDF2
import pandas as pd
import re

app = Flask(__name__)

# Load the scaler from the pickle file
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Load the trained model from the pickle file
with open('trained_model.pkl', 'rb') as file:
    classifier = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Get the uploaded file from the request
    pdf_file = request.files['pdfFile']

    # Check if a file was uploaded
    if pdf_file:
        # Load the PDF file
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # extract its text
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Pre-Process the extracted text (e.g., pass it to the ML model for prediction)
        feature_values = []
        pattern = r'(\w+)\s*=\s*([\d.]+)'
        matches = re.findall(pattern, text)
        for match in matches:
            feature_name = match[0].lower()
            feature_value = float(match[1])
            feature_values[feature_name] = feature_value

        # Convert the feature values into a DataFrame
        df = pd.DataFrame([feature_values])

        # Apply feature scaling on the feature values
        df_scaled = scaler.transform(df)

        # Make predictions on the feature values
        predictions = classifier.predict(df_scaled)

        # Return the result template with the predictions and feature_values
        return render_template('result.html', prediction=predictions[0], feature_values=feature_values)

    else:
        return "No file uploaded."

if __name__ == '__main__':
    app.run(debug=True)
