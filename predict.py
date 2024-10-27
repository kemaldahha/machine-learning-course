import pickle

model_file = "model_C=1.0.bin"

with open(model_file, "rb") as f_in:
    dv, model = pickle.load(f_in)

customer = {
    'gender': 'male',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'yes',
    'phoneservice': 'yes',
    'multiplelines': 'no',
    'internetservice': 'no',
    'onlinesecurity': 'no_internet_service',
    'onlinebackup': 'no_internet_service',
    'deviceprotection': 'no_internet_service',
    'techsupport': 'no_internet_service',
    'streamingtv': 'no_internet_service',
    'streamingmovies': 'no_internet_service',
    'contract': 'two_year',
    'paperlessbilling': 'no',
    'paymentmethod': 'mailed_check',
    'tenure': 12,
    'monthlycharges': 19.7,
    'totalcharges': 258.35
 }

X = dv.transform([customer])
y_pred = model.predict_proba(X)[0, 1]

print("input", customer)
print("churn probability", y_pred)