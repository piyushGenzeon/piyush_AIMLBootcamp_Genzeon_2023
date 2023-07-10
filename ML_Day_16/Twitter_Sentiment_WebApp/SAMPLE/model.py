# import numpy as np
# import requests
#
# city = input("Enter the city name: ")
#
# api_key = '6d59c4bbf4f1808d20a125488c3cceb3'
# url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city,api_key)
#
# response = requests.get(url)
# data = response.json()
#
# if data['cod'] == 200:
#     print(f"Place: {data['name']}")
#     print(f"Latitude: {data['coord']['lat']}")
#     print(f"Longitude: {data['coord']['lon']}")
#
#     main = data['main']
#     tempmin = main['temp_min']
#     tempmax = main['temp_max']
#     humidity = main['humidity']
#
#     weather = data['weather']
#     description = weather[0]['description']
#
#     # # Check if 'rain' key exists in the API response
#     # if 'rain' in data:
#     #     rain = data['rain']
#     #     if '1h' in rain:
#     #         rainfall = rain['1h']
#     #     else:
#     #         rainfall = 0
#     # else:
#     #     rainfall = 0
#    # pos=input("positive")
#    # pfinp=input("pf")
#     print(f"Minimum Temperature: {tempmin}°C")
#     print(f"Maximum Temperature: {tempmax}°C")
#     print(f"Humidity: {humidity}%")
#     #print(f"Positive: {pos}")
#     #print(f"PF: {pfinp}")
#    # print(f"Rainfall: {rainfall} mm")
#     print(f"Weather Description: {description}")
# else:
#     print("Invalid city name or API request failed.")

##########################################################################
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


#reading dataframe
dataframe='outbreak_detect.csv'
df=pd.read_csv(dataframe)
#print(df)

#label encoding
label_encoder=LabelEncoder()
df['Outbreak']=label_encoder.fit_transform(df['Outbreak'])

#putting data in x and y
x=df.drop(['Outbreak','Rainfall'],axis=1)
y=df['Outbreak']

#splitting
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)

#standardscaler - data normalization
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

#after normalization create a pickel file
with open('sst.pkl', 'wb') as file:
    pickle.dump(sc, file)

#training the model using KNN algo
clf = RandomForestClassifier()
clf.fit(x_train, y_train)

y_pred=clf.predict(x_test)

# inputt=[]
# inputt.append(tempmax)
# inputt.append(tempmin)
# inputt.append(humidity)
# final = [np.array(inputt)] #converted to array using numpy
# print(final)
# prediction=clf.predict_proba(final) # predict_proba method needs the input in array form
# output = '{0:.{1}f}'.format(prediction[0][1], 2)
# print(output)
# if output>=str(0.5):
#   print(1)
# else:
#   print(0)

#create a pickel file of the model
pickle.dump(clf, open('model.pkl','wb'))

#print(df)

clf.score(sc.transform(x),y)
print("Overall Accuracy:", clf.score(sc.transform(x), y) * 100)