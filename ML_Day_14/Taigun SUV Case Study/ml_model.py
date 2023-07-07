#Step 1 : pip install pandasai
import pandas as pd
import pickle

dataset = 'SUV_Purchase.csv'
df = pd.read_csv(dataset)

print(df.head())

#Step 2 : preprocessing
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])

#Step 3 : Feature Engineering : Where we need to remove that column
df.drop('User ID', axis = 1, inplace=True)

#Step 4 : Load the data into X and Y
X = df.drop(['Purchased'],axis=1)
Y = df[['Purchased']]

#Step 5 : Split the data
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)


#Step 6 : Normalize the data by scaling

from sklearn.preprocessing import StandardScaler
sst = StandardScaler()
X_train = sst.fit_transform(X_train)
X_test = sst.transform(X_test)

#Creating a .pkl file of the scalar to be used later
with open('sst.pkl','wb') as file:
    pickle.dump(sst, file)

#Step 7 : Train the model
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

rf.fit(X_train,Y_train) #fit the model with training data

#Step 8 : Predection and testing accuracy
Y_pred = rf.predict(X_test)
print("Overall Accuracy ",rf.score(sst.transform(X),Y)*100)

#pickling

import pickle

pickle.dump(rf,open('model.pkl','wb')) #searlizing our model(obj to bytestream) (wb means write binary , we re writing to the model.pkl file)
print("Model Dumped")






# import pandas as pd
#
# from sklearn.preprocessing import LabelEncoder
#
# from sklearn.model_selection import train_test_split
#
# from sklearn.preprocessing import StandardScaler
#
# from sklearn.ensemble import RandomForestClassifier
#
# import pickle
#
# # Step 1: Load the dataset
#
# dataset = 'SUV_Purchase.csv'
#
# df = pd.read_csv(dataset)
#
# # Step 2: Preprocess data
#
# label_encoder = LabelEncoder()
#
# df['Gender'] = label_encoder.fit_transform(df['Gender'])
#
# # Step 3: Feature engineering
#
# df.drop('User ID', axis=1, inplace=True)
#
# # Step 4: Load data
#
# X = df.drop(['Purchased'], axis=1)
#
# Y = df[['Purchased']]
#
# # Step 5: Split data
#
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
#
# # Step 6: Normalize the data
#
# scaler = StandardScaler()
#
# X_train = scaler.fit_transform(X_train)
#
# X_test = scaler.transform(X_test)
#
# # Step 7: Train the model
#
# rf = RandomForestClassifier()
#
# rf.fit(X_train, Y_train)
#
# # Step 8: Predict from the model
#
# Y_pred = rf.predict(X_test)
#
# print(Y_pred)
#
# # Print the model accuracy on the entire dataset
#
# print(rf.score(scaler.transform(X), Y) * 100)
#
# # Pickling - Serialize the model and scaler
#
# pickle.dump(rf, open('model.pkl', 'wb')) # Serialize the model
#
# pickle.dump(scaler, open('scaler.pkl', 'wb')) # Serialize the scaler
#
# print("Model and scaler are saved")
#
# # Load the trained model and scaler
#
# model = pickle.load(open('model.pkl', 'rb'))
#
# scaler = pickle.load(open('scaler.pkl', 'rb'))
#
# def scale_data(data):
#
# # Transform the data using the loaded scaler
#
# scaled_data = scaler.transform(data)
#
# return scaled_data
#
# def predict_dummy(age, gender, salary):
#
# # Preprocess the input data (similar to what you did before training the model)
#
# gender_encoded = 1 if gender == 'Male' else 0
#
# # Scale the input data
#
# scaled_data = scale_data([[age, gender_encoded, salary]])
#
# # Make the prediction using the loaded model
#
# prediction = model.predict(scaled_data)
#
# print(prediction[0])
#
# return prediction[0]
#
# # Example usage
# age = 27
# gender = 'Female'
# salary = 84000
#
# prediction = predict_dummy(age, gender, salary)
#
# print("Prediction:", prediction)