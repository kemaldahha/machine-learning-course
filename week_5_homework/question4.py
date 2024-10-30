import pickle
from flask import Flask, request, jsonify


with open("model1.bin", "rb") as f_model, open("dv.bin", "rb") as f_dv:
    model = pickle.load(f_model)
    dv = pickle.load(f_dv)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    client = request.get_json()
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1].round(3)
    
    result = {
        "probability": y_pred
    }
    
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port="9696")