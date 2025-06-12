import streamlit as st

# Title
st.title("📏 Distance Converter")

# Supported units and their values in meters
units_in_meters = {
    "Millimeter": 0.001,
    "Centimeter": 0.01,
    "Meter": 1.0,
    "Kilometer": 1000.0,
    "Inch": 0.0254,
    "Foot": 0.3048,
    "Yard": 0.9144,
    "Mile": 1609.34
}

# Input from user
distance = st.number_input("Enter the distance:", format="%.4f")

from_unit = st.selectbox("Convert from:", list(units_in_meters.keys()))
to_unit = st.selectbox("Convert to:", list(units_in_meters.keys()))

# Conversion function
def convert_distance(value, from_u, to_u):
    value_in_meters = value * units_in_meters[from_u]
    converted_value = value_in_meters / units_in_meters[to_u]
    return converted_value

# Convert on button click
if st.button("Convert"):
    result = convert_distance(distance, from_unit, to_unit)
    st.success(f"{distance} {from_unit} = {result:.4f} {to_unit}")
