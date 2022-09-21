import numpy as np
from flask import Flask, request, render_template
import pickle
from sklearn import tree, preprocessing
import sklearn.ensemble as ske

# Create an app object using the Flask class.
app = Flask(__name__)

# Load the trained model. (Pickle file)
model = pickle.load(
    open('C:\\Users\\sanja\\app\\fire_prediction\\models\\randomforest_model.pkl', 'rb'))

# Define the route to be home.
# The decorator below links the relative route of the URL to the function it is decorating.
# Here, home function is with '/', our root directory.
# Running the app sends us to index.html.
# Note that render_template means it looks for the file in the templates folder.

# use the route() decorator to tell Flask what URL should trigger our function.


@app.route('/')
def home():
    return render_template('index.html')

# You can use the methods argument of the route() decorator to handle different HTTP methods.
# GET: A GET message is send, and the server returns data
# POST: Used to send HTML form data to the server.
# Add Post method to the decorator to allow for form submission.
# Redirect to /predict page with the output


@app.route('/predict', methods=['POST'])
def predict():
    probability = []
    causes = {}
    incidents = ['Natural', 'Accidental', 'Malicious', 'Other']

    for i, cause in enumerate(incidents):
        causes[i] = cause

    # Convert string inputs to float.
    int_features = [float(x) for x in request.form.values()]
    features = np.array(int_features)
    test = features.reshape(1, 6)
    temp = model.predict_proba(test)
    for i in range(len(temp)):
        probability.append(temp[i][0][1])
        #print(causes[i],':', temp[i][0][1])
    maximum = max(probability)
    index = probability.index(maximum)
    #print('Fire Caused by :',causes[index])

    return render_template('index.html', prediction_text='Fire Caused by {}'.format(causes[index]))


# When the Python interpreter reads a source file, it first defines a few special variables.
# For now, we care about the __name__ variable.
# If we execute our code in the main program, like in our case here, it assigns
# __main__ as the name (__name__).
# So if we want to run our code right here, we can check if __name__ == __main__
# if so, execute it here.
# If we import this file (module) to another file then __name__ == app (which is the name of this python file).

if __name__ == "__main__":
    app.run()
