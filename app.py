import streamlit as st
import pandas as pd
import pickle

# Load the model pipeline
model_pipeline = pickle.load(open('model_pipeline.pkl', 'rb'))

# Set page configuration
st.set_page_config(page_title="Customer Churn Prediction", page_icon="🔮")

# Header
st.title('🔮 Customer Churn Prediction')

st.write("""
Welcome to the Customer Churn Prediction app! This app helps you predict whether a customer will churn based on their details. 
Fill in the information below to get started.
""")

# Sidebar for inputs with brief instructions
st.sidebar.header("Insert Customer Details")

st.sidebar.write("Please provide the following details:")

CreditScore = st.sidebar.number_input('💳 Credit Score', min_value=0, max_value=1000, value=500)
Age = st.sidebar.number_input('🎂 Age', min_value=18, max_value=100, value=30)
Gender = st.sidebar.selectbox('👫 Gender', ['Male', 'Female'])
Geography = st.sidebar.selectbox('🌍 Geography', ['France', 'Germany', 'Spain'])
Tenure = st.sidebar.number_input('📅 Tenure', min_value=0, max_value=10, value=5)
Balance = st.sidebar.number_input('💰 Balance', min_value=0.0, value=0.0)
NumOfProducts = st.sidebar.number_input('📦 Number of Products', min_value=1, max_value=10, value=1)
HasCrCard = st.sidebar.selectbox('💳 Has Credit Card?', [0, 1])
IsActiveMember = st.sidebar.selectbox('✅ Is Active Member?', [0, 1])
EstimatedSalary = st.sidebar.number_input('💵 Estimated Salary', min_value=0.0, value=50000.0)

# Main area for displaying results
st.header("Prediction Results")

# Prepare the input data
input_data = pd.DataFrame({
    'CreditScore': [CreditScore],
    'Age': [Age],
    'Gender': [Gender],
    'Geography': [Geography],
    'Tenure': [Tenure],
    'Balance': [Balance],
    'NumOfProducts': [NumOfProducts],
    'HasCrCard': [HasCrCard],
    'IsActiveMember': [IsActiveMember],
    'EstimatedSalary': [EstimatedSalary]
})

# Prediction
if st.button('Predict 🔍'):
    try:
        prediction = model_pipeline.predict(input_data)
        if prediction[0] == 1:
            st.error('🚨 This customer is likely to churn.')
        else:
            st.success('✅ This customer is not likely to churn.')
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Add a footer
st.markdown("""
    ---
    Created with ❤️ by Gangaram Sahu
""")
