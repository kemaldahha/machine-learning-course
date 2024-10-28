import pickle
from flask import Flask, request, jsonify

# DictVectorizer and LogisticRegressiom 
# model made in train.py
model_file = "model_C=1.0.bin"

with open(model_file, "rb") as f_in:
    dv, model = pickle.load(f_in)

# The web service is called 'churn'
app = Flask("churn")

# With this decorator we create a route /predict.
@app.route("/predict", methods=["POST"])
def predict():
    '''Takes customer data as json and returns json result with 
    churn_probability (float) and churn prediction (bool).'''
    # Store json from post request into customer dictionary
    customer = request.get_json()
    
    # This should go into another function. For now keep it here.
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5
    
    # Need to convert into python float and bool, 
    # since Flask cannot handle Numpy variables
    result = {
        "churn_probability": float(y_pred),
        "churn": bool(churn),
    }
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port="9696")
