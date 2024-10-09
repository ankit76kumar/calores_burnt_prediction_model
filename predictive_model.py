# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:46:41 2024

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

# Set page layout to wide
st.set_page_config(page_title="Calories Burnt Prediction Web App", layout="wide")

# Load the pre-trained model
loaded_model = pickle.load(open("C:/Users/HP/OneDrive/Desktop/project/m_l projects/calories_burnt_prediction/calories_burnt_predictions.sav", "rb"))

# Creating a web page
def main():
    # Giving a title to the webpage
    st.title("Calories Burnt Prediction Web App")
    
    # Getting input data from the user
    Gender = st.selectbox("Select your gender:", options=[0, 1], format_func=lambda x: "Male" if x == 0 else "Female")
    Age = st.number_input("Enter your age:", min_value=1, step=1)
    Height = st.number_input("Enter your height in cm:", min_value=1.0, step=0.1)
    Weight = st.number_input("Enter your weight in kg:", min_value=1.0, step=0.1)
    Duration = st.number_input("Enter your duration of workout in minutes:", min_value=1.0, step=0.1)
    Heart_Rate = st.number_input("Enter your heart rate:", min_value=1, step=1)
    Body_Temp = st.number_input("Enter your body temperature in °C:", min_value=0.1, step=0.1)

    # Code for prediction
    prediction = ""

    # Create a button for prediction
    if st.button("Calculate Calories Burnt"):
        # Prepare input data for prediction
        input_data = np.array([Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp]).reshape(1, -1)
        
        # Make prediction
        result = loaded_model.predict(input_data)
        prediction = f"Total calories burnt: {result[0]:.2f} calories"
    
    # Display the prediction result
    if prediction:
        st.success(prediction)

if __name__ == "__main__":
    main()

    

    
    

