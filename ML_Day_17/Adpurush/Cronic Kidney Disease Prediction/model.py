import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd

dataset = 'kidney_disease.csv'
df = pd.read_csv(dataset)
print(df.head())

print(df.isna().sum())

#Droping the unecesary columns
df.drop(['id', 'rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane'], axis =1, inplace = True)

# df = df.drop(columns='rbc')
# df = df.drop(columns='pc')
# df = df.drop(columns='pcc')
# df = df.drop(columns='ba')
# df = df.drop(columns='htn')
# df = df.drop(columns='dm')
# df = df.drop(columns='cad')
# df = df.drop(columns='appet')
# df = df.drop(columns='pe')
# df = df.drop(columns='ane')

print(df)

# Convert 'pcv' column to numeric data type
df['pcv'] = pd.to_numeric(df['pcv'], errors='coerce')
df['wc'] = pd.to_numeric(df['wc'], errors='coerce')
df['rc'] = pd.to_numeric(df['rc'], errors='coerce')

# Fill NaN values with mean or median
df['age'].fillna(df['age'].mean(), inplace=True)
df['bp'].fillna(df['bp'].mean(), inplace=True)
df['sg'].fillna(df['sg'].mean(), inplace=True)
df['al'].fillna(df['al'].mean(), inplace=True)
df['su'].fillna(df['su'].median(), inplace=True)
df['bgr'].fillna(df['bgr'].mean(), inplace=True)
df['bu'].fillna(df['bu'].median(), inplace=True)
df['sc'].fillna(df['sc'].median(), inplace=True)
df['sod'].fillna(df['sod'].median(), inplace=True)
df['pot'].fillna(df['pot'].median(), inplace=True)
df['hemo'].fillna(df['hemo'].mean(), inplace=True)
df['pcv'].fillna(df['pcv'].mean(), inplace=True)
df['wc'].fillna(df['wc'].median(), inplace=True)
df['rc'].fillna(df['rc'].median(), inplace=True)

# Create a mapping dictionary for label encoding
label_mapping = {'ckd': 1, 'notckd': 0}

# Perform label encoding and remove other values
df['classification'] = df['classification'].map(label_mapping)

# Drop rows with NaN values
df.dropna(subset=['classification'], inplace=True)

# Split the data into training and testing sets
X = df.drop('classification', axis=1)
y = df['classification']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# normalisation OR Perform feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train a random forest classifier
classifier = RandomForestClassifier(random_state=42)
classifier.fit(X_train_scaled, y_train)

#Creating Pickle File of our label mapping, scaled data and trained Model
label_encoder_filename = 'label_encoder.pkl'
scaler_filename = 'scaler.pkl'
model_filename = 'trained_model.pkl'

with open(label_encoder_filename, 'wb') as file:
    pickle.dump(label_mapping, file)

with open(scaler_filename, 'wb') as file:
    pickle.dump(scaler, file)

with open(model_filename, 'wb') as file:
    pickle.dump(classifier, file)

print("Model and scaler saved as", label_encoder_filename, "and", scaler_filename, "and", model_filename)

# Make predictions on the testing set
y_pred = classifier.predict(X_test_scaled)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy*100)


