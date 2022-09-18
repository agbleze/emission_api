#%%
from fastapi import FastAPI, Depends
from pydantic import BaseModel
import joblib
from sklearn.pipeline import Pipeline
from typing import List, Any, Optional, Tuple
import os
import pandas as pd

#%%
#loaded_model = joblib.load("model_used.model")

#%%
#model_path = os.path.join(os.path.dirname(__file__), "model_used.model")

#%%
#joblib.load(model_path)

#%%
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
        #model, targets = loaded_model
        self.model = loaded_model
        #self.targets = targets
        
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
        

carbon_emision_model = CarbonEmissionModel()

app = FastAPI()
@app.post("/predict")
async def get_prediction(output: PredictionOutput = Depends(carbon_emision_model.predict)
                         ) -> PredictionOutput:
    return output

@app.on_event('startup')
async def startup():
    carbon_emision_model.load_model()





"""
TODO:
1. Send Dict of values to API
1.i when submit button is clicked, it put values selected
into dict and makes API request
2. API recieves sent dict and convert to df
3. API feeds df into model for prediction
4. API returns prediction
5. Prediction is shown on the dashboard

"""        
# app = FastAPI()
# @app.post("/predict")
# async def get_prediction(input: PredictionInput):
#     prediction_inputs = input.parameter
#     prediction_inputs_df = pd.DataFrame(data=prediction_inputs, index=[0])
    
    
    
    

    
    
    
    
    

#%%
# def make_prediction(state_selected, lga_selected, sector_selected, credit_amt, 
#                     income_amt, predict_button):
#     ctx = callback_context
#     button_clicked = ctx.triggered[0]['prop_id'].split('.')[0]
    
#     # prediction_input = [state_selected, lga_selected, sector_selected, credit_amt,
#     #                     income_amt]
    
    
    
#     prediction_inputs = {'state_name': state_selected, 'lga': lga_selected, 
#                          'sector': sector_selected, 'credit_mean': credit_amt, 
#                          'income_mean': income_amt
#                          }
#     prediction_inputs_df = pd.DataFrame(data=prediction_inputs, index=[0])

    
#     if ((not button_clicked) or (button_clicked != 'id_predict_emission') 
#         or (not any(prediction_inputs_df)) or (not predict_button)
#         ):
#         PreventUpdate
        
#     if button_clicked == 'id_predict_emission':
        
#         if not all(prediction_inputs_df):
#             PreventUpdate
            
#             # message = ('All parameters must be provided. Either some values have not \
#             #             been provided or invalid values were provided. Please select the \
#             #            right values for all parameters from the dropdown. \
#             #             Then, click on predict clicks button to \
#             #             predict number of clicks'
#             #            )
#             # return True, message, dash.no_update
        
#         if all(prediction_inputs_df):
#             result = loaded_model.predict(prediction_inputs_df)[0]
#             prediction = round(result)
#             prediction_desc = f'Household with the selected characteristics is predicted to emit {prediction} kg carbon dioxide'
#             return (prediction, prediction_desc) #False, dash.no_update, prediction
        
 
 #%%
# import pandas as pd 
# prediction_inputs = {'state_name': 'Bayela', 'lga': 108, 
#                     'sector': 'RURAL', 'credit_mean': 70, 
#                     'income_mean': 600
#                     }

#{"state_name": "Bayela", "lga": 108, "sector": "RURAL", "credit_mean": 70, "income_mean": 600}


# prediction_inputs_df = pd.DataFrame(data=prediction_inputs, index=[0])       
   
# #%%
# if not all(prediction_inputs_df):
#     print('Not ready')
# else:
#     print('Go!')
            
                    
# #%%
# loaded_model.predict(prediction_inputs_df)[0]


#%%
# echo '{"parameter": {"state_name": "Bayela", "lga": 108, "sector": "RURAL", "credit_mean": 70, "income_mean": 600}}' | http POST http://127.0.0.1:8000/predict

# %%
