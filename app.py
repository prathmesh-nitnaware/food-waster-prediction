import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.exceptions import NotFittedError

# --- Page Configuration ---
st.set_page_config(
    page_title="Food Wastage Predictor",
    page_icon="🍎",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Load Model with Comprehensive Validation ---
@st.cache_resource
def load_model():
    try:
        saved_data = joblib.load('xgboost_food_wastage_model.pkl')

        # Validate the structure
        if not isinstance(saved_data, dict):
            raise ValueError("Saved file is not a dictionary")

        required_keys = {'model', 'scaler', 'metadata'}
        if not required_keys.issubset(saved_data.keys()):
            missing = required_keys - set(saved_data.keys())
            raise ValueError(f"Missing keys in saved file: {missing}")

        # Validate scaler
        if not hasattr(saved_data['scaler'], 'transform'):
            raise ValueError("Scaler object is invalid or not properly saved")

        # Validate model
        if not hasattr(saved_data['model'], 'predict'):
            raise ValueError("Model object is invalid")

        return saved_data

    except FileNotFoundError:
        st.error("❌ Model file not found. Please ensure 'xgboost_food_wastage_model.pkl' exists.")
        return None
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        return None

# Load the model
saved_data = load_model()

# --- App Title and Description ---
st.title("🍎 Food Wastage Prediction App")
st.markdown("""
This app predicts potential food wastage based on expiry dates and perishability.
Enter the food details below to get a wastage prediction.
""")

# Stop if model didn't load
if saved_data is None:
    st.stop()

# Extract components
model = saved_data['model']
scaler = saved_data['scaler']
features = saved_data['metadata']['features']

# --- Sidebar with Model Info ---
with st.sidebar:
    st.header("Model Information")
    st.markdown(f"""
    - **Algorithm**: {saved_data['metadata']['model_type']}
    - **Training Date**: {saved_data['metadata']['training_date']}
    - **Features Used**: {', '.join(features)}
    - **Training Score**: {saved_data['metadata'].get('training_score', 'N/A')}
    """)

    st.markdown("---")
    st.header("How to Use")
    st.markdown("""
    1. Enter the days until expiry
    2. Select if the food is perishable
    3. Click 'Predict Wastage'
    4. View the prediction and recommendations
    """)

# --- Main Input Form ---
with st.form("prediction_form"):
    st.subheader("Food Item Details")

    col1, col2 = st.columns(2)
    with col1:
        days_expiry = st.number_input(
            "Days Until Expiry",
            min_value=0,
            max_value=30,
            value=3,
            help="Number of days until the food expires"
        )
    with col2:
        is_perishable = st.selectbox(
            "Is Perishable?",
            options=[("Yes", 1), ("No", 0)],
            format_func=lambda x: x[0],
            help="Select if the food is perishable"
        )

    submit_button = st.form_submit_button("Predict Wastage")

# --- Prediction and Results ---
if submit_button:
    try:
        # Create input DataFrame
        input_data = pd.DataFrame({
            'Days_Until_Expiry': [days_expiry],
            'Is_Perishable': [is_perishable[1]]
        })

        # Verify features match
        if list(input_data.columns) != features:
            input_data = input_data[features]  # Reorder columns

        # Make prediction
        scaled_input = scaler.transform(input_data)
        prediction = model.predict(scaled_input)[0]

        # Display results
        st.success(f"📊 Predicted Wastage: {prediction:.2f} units")

        # Risk interpretation
        if prediction > 10:
            st.warning("⚠️ High wastage risk! Prioritize immediate redistribution.")
            st.markdown("""
            **Recommended Actions:**
            - Contact food banks immediately
            - Offer discounts for quick sale
            - Process into preserved goods
            """)
        elif prediction > 5:
            st.info("ℹ️ Moderate wastage risk. Monitor closely.")
            st.markdown("""
            **Recommended Actions:**
            - Plan for redistribution in 1-2 days
            - Store in optimal conditions
            """)
        else:
            st.success("✅ Low wastage risk. Safe for standard storage.")
            st.markdown("""
            **Recommended Actions:**
            - Regular monitoring is sufficient
            - Maintain current storage conditions
            """)

        # Show raw prediction details for advanced users
        with st.expander("Advanced Details"):
            st.write("Input Data:", input_data)
            st.write("Scaled Input:", scaled_input)
            st.write("Model Type:", type(model).__name__)

    except NotFittedError:
        st.error("❌ Model or scaler not properly fitted. Please retrain the model.")
    except Exception as e:
        st.error(f"❌ Prediction failed: {str(e)}")
        st.write("Debug Information:")
        st.write(f"- Input Data: {input_data.to_dict() if 'input_data' in locals() else 'Not created'}")
        st.write(f"- Expected Features: {features}")

# --- Example Predictions ---
st.markdown("---")
st.subheader("Example Predictions")
example_data = [
    {"Days": 2, "Perishable": "Yes", "Predicted Wastage": "12.5 units", "Risk": "High"},
    {"Days": 5, "Perishable": "No", "Predicted Wastage": "3.2 units", "Risk": "Low"},
    {"Days": 1, "Perishable": "Yes", "Predicted Wastage": "18.7 units", "Risk": "High"}
]

st.table(pd.DataFrame(example_data))

# --- Footer ---
st.markdown("---")
st.caption("""
**Note**: This prediction tool is based on historical data and provides estimates.
For critical decisions, consult with food safety experts.
""")
