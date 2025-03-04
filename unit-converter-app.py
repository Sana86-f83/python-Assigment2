import streamlit as st
import base64
import os

st.set_page_config(
    page_title="UniScale ⚖️📏",
    page_icon="📏",
    layout="centered"
)
def load_css(file_name):
    css_path = os.path.join(os.getcwd(), file_name)
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    else:
        st.error(f"⚠️ CSS file not found: {file_name}")

load_css("styles.css")

# Function to Convert Local Image to Base64
def set_bg(local_img_path):
    if os.path.exists(local_img_path):
        with open(local_img_path, "rb") as img_file:
            encoded_string = base64.b64encode(img_file.read()).decode()
        bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-opacity:70%;
        }}
        </style>
        """
        st.markdown(bg_img, unsafe_allow_html=True)
    else:
        st.error(f"⚠️ Background image not found: {local_img_path}")

set_bg("images/background.jpg")


# Title and Description with Animations
st.markdown("<h1 class='title'>🌏 UniScale ⚖️ </h1>", unsafe_allow_html=True)
st.markdown("### <p class='description'>UniScale ⚖️ – Fast & easy unit conversion for length, weight, and time! 🚀</p>", unsafe_allow_html=True)

# Sidebar Image
st.sidebar.image('images/unit-converter.jpg', use_container_width=True)

# Unit Category Selection
category = st.sidebar.selectbox("⚖️ Select a Conversion", [
    "📏 Length", "⚖️ Weight", "🕰️ Time", "📐 Height", "🌡️ Temperature"
])

# **Show Selected Category as Heading**
st.markdown(f"<h2 class='category-heading'>{category} Conversion</h2>", unsafe_allow_html=True)

# Conversion Logic
def convert_units(category, value, unit):
    if category == "📏 Length":
       return value * 0.621371 if unit == "Kilometers to Miles" else value / 0.621371
    elif category == "⚖️ Weight":
        return value * 2.20462 if unit == "Kilograms to Pounds" else value / 2.20462
    elif category == "🕰️ Time":
        conversions = {
            "Seconds to Minutes": value / 60,
            "Minutes to Seconds": value * 60,
            "Minutes to Hours": value / 60,
            "Hours to Minutes": value * 60,
            "Hours to Days": value / 24,
            "Days to Hours": value * 24
        }
        return conversions.get(unit, value)
    elif category == "📐 Height":
        return value * 3.28084 if unit == "Meters to Feet" else value / 3.28084 
    elif category == "🌡️ Temperature":
        return (value * 9/5) + 32 if unit == "Celsius to Fahrenheit" else (value - 32) * 5/9


if category == "📏 Length":
    unit = st.selectbox("📏 Select a Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "⚖️ Weight":
    unit = st.selectbox("⚖️ Select a Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "🕰️ Time":
    unit = st.selectbox("🕰️ Select a Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])
elif category == "📐 Height":
    unit = st.selectbox("📐 Select a Conversion", ["Meters to Feet", "Feet to Meters"])
elif category == "🌡️ Temperature":
    unit = st.selectbox("🌡️ Select a Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])


value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"{value} {unit.split(' to ')[0]} is equal to {result:.2f} {unit.split(' to ')[1]}")

st.markdown("""
    <hr>
    <div style="text-align: center; padding: 10px; font-size: 18px; color: white;">
        © 2025 | Developed by <b style='color:yellow;font-size:20px;'>Sana Faisal</b> ⚖️
        <br>
        <a href="https://www.linkedin.com/in/sana-faisal-developer/" target="_blank" style="color: #4CAF50; text-decoration: none;">
            Connect on LinkedIn
        </a>
    </div>
""", unsafe_allow_html=True)

