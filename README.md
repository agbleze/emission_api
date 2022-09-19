# Machine learning API for predicting Household carbon emission 
This repo contains code for machine learning API for carbon emission. The complete project pipeline to developed the model separated in different repository. This repositiory shows the final stage of using the model developed to create an API with FASTAPI.


### FastAPI endpoints
The code for the developing FastAPI is in main.py file. It has two main endpoints as follows


i. Root endpoint ("/"): with a get method that receives no parameter and returns the description of the API.


ii. Predict endpoint ("/predict"): with a post method accepts a number of parameters as json and return prediction of carbon emission
