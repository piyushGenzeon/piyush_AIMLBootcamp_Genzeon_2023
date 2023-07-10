#Reading Dataframe
import pandas as pd
dataframe = 'outbreak_detect.csv'
df = pd.read_csv(dataframe)


#Label Encoding of 'Outbreak' column as it in text format fo rconverting it
# to numerical format
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['Outbreak'] = label_encoder.fit_transform(df['Outbreak'])

#Putting data in x and y
x = df.drop(['Outbreak','Rainfall'],axis=1)
y = df['Outbreak']

#Splitting
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

# StandardScaler - Data Normalization
# By fitting the StandardScaler on the training data and then transforming both
# the training and testing sets, you ensure that the scaling is consistent across the dataset.
from sklearn.preprocessing import StandardScaler
stdscaler = StandardScaler()
x_train = stdscaler.fit_transform(x_train)
x_test = stdscaler.transform(x_test)

#After Normalization create a pickle file for scaled data
import pickle
with open('scaler.pkl','wb') as file:
    pickle.dump(stdscaler, file)

#Training the mmodel using RandomForest Algo
from sklearn.ensemble import RandomForestClassifier
clfModel = RandomForestClassifier()
clfModel.fit(x_train, y_train)

#Now create Prediction for Testing inputs
y_pred = clfModel.predict(x_test)

#Create a pickle file of the trained model
pickle.dump(clfModel, open('model.pkl','wb'))

#Printing the Final score
score = clfModel.score(stdscaler.transform(x),y)
print("Overall Accuracy : ", score*100)