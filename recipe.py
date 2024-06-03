import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from PIL import UnidentifiedImageError

def load_image2(url, resize_to=(600, 400)):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img = img.resize(resize_to)
        return img
    except (requests.exceptions.RequestException, UnidentifiedImageError):
        return None

# Load the image
img_url = "https://sallysbakingaddiction.com/wp-content/uploads/2015/10/butternut-squash-mac-and-cheese-2.jpg"
img = load_image2(img_url)

# Display the image
if img:
    st.image(img, caption="Butternut Squash Mac and Cheese", use_column_width=True)

# Recipe Ingredients
ingredients = """
    ### Ingredients
    - 1 medium butternut squash, peeled, seeded, and cubed
    - 2 large potatoes, peeled and cubed
    - 2 large carrots, peeled and sliced
    - 1 large onion, chopped
    - 1 cup raw cashews, soaked in water for at least 2 hours
    - 1/4 cup deodorized coconut oil
    - 1/2 cup nutritional yeast (NOOCH)
    - 2 teaspoons garlic powder
    - 2 teaspoons onion powder
    - 1 teaspoon smoked paprika
    - 1/2 teaspoon turmeric (optional, for color)
    - 1 teaspoon mustard seed powder
    - 1 tablespoon agar powder
    - 1/2 cup panko crumbs
    - Salt and pepper, to taste
    - 1 pound pasta of your choice (gluten-free)
    """
st.markdown(ingredients)

# Recipe Directions
directions = """
    ### Directions
    #### Prepare the Vegetables
    1. In a large pot, add the butternut squash, potatoes, carrots, and onion. Cover with water and bring to a boil. Cook until the vegetables are tender, about 15-20 minutes. Drain and set aside.

    #### Blend the Sauce
    2. In a high-speed blender, combine the cooked vegetables, soaked and drained cashews, coconut oil, nutritional yeast, garlic powder, onion powder, smoked paprika, turmeric, mustard seed powder, and agar powder. Blend until smooth and creamy. If the mixture is too thick, add water or vegetable broth, a little at a time, until the desired consistency is reached. Season with salt and pepper to taste.

    #### Cook the Pasta
    3. While preparing the sauce, cook the pasta according to the package instructions. Drain and set aside.

    #### Combine and Serve
    4. In a large pot, combine the cooked pasta and the butternut squash sauce. Stir well to coat the pasta evenly with the sauce. Heat over medium-low heat until warmed through.
    5. Transfer to a baking dish, sprinkle with panko crumbs, and bake at 375°F (190°C) until the top is golden and crispy, about 10-15 minutes.
    6. Serve the mac and cheese hot, garnished with additional nutritional yeast or smoked paprika if desired.
    """

st.markdown(directions)

# Tips and Tricks
tips = """
    ### Tips and Tricks
    - To soak the cashews, place them in a small bowl and cover with 2 cups (500 mL) hot water for at least 1 hour or overnight, covered, and stored in the fridge. Drain and rinse the cashews, discarding the soaking liquid.
    """

st.write(tips)
