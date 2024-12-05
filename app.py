import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from sklearn.preprocessing import StandardScaler

app = FastAPI()

# Load the scaler and model from pickle files
pickle_filename_scaler = "scaler.pkl"
pickle_filename_data = "housing_data.pkl"

with open("lasso_model.pkl", 'rb') as file:
    loaded_model = pickle.load(file)

# Load the scaler
with open(pickle_filename_scaler, 'rb') as file:
    loaded_scaler = pickle.load(file)

# Pydantic model for input validation
class Pricing(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: int
    guestroom: int
    basement: int
    airconditioning: int
    parking: int
    prefarea: int
    furnishingstatus: int

@app.get('/')
def index():
    return {'message': 'Welcome to the House Pricing API'}

@app.post('/predict')
def prediction(data: Pricing):
    # Convert the Pydantic model to a dictionary
    data_dict = data.dict()
    print(data_dict)

    # Extract the features from the request data
    features = [
        data_dict["area"],
        data_dict["bedrooms"],
        data_dict["bathrooms"],
        data_dict["stories"],
        data_dict["mainroad"],
        data_dict["guestroom"],
        data_dict["basement"],
        data_dict["airconditioning"],
        data_dict["parking"],
        data_dict["prefarea"],
        data_dict["furnishingstatus"]
    ]

    # Scale the features using the loaded scaler
    scaled_features = loaded_scaler.transform([features])

    # Make the prediction using the loaded model
    prediction = loaded_model.predict(scaled_features)

    # Return the prediction as a JSON response
    return {"prediction": prediction[0].tolist()}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
