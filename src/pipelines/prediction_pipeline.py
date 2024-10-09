## creating api for frontend and integrate with pipeline
import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.logger import logging

class PredictPipeline:
    def __init__(self):
        # Define the path where the model and preprocessor were saved
        self.model_path = os.path.join("artifacts", "model.pkl")
        self.preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
    
    def predict(self, features):
        try:
            # Load the pre-trained model and preprocessor
            logging.info("Loading preprocessor and model for prediction")
            model = load_object(self.model_path)
            preprocessor = load_object(self.preprocessor_path)

            # Preprocess the input features
            logging.info("Preprocessing input features")
            data_scaled = preprocessor.transform(features)

            # Make predictions using the loaded model
            logging.info("Making predictions")
            predictions = model.predict(data_scaled)

            return predictions
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            raise CustomException(e,sys)
        
# with front end creating one more class
# from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

# Create an instance of CustomData with the input features
# for mapping
class CustomData:
    def __init__(self, 
                 carat: float, 
                 depth: float, 
                 table: float, 
                 x: float, 
                 y: float, 
                 z: float, 
                 cut: str, 
                 color: str, 
                 clarity: str):
        
        # Initialize the instance variables
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        """Convert the custom data to a DataFrame for model prediction."""
        import pandas as pd
            
        try:
                # Create a DataFrame from the instance variables
                data = {
                    'carat': [self.carat],
                    'depth': [self.depth],
                    'table': [self.table],
                    'x': [self.x],
                    'y': [self.y],
                    'z': [self.z],
                    'cut': [self.cut],
                    'color': [self.color],
                    'clarity': [self.clarity]
                }
                
                return pd.DataFrame(data)
            
        except Exception as e:
                logging.error("Error converting custom data to DataFrame", exc_info=True)
                raise CustomException(e, sys)


                
            
