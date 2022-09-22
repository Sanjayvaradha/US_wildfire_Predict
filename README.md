# Canonical_US_wildfire

# Have wildfires become more or less frequent over time?

In Canonical.ipynb we can see
-> The count of wildfire is random over a period of year but the size of the wildfire is more frequent over years.

# The most and least fire-prone?
From the same notebook we can see the from the graph,

->when it comes to the fire counts the most fire prone state is Carlifornia and least is New Mexico
->When it comes to fire size the most is Alaska and least is Colorado.

# Given the size, location and date, can you predict the cause of a fire wildfire?

The prediction for this wildfire is shown by
-> Graph along with confusion matrix and classification report
-> Also model deployment using Flask API

The model is trained with important features prediction the column "STAT_CAUSE_DESCR"
REFERENCE

0->natural = ['Lightning']
1->accidental = ['Structure','Fireworks','Powerline','Railroad','Smoking','Children','Campfire','Equipment Use','Debris Burning']
2->malicious = ['Arson']
3->other = ['Missing/Undefined','Miscellaneous']

Random Forest Classifier (Bagging method) is used to predict the cause of the wildfire

Having the processing power, the accuracy of 61% was able to achieve

For inference part, the user can manually enter the following data to predict the cause of the fire
Data -> Latitude, Longitude, Fire size, Month, Date, Discovery date

The accuracy of the model can be improved by boosting method and adding more number of features.

# Flask deployment (Local host)

Instruction to use

The folder structures are

1.Template (which has (index.html)HTML code to view in website)
2.app.py - Python file implementing flask 
3.rf_models - zip format of the random forest classifier trained model

Run the app.py 

1. It will unzip the rf_models and load the model using pickle
2. The render_template will run the index.html file to view the website
3. Enter the following data in website and click submit button
4. At backend with the will help of FLASK model will predict the cause and the resut will be displayed on website


