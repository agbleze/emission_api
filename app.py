#%%
from fastapi import FastAPI, Depends
from pydantic import BaseModel
import joblib
from sklearn.pipeline import Pipeline
from typing import List, Any

class PredictionInput(BaseModel):
    parameter: List[Any]

class PredictionOutput(BaseModel):
    emission: float










