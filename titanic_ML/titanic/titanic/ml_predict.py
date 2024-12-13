
import os
import pickle

# Construct the path dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "titanic_model.sav")

# Load the model
with open(model_path, 'rb') as file:
    randomforest = pickle.load(file)

def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
    x=[[pclass,sex,age,sibsp,parch,fare,embarked,title]]
    # randomforest = pickle.load(open('titanic_model.sav','rb'))
    prediction = randomforest.predict(x)
    if prediction == 0:
        return "not survived"
    elif prediction == 1:
        return "survived"
    else:
        return "error"