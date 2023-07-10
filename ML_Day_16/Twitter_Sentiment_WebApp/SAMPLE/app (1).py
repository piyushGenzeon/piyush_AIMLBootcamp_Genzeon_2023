from flask import Flask, render_template, request
import numpy as np
import pickle
import requests

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    # Get the input values from the form
    Positive = float(request.form['pos'])
    pf = float(request.form['pfinp'])
    city = request.form['city']

    # Make API call to get weather data
    api_key = '6d59c4bbf4f1808d20a125488c3cceb3'
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city,api_key)

    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        main = data['main']
        tempmin_api = main['temp_min']
        tempmax_api = main['temp_max']
        humidity_api = main['humidity']

        # Combine the input values from the form and API data into input_data array
        input_data = np.array([[Positive, pf, tempmin_api, tempmax_api, humidity_api]])
        prediction = model.predict_proba(input_data)
        output = prediction[0][1]

        with open('sst.pkl', 'rb') as file:
            sst = pickle.load(file)

        # Determine the outbreak based on the probability threshold
        if output >= 0.5:
            outbreak = 'Yes'
        else:
            outbreak = 'No'

        return render_template('index1.html', prediction=outbreak)

    else:
        return 'Invalid city name or API request failed.'

if __name__ == '__main__':
    app.run(debug=True)
