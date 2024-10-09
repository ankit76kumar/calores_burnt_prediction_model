
import numpy as np 
import pickle 

# Load the model
loaded_model = pickle.load(open("C:/Users/HP/OneDrive/Desktop/project/m_l projects/calories_burnt_prediction/calories_burnt_predictions.sav", "rb"))

# Function to get validated input
def get_input(prompt, input_type=float, condition=lambda x: True):
    while True:
        try:
            value = input_type(input(prompt))
            if condition(value):
                return value
            else:
                print("Input does not meet the required condition. Please try again.")
        except ValueError:
            print("Invalid input type. Please enter a valid value.")

# Gather user input
Gender = get_input("Enter your gender (0 for male, 1 for female): ", int, lambda x: x in [0, 1])
Age = get_input("Enter your age: ", int, lambda x: x > 0)
Height = get_input("Enter your height in cm: ", float, lambda x: x > 0)
Weight = get_input("Enter your weight in kg: ", float, lambda x: x > 0)
Duration = get_input("Enter your duration of workout in minutes: ", float, lambda x: x > 0)
Heart_Rate = get_input("Enter your heart rate: ", float, lambda x: x > 0)
Body_Temp = get_input("Enter your body temperature in °C: ", float, lambda x: x > 0)

# Prepare input data
input_data = [Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp]

# Make prediction
result1 = loaded_model.predict([input_data])
print(f"Total calories burnt in this day: {result1[0]:.2f} calories")

