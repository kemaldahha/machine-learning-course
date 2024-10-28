import requests


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

print(requests.post("http://localhost:9696/predict", json=customer).text)
