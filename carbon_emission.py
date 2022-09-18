from fastapi import FastAPI, Depends
from pydantic import BaseModel
import joblib
from sklearn.pipeline import Pipeline
from typing import List, Any, Optional, Tuple
import os
import pandas as pd


class PredictionInput(BaseModel):
    parameter: dict

class PredictionOutput(BaseModel):
    emission: float


class CarbonEmissionModel:
    model: Optional[Pipeline]
    
    
    def load_model(self):
        """Load the model
        """
        model_file = os.path.join(os.path.dirname(__file__), "model_used.model")
        loaded_model: Pipeline = joblib.load(model_file)
        self.model = loaded_model
        
    async def predict(self, input: PredictionInput) -> PredictionOutput:
        """Runs a prediction

        Args:
            PredictionInput (_type_): _description_

        Returns:
            PredictionOutput: _description_
        """
        if not self.model:
            raise RuntimeError("Model is not loaded")
        prediction_inputs = input.parameter
        prediction_inputs_df = pd.DataFrame(data=prediction_inputs, index=[0])
    
        prediction = self.model.predict(prediction_inputs_df)
        emission = prediction[0]
        return PredictionOutput(emission=emission)
        





