
import streamlit as st
import pickle

# Load the model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Predictor")

# Input fields
area = st.number_input("Living Area (GrLivArea)", value=1000)
bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)
bath = st.selectbox("Full Bathrooms", [1, 2, 3])

# Predict button
if st.button("Predict"):
    result = model.predict([[area, bedrooms, bath]])
    st.success(f"Estimated Sale Price: ${int(result[0])}")
