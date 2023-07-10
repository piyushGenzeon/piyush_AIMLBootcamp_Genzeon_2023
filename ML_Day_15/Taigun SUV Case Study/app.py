# pip install flask
import pickle

from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler



app=Flask(__name__)


#Deserialize / depickle - Loading the model
clf=pickle.load(open('model.pkl','rb'))

#jinja2 template - Template engine - will select the templates from the template folder
@app.route("/")  #Decorators - When user access the root URL - Func get invoked
def hello():
    return render_template("index.html")

@app.route('/predict', methods=['POST','GET'])
def predict_class():
    print([x for x in request.form.values()]) #POST method is working fine - communication created success
    features=[int(x) for x in request.form.values()]
    #Label encode, normalize - 2 conflicts

    with open('sst.pkl', 'rb') as file:
        sst = pickle.load(file)

    # sst = StandardScaler()
    # sst=sst.fit(X_train)
    output=clf.predict(sst.transform([features]))
    print(output) #[1]
    if output[0]==0:  #GET method
        return render_template("index.html",pred="The Person will not purchase the SUV")
    else:
        return render_template("index.html",pred="The Person will purchase the SUV")

if __name__ == "__main__":  #Script executed from main entry file
    app.run(debug=True)  #Create a Flask Local Server