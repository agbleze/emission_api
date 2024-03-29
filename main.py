from fastapi import FastAPI, Depends
from pydantic import BaseModel
import joblib
from sklearn.pipeline import Pipeline
from typing import List, Any, Optional, Tuple
import os
import pandas as pd
from carbon_emission import PredictionOutput, PredictionInput, CarbonEmissionModel
import uvicorn
# instantiate class
carbon_emision_model = CarbonEmissionModel()

# instantiate fastapi
app = FastAPI()

# root endpoint
@app.get("/")
async def get_api_description():
    return {"Description:": "This is a machine learning API for carbon emission prediction"}

# create prediction endpoint with post method
@app.post("/predict")
async def get_prediction(output: PredictionOutput = Depends(carbon_emision_model.predict)
                         ) -> PredictionOutput:
    return output


# load model when api starts
@app.on_event('startup')
async def startup():
    carbon_emision_model.load_model()

if __name__ == '__main__':
    uvicorn.run(app=app, port=8000, log_level='info')
#%%
# echo '{"parameter": {"state_name": "Bayela", "lga": 108, "sector": "RURAL", "credit_mean": 70, "income_mean": 600}}' | http POST http://127.0.0.1:8000/predict



# %%
