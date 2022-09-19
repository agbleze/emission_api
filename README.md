# Machine learning API for predicting Household carbon emission 
This repo contains code for machine learning API for carbon emission. The complete project pipeline to developed the model separated in different repository. This repositiory shows the final stage of using the model developed to create an API with FASTAPI.


### FastAPI endpoints
The code for the developing FastAPI is in main.py file. It has two main endpoints as follows


i. Root endpoint ("/"): with a get method that receives no parameter and returns the description of the API.


ii. Predict endpoint ("/predict"): with a post method accepts a number of parameters as json and return prediction of carbon emission. 

An example of the what can used to call the API predict endpoint is *'{"parameter": {"state_name": "Bayela", "lga": 108, "sector": "RURAL", "credit_mean": 70, "income_mean": 600}}'.*

The state_name is the name of a state in Nigeria, lga is Local Government Area in Nigeria, sector can be either "RURAL" or "URBAN", credit_mean is the average credit (loan) received by a household and income_mean is average income of a household.


### How to run the code for the API
It is possible to the code on your local machine to have a experience of it works. In order to run the code, the following instructions can be followed;


1. Create a virtual environment 
In your terminal create a virtual environment and nagivate into it. A virtual environment can be created below in mac

  ```python3 -m venv {provide a name for virtual environment}```. Eg  ```python3 -m venv virt```
  
In this exercise, let assume the virtual environment was name virt. The next will be to navigate into the virtual environment

  ```cd virt ```
  
  
 
 2. Activate the virtual environment as follows (this based on Mac)
  
   ```source bin\activate ```



3. Clone repository into the virtual environment


```git clone https://github.com/agbleze/emission_api.git```



4. Install packages in the requirements.txt file which were used to develop the project

```pip install -r requirements.txt```



5. Run the code for the API 

```python main.py```

This will run the API locally and with the link that it produces, calls can be made to the API. The API link will be something similar to http://127.0.0.1:8000   



6. API calls to endpoints
With the API now running in the background, open a new terminal and make API calls as follows


i. Predict emission goes to "/predict" endpoint.  Example:

```echo '{"parameter": {"state_name": "Bayela", "lga": 108, "sector": "RURAL", "credit_mean": 70, "income_mean": 600}}' | http POST http://127.0.0.1:8000/predict```



