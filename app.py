import streamlit as st
import pandas as pd
import joblib

# Set the title and header of the Streamlit app
st.title("Local Food Wastage Management System")
st.header("Predicting the Quantity of Food to be Claimed")
st.markdown("---")

# 1. Load the trained machine learning model
# The model file 'best_regressor_model.joblib' should be in the same directory as this app.py file.
try:
    loaded_model = joblib.load('best_regressor_model.joblib')
except FileNotFoundError:
    st.error("Error: The model file 'best_regressor_model.joblib' was not found.")
    st.stop() # Stop the app if the model file is not found

# 2. Create the user input form
st.subheader("Enter Food Listing Details")

# Input for numerical feature
quantity = st.number_input("Enter the quantity of food listed:", min_value=1, value=5, step=1)

# Input for categorical features
city = st.selectbox("Select the city:", ('Bangalore', 'Chennai', 'Delhi', 'Mumbai'))
provider_type = st.selectbox("Select the provider type:", ('Individual', 'Restaurant'))

# 3. Create a button to trigger the prediction
if st.button("Predict Quantity to be Claimed"):
    # 4. Prepare the user's input data for the model
    # Create a DataFrame with the same column names and order as the training data
    
    # Initialize all city and provider columns to 0
    data = {
        'quantity_listed': [quantity],
        'city_Chennai': [0],
        'city_Delhi': [0],
        'city_Mumbai': [0],
        'provider_type_Restaurant': [0]
    }
    
    # Create the DataFrame
    input_df = pd.DataFrame(data)
    
    # One-hot encode the city and provider_type input to match the model's features
    # Note: We only set the value to 1 for the selected options
    if city == 'Chennai':
        input_df['city_Chennai'] = 1
    elif city == 'Delhi':
        input_df['city_Delhi'] = 1
    elif city == 'Mumbai':
        input_df['city_Mumbai'] = 1
    
    if provider_type == 'Restaurant':
        input_df['provider_type_Restaurant'] = 1

    # 5. Make the prediction
    predicted_quantity = loaded_model.predict(input_df)

    # 6. Display the prediction result
    st.success(f"Based on your input, the predicted quantity of food to be claimed is: {predicted_quantity[0]:.2f} units.")
