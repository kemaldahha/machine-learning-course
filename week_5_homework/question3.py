import pickle


with open("model1.bin", "rb") as f_model, open("dv.bin", "rb") as f_dv:
    model = pickle.load(f_model)
    dv = pickle.load(f_dv)

client = {"job": "management", "duration": 400, "poutcome": "success"}

X = dv.transform(client)

print(model.predict_proba(X)[:, 1].round(3))