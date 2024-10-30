import requests


customer = {
    'gender': 'male',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no_internet_service',
    'streamingtv': 'no_internet_service',
    'streamingmovies': 'no_internet_service',
    'contract': 'one_year',
    'paperlessbilling': 'no',
    'paymentmethod': 'month-to-month',
    'tenure': 4,
    'monthlycharges': 190.7,
    'totalcharges': 2580.35
 }

host = "churn-serving-dev.eu-west-1.elasticbeanstalk.com"

print(requests.post(f"http://{host}/predict", json=customer).text)
