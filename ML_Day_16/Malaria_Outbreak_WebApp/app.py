import numpy as np
from flask import Flask, render_template

app = Flask(__name__)

#Load the trained model
import pickle
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    from flask import render_template
    return render_template('index.html')

@app.route('/predict', methods = ['POST','GET'])
def predict():
    #GEt the input values from the form
    from flask import request
    Positive = float(request.form['pos'])
    pf = float(request.form['pfinp'])
    city = request.form['city']
    print(city)
    #Make API call to get weather data
    api_key = '3324c62376ebf6deab6313f8a078af24'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city,api_key)

    import requests
    response = requests.get(url)
    data = response.json()
    print(data)

    if data['cod'] == 200:
        main = data['main']
        tempmin_api = main['temp_min']
        tempmax_api = main['temp_max']
        humidity_api = main['humidity']

        # Combine the input values from the form and API data into input_data array
        # input_data = np.array([[Positive, pf, tempmin_api, tempmax_api, humidity_api]])
        input_data = [[Positive, pf, tempmin_api, tempmax_api, humidity_api]]

        prediction = model.predict_proba(input_data)
        output = prediction[0][1]

        with open('scaler.pkl', 'rb') as file:
            sst = pickle.load(file)

        # Determine the outbreak based on the probability threshold
        if output >= 0.5:
            outbreak = 'Yes'
        else:
            outbreak = 'No'

        return render_template('index.html', prediction=outbreak)

    else:
        return 'Invalid city name or API request failed.'

if __name__ == '__main__':
    app.run(debug=True)
