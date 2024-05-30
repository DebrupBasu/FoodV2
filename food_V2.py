import streamlit as st
from PIL import Image, UnidentifiedImageError
import requests
import subprocess
from io import BytesIO

import streamlit as st

import streamlit as st

st.markdown("""
    <style>
    .stButton > button {
        background-color: #FFB6C1; /* Green */
        border: none;
        color: white;
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



def load_image(url, resize_to=(100, 100)):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img = img.resize(resize_to)
        return img
    except (requests.exceptions.RequestException, UnidentifiedImageError):
        return None

def load_image2(url, resize_to=(250, 250)):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img = img.resize(resize_to)
        return img
    except (requests.exceptions.RequestException, UnidentifiedImageError):
        return None
    
def load_image3(url, resize_to=(100, 100)):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img = img.resize(resize_to)
        return img
    except (requests.exceptions.RequestException, UnidentifiedImageError):
        return None    

def run_chef_script():
    subprocess.run(["python", "chef.py"]) 

def run_chef_script2():
    subprocess.run(["python", "recipe.py"])    

st.title("Vegan AI for Homecooks and Chefs")

# Ask about cooking level
cook_level = st.selectbox("What is your level of cooking experience?", ["", "Homecook", "Chef"])

if cook_level == "Homecook":
    # Ask about meal type
    meal_choice = st.selectbox("What are you planning to make?", ["", "Breakfast", "Lunch", "Dinner", "Dessert"])

    # Ask about cuisine preference (optional)
    cuisine_choice = st.selectbox("Do you have a specific cuisine in mind? (optional)", ["", "American", "Asian", "Italian", "Mexican", "Indian", "Other"])

    st.write("Got it! How much time do you have to whip up something tasty? Less than 30 mins, 30-60 mins, or more than an hour?")
    cook_time_choice = st.selectbox("Maximum Cooking Time", ["", "Less than 30 mins", "30-60 mins", "More than an hour"])

    # Ask about flavor profile
    flavor_profile = st.selectbox("What flavor profile do you prefer?", ["", "Savory", "Sweet", "Spicy", "Sour", "Herbal"])

    st.write("Maximum Calories per serving")
    calories = st.number_input("", min_value=0, step=10)

    st.write("Choose the raw vegan ingredients which are available to you")

    # Display images for ingredient selection
    col1, col2, col3 = st.columns(3)

    with col1:
        img_veg = load_image("https://cdn.aarp.net/content/dam/aarp/health/healthy-living/2023/07/1140-colorfulrawveggies.jpg")
        if img_veg:
            st.image(img_veg, caption="Vegetables (broccoli, carrots, etc.)", use_column_width=True)
            vegetables = st.checkbox("Select Vegetables")
    with col2:
        img_starchy_base = load_image("https://i.pinimg.com/originals/24/a7/18/24a71823346e706e6d088493abde5a80.jpg")
        if img_starchy_base:
            st.image(img_starchy_base, caption="Starchy Base (potatoes, rice, pasta)", use_column_width=True)
            starchy_base = st.checkbox("Select Starchy Base")
    with col3:
        img_protein_source = load_image("https://previews.123rf.com/images/nadianb/nadianb1802/nadianb180200465/96309300-vegan-protein-source-tofu-vegan-milk-beans-lentils-nuts-broccoli-spinach-and-seeds-on-dark-rusty.jpg")
        if img_protein_source:
            st.image(img_protein_source, caption="Protein Source (tofu, beans, lentils)", use_column_width=True)
            protein_source = st.checkbox("Select Protein Source")

    col4, col5, col6 = st.columns(3)

    with col4:
        img_nuts_seeds = load_image("https://domf5oio6qrcr.cloudfront.net/medialibrary/9884/GettyImages-179751167.jpg")
        if img_nuts_seeds:
            st.image(img_nuts_seeds, caption="Nuts/Seeds (cashews, almonds, etc.)", use_column_width=True)
            nuts_seeds = st.checkbox("Select Nuts/Seeds")         
    with col5:
        img_fruits = load_image("https://qph.cf2.quoracdn.net/main-qimg-bbb2b1c716fb4744eb2d20d15e023e28.webp")
        if img_fruits:
            st.image(img_fruits, caption="Fruits (fresh or frozen)", use_column_width=True)
            fruits = st.checkbox("Select Fruits")
    with col6:
        img_other = load_image("https://images.squarespace-cdn.com/content/v1/5ad395ba36099b72e4432660/1540127550281-ZTWZ40K4AWAOHZRBDGO7/IMG_9451-2.jpg")
        if img_other:
            st.image(img_other, caption="Other (coconut milk, vegan cheese)", use_column_width=True)
            other = st.checkbox("Select Others")

    selected_ingredients = {}
    # Button to get recommendations
    if st.button("Get Chef Doug's Recipe Recommendations"):
        selected_ingredients = {
            "Vegetables": vegetables,
            "Starchy Base": starchy_base,
            "Protein Source": protein_source,
            "Nuts/Seeds": nuts_seeds,
            "Fruits": fruits,
            "Others": other,
        }

        selected_ingredients_list = [key for key, value in selected_ingredients.items() if value]
        st.write(f"Alright, you have selected: {', '.join(selected_ingredients_list)}. Here are some vegan meal ideas for {meal_choice}:")

        # Recommendation logic based on cuisine, meal type, flavor profile, cooking time, and calories
        if (
            selected_ingredients.get("Vegetables") and 
            selected_ingredients.get("Nuts/Seeds") and 
            selected_ingredients.get("Others") and 
            cuisine_choice in ["", "American"] and 
            meal_choice in ["Lunch", "Dinner"] and 
            flavor_profile in ['Herbal', 'Spicy'] and 
            cook_time_choice == "30-60 mins" and 
            calories <= 1000
        ):
            st.subheader("Creamy Butternut Squash Mac and Cheese")
            img_url = "https://sallysbakingaddiction.com/wp-content/uploads/2015/10/butternut-squash-mac-and-cheese-2.jpg"
            st.markdown(f'<img src="{img_url}" alt="Creamy Butternut Squash Mac and Cheese" style="width:400px;height:300px;">', unsafe_allow_html=True)
            if st.button("Recipe Purchase and Get Tips & Tricks Video for $1"):
            #purchase_option = st.markdown("[Recipe Purchase and Get Tips & Tricks Video for $1](#)", unsafe_allow_html=True)
            #if purchase_option:
                run_chef_script2()
            if st.button("Buy Chef Doug's Cookbooks"):
                st.markdown("<div class='stButton buy-cookbook'><a href='https://www.amazon.com/stores/author/B00E5FEE5S/allbooks?ingress=0&visitId=131f99ec-8628-4c07-85cd-4f4dd8d2ff1d' target='_blank'>Buy Chef Doug's Cookbooks</a></div>", unsafe_allow_html=True)    
            #st.write("[Buy Chef Doug's Cookbooks](https://www.amazon.com/stores/author/B00E5FEE5S/allbooks?ingress=0&visitId=131f99ec-8628-4c07-85cd-4f4dd8d2ff1d)")
if cook_level == "Chef":
    st.header("**Services:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Product Development and Culinary Services")
        st.image(load_image3("https://hospitalityinsights.ehl.edu/hubfs/Blog-EHL-Insights/Blog-Header-EHL-Insights/commercial%20food.jpeg"), caption="")
        st.write("- [Development of Consumer Packaged Goods](https://www.dougmcnish.com/services)")
        menu_link = st.markdown("- [Menu & Recipe Development](#)", unsafe_allow_html=True)
        st.write("- [Food Costing & Menu Engineering](https://www.dougmcnish.com/services)")

        if menu_link:
          run_chef_script()

    with col2:
        st.write("Brand Promotion and Representation")
        st.image(load_image3("https://ignitizeconsulting.com/wp-content/uploads/2019/06/branding-sales.jpg"), caption="")
        st.write("- [Cooking Demo & Brand Representation](https://www.dougmcnish.com/services)")
        st.write("- [Tradeshow Representation](https://www.dougmcnish.com/services)")

    with col3:
        st.write("Operational Efficiency and Consulting")
        st.image(load_image3("https://assets-global.website-files.com/5e8bd2ab8e48e69429cb4fd8/62962735a52a147a3fcdc6dd_illustration_management-consultants.png"), caption="")
        st.write("- [Systems + Operations](https://www.dougmcnish.com/services)")
        st.write("- [Executive Chef Coaching](https://www.dougmcnish.com/services)")
        st.write("- [Food Consulting Call: Consulting for culinary and operational challenges](https://www.dougmcnish.com/schedule-a-1-on-1-call)")
