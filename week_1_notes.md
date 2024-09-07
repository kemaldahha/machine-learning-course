# Week 1

## 1.1 [Introduction to Machine Learning](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/01-intro/01-what-is-ml.md)

- Example: recommending a price for a car, given its properties such as: age, mileage, model, no. of doors, etc.
- Patterns can be found in the data which can be modelled
- Essence of ML: given data, have a model learn patterns in the data
- Data consists of:
    - Features: what we know about cars (i.e. its properties)
    - Target: what we want to predict (i.e. its price)
- User can provide information on a car they want to sell. This data is extracted. Price (target) is predicted and suggested to the user as an appropriate price.

## 1.2 [ML vs Rule-Based Systems](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/01-intro/02-ml-vs-rules.md)

This lesson will cover a comparison between rule-based and ML systems. The example used is an e-mail spam detection system.

We want to develop a spam detection system using a classifier.

One approach is to take all the spam messages and try to identify what makes a message spam. We could come up with explicit rules based on the sender, subject, etc. However spam messages evolve and require frequent updates, leading inevitably to a myriad of rules and logic which will be a nightmare to maintain.

Alternatively, we can use Machine Learning. How do we do this? We get the data (all the e-mails), define and calculate features, train and use the model.
- Getting the data: we could have a spam button which users can press to indicate an e-mail is spam
- Defining features: we could start off with some rules, e.g. length of subject greater than 10, length of body greater than 10, sender has a certain domain, sender e-mail address has a certain pattern, and so on. These are just some examples of features, there can be more/different ones. Then for a given e-mail, we can put its data in a vector: $[1, 1, 0, 0, 1, 1]$, This would indicate then the length of the subject is greater than 10, length of body is greater than 10, etc. Say that the user designated this e-mail as spam, then the target variable is also $1$. We do this for many e-mails and get a matrix with the features and a vector with target variables.
- Train model: features and target variables go into ML model. We fit/train the model and determine some unknown coefficients that minimize the error between predictions and the target.
- Use model: now that the model has been trained, we can put new data into it and predict the target. 

## 1.3 [Supervised Machine Learning](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/01-intro/03-supervised-ml.md)



## 1.4 [CRISP-DM](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/01-intro/04-crisp-dm.md)



## 1.5 [The Modelling Step (Model Selection Process)](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/01-intro/05-model-selection.md)



## 1.6 [Setting up the Environment](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/01-intro/06-environment.md)



## 1.7 [Introduction to NumPy](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/01-intro/07-numpy.md)



## 1.8 [Linear Algebra Refresher](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/01-intro/08-linear-algebra.md)



## 1.9 [Introduction to Pandas](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/01-intro/09-pandas.md)



## 1.10 [Summary](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/01-intro/10-summary.md)



## 1.11 [Homework](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/01-intro/homework.md)


