# Machine learning API for predicting Household carbon emission 
This repo contains code for machine learning API for carbon emission. The complete project pipeline to developed the model separated in different repository. This repositiory shows the final stage of using the model developed to create an API with FASTAPI.


### FastAPI endpoints
The code for the developing FastAPI is in main.py file. It has two main endpoints as follows


i. Root endpoint ("/"): with a get method that receives no parameter and returns the description of the API.


ii. Predict endpoint ("/predict"): with a post method accepts a number of parameters as json and return prediction of carbon emission. 

An example of the what can used to call the API predict endpoint is *'{"parameter": {"state_name": "Bayela", "lga": 108, "sector": "RURAL", "credit_mean": 70, "income_mean": 600}}'.*

The state_name is the name of a state in Nigeria, lga is Local Government Area in Nigeria, sector can be either "RURAL" or "URBAN", credit_mean is the average credit (loan) received by a household and income_mean is average income of a household.


### How to run the code for the API
It is possible to the code on your local machine to have a experience of it works. In order to run the code, the following instructions can be followed

