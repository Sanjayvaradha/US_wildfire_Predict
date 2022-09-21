import numpy as np
from flask import Flask, request, render_template
import pickle
import zipfile

folder_to_be_unzipped = 'models_unzipped'
with zipfile.ZipFile('C:\\Users\\sanja\\app\\fire_prediction\\rf_models.zip', 'r') as zip_ref:
    zip_ref.extractall(folder_to_be_unzipped)


# Create an app object using the Flask class.
app = Flask(__name__)

# Load the trained model. (Pickle file)
model = pickle.load(
    open("C:\\Users\\sanja\\app\\fire_prediction\\models_unzipped\\rf_model\\randomforest_model.pkl", 'rb'))

causes = {}
incidents = ['Natural', 'Accidental', 'Malicious', 'Other']

for i, cause in enumerate(incidents):
    causes[i] = cause


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    probability = []
    # Convert string inputs to float.
    int_features = [float(x) for x in request.form.values()]
    features = np.array(int_features)
    features = features.reshape(1, 6)

    temp = model.predict_proba(features)

    for i in range(len(temp)):
        probability.append(temp[i][0][1])

    maximum = max(probability)
    index_num = probability.index(maximum)
    output = causes[index_num]
    print(output)

    return render_template('index.html', prediction_text='Fire caused by {}'.format(output))


if __name__ == "__main__":
    app.run()
