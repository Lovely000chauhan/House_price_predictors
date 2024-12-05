## Project Overview

The **House Price Predictor** uses a regression model to predict house prices based on features like:
  1.  area: float
  2.  bedrooms: int
  3.  bathrooms: int
  4.  stories: int
  5.  mainroad: int
  6.  guestroom: int
  7.  basement: int
  8.  airconditioning: int
  9.  parking: int
  10.  prefarea: int
  11.  furnishingstatus: int
The model was trained using historical housing data and can be used to predict the price of a house given a set of input features.
# Technologies Used

- **Python 3.x**: The programming language used for the project.
- **pandas**: Data manipulation and analysis.
- **scikit-learn**: A library for machine learning that provides easy-to-use tools for regression and model evaluation.
- **matplotlib** / **seaborn**: Libraries for data visualization.
- **Jupyter Notebook** (optional): For interactive development and exploration.

 ## Bash command to rum app.py in Command Prompt
  1. cd C:\Users\YourUsername\Documents\project
  2. dir
  3. Activate the Virtual Environment
  To activate the environment, use the following command:
    .\myenv\Scripts\activate
  4. pip install fastapi uvicorn
  5. uvicorn main:app --reload
  6. 

