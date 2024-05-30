import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from PIL import UnidentifiedImageError
def load_image2(url, resize_to=(250, 250)):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img = img.resize(resize_to)
        return img
    except (requests.exceptions.RequestException, UnidentifiedImageError):
        return None
st.markdown("""
    <style>
    .stButton > button {
        background-color: #FFF4E6; /* Green */
        border: none;
        color: black;
        padding: 8px 12px; /* Reduced padding for thinner button */
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    .stButton > button:hover {
        color: black; /* Text color becomes black on hover */
    }
    .stButton > button:active {
        color: black; /* Text color becomes black when button is clicked */
    }
    .stButton.buy-cookbook > button {
        background-color: #FFB6C1; /* Light Pink */
    }
    </style>
    """, unsafe_allow_html=True)
        

st.title("Vegan AI for Chefs")

meal_choice = st.selectbox("What are you planning to make?", ["", "Breakfast", "Lunch", "Dinner", "Dessert"])
cuisine_choice = st.selectbox("Do you have a specific cuisine in mind? (optional)", ["", "American", "Asian", "Italian", "Mexican", "Indian", "Other"])
flavor_profile = st.selectbox("What flavor profile do you prefer?", ["", "Savory", "Sweet", "Spicy", "Sour", "Herbal"])

st.write("Professional Vegan Chef's Recipe and Recommendation")

if cuisine_choice in ["", "Asian"] and meal_choice in ["Lunch", "Dinner"] and flavor_profile in ['Savory', 'Spicy']:
    st.subheader("**Recipe:** Szechuan Tofu Stir Fry with Spicy Garlic Sauce")
    img_url = "https://savoryspin.com/wp-content/uploads/2021/04/PlantBased-Cashew-Curry.jpg"
    img = load_image2(img_url)
    st.image(img, caption="Szechuan Tofu Stir Fry")
    import webbrowser
    if st.button("Buy Chef Doug's Cookbooks"):
    webbrowser.open_new_tab('https://www.amazon.com/stores/author/B00E5FEE5S/allbooks?ingress=0&visitId=131f99ec-8628-4c07-85cd-4f4dd8d2ff1d') 

if cuisine_choice in ["", "Italian"] and meal_choice in ["Lunch", "Dinner"] and flavor_profile in ['Savory', 'Herbal']:
    st.subheader("**Recipe:** Vegan Mushroom Risotto")
    st.image("https://veganhuggs.com/wp-content/uploads/2018/02/mushroom-risotto-featured.jpg", caption="Vegan Mushroom Risotto")
    st.write("**Cookbooks to Buy:** [Doug McNish's Cookbooks](https://www.amazon.com/stores/author/B00E5FEE5S/allbooks?ingress=0&visitId=131f99ec-8628-4c07-85cd-4f4dd8d2ff1d)")

if cuisine_choice in ["", "Mexican"] and meal_choice in ["Lunch", "Dinner"] and flavor_profile in ['Savory', 'Spicy']:
    st.subheader("**Recipe:** Vegan Enchiladas with Cashew Cheese")
    st.image("https://i2.wp.com/www.evolvingtable.com/wp-content/uploads/2019/01/Black-Bean-Spinach-Enchiladas_1.jpg", caption="Vegan Enchiladas")
    st.write("**Cookbooks to Buy:** [Doug McNish's Cookbooks](https://www.amazon.com/stores/author/B00E5FEE5S/allbooks?ingress=0&visitId=131f99ec-8628-4c07-85cd-4f4dd8d2ff1d)")
