
import streamlit as st
import joblib
import numpy as np

# Load models
heating_model = joblib.load("heating_load_model.pkl")
cooling_model = joblib.load("cooling_load_model.pkl")

st.title("EnerSketch")
st.subheader("AI-Powered Building Energy Performance Predictor")

st.write("""
EnerSketch is an AI-powered building energy performance prediction tool
designed to support architects during the early stages of design.

The application estimates heating and cooling loads based on key building
parameters, allowing users to explore energy-efficient design alternatives.
""")

# Inputs
x1 = st.number_input("Relative Compactness", value=0.98)
x2 = st.number_input("Surface Area", value=514.5)
x3 = st.number_input("Wall Area", value=294.0)
x4 = st.number_input("Roof Area", value=110.25)
x5 = st.number_input("Overall Height", value=7.0)
x6 = st.number_input("Orientation", value=2)
x7 = st.number_input("Glazing Area", value=0.25)
x8 = st.number_input("Glazing Distribution", value=3)

if st.button("Predict"):

    sample = np.array([[x1,x2,x3,x4,x5,x6,x7,x8]])

    heating = heating_model.predict(sample)[0]
    cooling = cooling_model.predict(sample)[0]

    st.success(f"Predicted Heating Load: {heating:.2f}")

    st.success(f"Predicted Cooling Load: {cooling:.2f}")

    st.subheader("Architectural Interpretation")

    if cooling < 20:
        st.write(
            "This design is predicted to have relatively low cooling demand and may be more energy-efficient."
        )
    else:
        st.write(
            "This design shows higher cooling demand. Consider adjusting orientation, glazing area, or overall building form."
        )

st.header("About the Dataset and Model")

st.write("""
Dataset:
UCI Energy Efficiency Dataset

Model:
Random Forest Regressor

The model was trained using building design variables such as
surface area, wall area, roof area, orientation, height,
and glazing characteristics.
""")

st.header("Architecture Relevance")

st.write("""
EnerSketch helps architects evaluate energy performance
during conceptual design stages before conducting detailed
energy simulations.

The tool encourages energy-conscious design decisions by
providing rapid feedback on heating and cooling demand.
""")

st.header("Limitations")

st.write("""
Predictions are based on the Energy Efficiency Dataset
and should be used as preliminary guidance only.

Results do not replace detailed building performance
simulations or professional energy analysis.
""")