import streamlit as st

# App title
st.title("🌡️ Temperature Converter")

# Input value
temp = st.number_input("Enter the temperature:", format="%.2f")

# Input unit
from_unit = st.selectbox("Convert from:", ["Celsius", "Fahrenheit", "Kelvin"])

# Output unit
to_unit = st.selectbox("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion logic
def convert_temperature(value, from_u, to_u):
    if from_u == to_u:
        return value

    # Convert from input unit to Celsius first
    if from_u == "Fahrenheit":
        value = (value - 32) * 5 / 9
    elif from_u == "Kelvin":
        value = value - 273.15

    # Now convert from Celsius to output unit
    if to_u == "Fahrenheit":
        return (value * 9 / 5) + 32
    elif to_u == "Kelvin":
        return value + 273.15
    return value  # If to_unit is Celsius

# Button to convert
if st.button("Convert"):
    result = convert_temperature(temp, from_unit, to_unit)
    st.success(f"{temp} {from_unit} = {result:.2f} {to_unit}")
