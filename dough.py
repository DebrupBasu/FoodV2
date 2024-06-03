import streamlit as st
from PIL import Image, UnidentifiedImageError
import requests
import subprocess
from io import BytesIO
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import json

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
    

def preprocess_image(img):
    img = img.resize((224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def classify_image(img_array):
    model = MobileNetV2(weights='imagenet')
    preds = model.predict(img_array)
    decoded_preds = decode_predictions(preds, top=1)[0]
    return decoded_preds

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def fetch_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def load_image(url, resize_to=(100, 100)):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img = img.resize(resize_to)
        return img
    except (requests.exceptions.RequestException, UnidentifiedImageError):
        return None


def compare_images(img1, img2):
    img1_resized = img1.resize((224, 224))  # Resize to match the MobileNetV2 input size
    img2_resized = img2.resize((224, 224))  # Resize to match the MobileNetV2 input size
    img1_array = img_to_array(img1_resized)
    img2_array = img_to_array(img2_resized)
    mse = np.mean((img1_array - img2_array) ** 2)
    return mse
    
ingredients = {
    "Vegetables": [
        {"name": "Butternut Squash", "image": [
            "Ingredients/butternut_squash.jpg",
            "Ingredients/butternut_squash2.JPEG"
        ]}
    ],
    "Starchy Base": [
        {"name": "Pasta", "image": [
            "Ingredients/pasta1.jpg",
            "Ingredients/pasta2.webp",
            "Ingredients/pasta3.jpg",
            "Ingredients/pasta4.jpg",
            "Ingredients/pasta5.jpg",
            "Ingredients/pasta6.JPEG",
            "Ingredients/pasta7.jpg"
        ]}
    ],
    "Protein Source": [
        {"name": "Nutritional Yeast", "image": [
            "Ingredients/yeast.webp",
            "Ingredients/yeast2.jpg",
            "Ingredients/yeast3.jpg",
            "Ingredients/yeast4.jpg",
            "Ingredients/yeast5.webp",
            "Ingredients/yeast6.JPEG",
            "Ingredients/yeast7.jpg"
        ]}
    ],
    "Nuts/Seeds": [
        {"name": "Mustard Seed", "image": [
            "Ingredients/MustardSeed.JPEG",
            "Ingredients/MustardSeed2.jpg"
        ]},
        {"name": "Cashewnuts", "image": [
            "Ingredients/Cashewnuts.JPEG",
            "Ingredients/Cashewnuts2.JPEG"
        ]}
    ],
    "Fruits": [],
    "Others (Vegan Dairy Products, Oil etc)": [
        {"name": "butter", "image": [
            "Ingredients/butter1.jpg",
            "Ingredients/butter2.jpg",
            "Ingredients/butter3.jpg",
            "Ingredients/butter4.jpg",
            "Ingredients/butter5.jpg"
        ]}
    ],
    "Seasoning": [

        {"name": "Breadcrumbs", "image": [
            "Ingredients/BreadCrumbs.JPEG"
        ]},
        {"name": "Garlic Powder", "image": [
            "Ingredients/GarlicPowder.JPEG"
        ]},
        {"name": "Salt", "image": [
            "Ingredients/Salt.JPEG"
        ]}
    ]
}
with open('ingredients.json', 'w') as json_file:
    json.dump(ingredients, json_file)    
 
# Load ingredients JSON
ingredients_data = load_json("ingredients.json")    

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

    uploaded_files = st.file_uploader("Choose the raw vegan ingredients which are available to you", type=["jpg", "jpeg", "png", "webp"], accept_multiple_files=True)
    identified_categories = []

    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            uploaded_image = Image.open(uploaded_file)
            st.image(uploaded_image, caption='Uploaded Image', use_column_width=False,width=200)
        
            # Preprocess and classify the uploaded image
            img_array = preprocess_image(uploaded_image)
            predictions = classify_image(img_array)
            top_prediction = predictions[0][1]
        
            # Compare the uploaded image with the images in the JSON file
            min_mse = float('inf')
            identified_category = None
            
            for category, items in ingredients_data.items():
                for item in items:
                    if isinstance(item["image"], list):
                        for image_path in item["image"]:
                            json_image = Image.open(image_path)
                            mse = compare_images(uploaded_image, json_image)
                            if mse < min_mse:
                                min_mse = mse
                                identified_item = item["name"]
                                identified_category = category
                    else:
                        json_image = Image.open(item["image"])
                        mse = compare_images(uploaded_image, json_image)
                        if mse < min_mse:
                            min_mse = mse
                            identified_item = item["name"]
                            identified_category = category
            
            # Display the identified category
            if identified_category:
                st.write(f"Identified category: {identified_category}")
                st.write(f"Identified item: {identified_item}")
                identified_categories.append(identified_category)
    
    # Display the selected ingredients
    st.write("Selected Ingredients:")
    st.write(identified_categories)

    # Use the selected ingredients list to determine the recipe recommendations
    if (
    "Seasoning" in identified_categories and 
    "Nuts/Seeds" in identified_categories and 
    "Protein Source" in identified_categories and 
    "Others (Vegan Dairy Products, Oil etc)" in identified_categories and
    cuisine_choice in ["", "American"] and 
    meal_choice in ["Lunch", "Dinner"] and 
    flavor_profile in ['Herbal', 'Spicy'] and 
    cook_time_choice == "30-60 mins" and 
    calories <= 1000
):
     st.subheader("If you add Butternut Squash to your list of Ingredients, we would like to recommend you Chef Doug McNish's Signature Butternut Squash Mac and Cheese recipe")
     img_url = "https://sallysbakingaddiction.com/wp-content/uploads/2015/10/butternut-squash-mac-and-cheese-2.jpg"
     st.markdown(f'<img src="{img_url}" alt="Creamy Butternut Squash Mac and Cheese" style="width:400px;height:300px;">', unsafe_allow_html=True)
     st.button("Recipe Purchase and Get Tips & Tricks Video for $1")
     st.button("Buy Chef Doug's Cookbooks")
