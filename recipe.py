import streamlit as st
import webbrowser

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
    #### Mac and Cheese
    - 1 cup (250 mL) roughly chopped white onion
    - 1 cup (250 mL) deodorized coconut oil
    - 1 cup (250 mL) all-purpose flour
    - ¹⁄₃ cup (75 mL) semi-sweet white wine, such as Riesling
    - 5 cups (1.25 L) unsweetened almond milk
    - ³⁄4 cup (175 mL) nutritional yeast
    - 2 teaspoons (10 mL) garlic powder
    - 2 teaspoons (10 mL) sea salt
    - ¹⁄2 teaspoon (2 mL) brown rice miso, or any type of miso
    - ¹⁄4 cup (60 mL) Swiss Cheese (recipe follows)
    - 1 pound (450 g) dried elbow macaroni
    - ¹⁄2 cup (125 mL) panko crumbs

    #### Swiss Cheese
    - 1 cup (250 mL) water
    - 1 tablespoon (15 mL) agar powder
    - 1 cup (250 mL) raw cashews, soaked and drained (see Tip)
    - ¹⁄4 cup (60 mL) unsweetened almond milk
    - ¹⁄₃ cup (75 mL) semi-sweet white wine, such as Riesling
    - 2 tablespoons (30 mL) freshly squeezed lemon juice
    - 2 tablespoons (30 mL) unpasteurized apple cider vinegar
    - 2 teaspoons (10 mL) Dijon mustard
    - 1¹⁄2 teaspoons (7 mL) nutritional yeast
    - 1¹⁄2 teaspoons (7 mL) sea salt
    - 1¹⁄2 teaspoons (7 mL) tahini
    - ¹⁄4 teaspoon (1 mL) ground mustard powder
    - ¹⁄8 teaspoon (0.5 mL) brown rice miso
    """
st.markdown(ingredients)

# Recipe Directions
directions = """
    ### Directions
    #### Prep the Swiss Cheese
    1. In a small pot, combine the water and agar powder. Bring to a boil, reduce the heat to a simmer, and cook until reduced by half, about 10 minutes. Set aside.
    2. In a high-speed blender, combine the soaked cashews, almond milk, white wine, lemon juice, apple cider vinegar, mustard, nutritional yeast, salt, tahini, mustard powder, and miso. Blend on high speed until smooth. Add the agar mixture and blend until no lumps remain.
    3. Transfer to a shallow container. Refrigerate until set, about 2 hours. Serve immediately or store in an airtight container in the fridge for up to 10 days.

    #### Make the Mac and Cheese
    1. Preheat the oven to 400°F (200°C).
    2. In a medium pot, over medium heat, combine the onion, coconut oil, and flour. Cook, stirring frequently, for 6 to 8 minutes. Remove the pot from the heat, add the white wine, and stir constantly for about 2 minutes to help remove some of the grittiness from the flour and to make a thick paste. Add the almond milk in a constant, steady stream while whisking at the same time. Whisk until no lumps remain, 1 to 2 minutes.
    3. Return the pot to medium-high heat and add the nutritional yeast, garlic powder, salt, and miso. Bring the mixture to a boil, stirring frequently. Reduce the heat to a simmer and cook for 2 to 3 minutes to help remove some of the raw taste from the flour.
    4. Remove the pot from the heat and stir in the Swiss cheese. In batches, transfer the sauce to a blender, taking care not to fill the blender more than halfway with the hot sauce, and blend until completely smooth. Transfer the sauce to a large, clean pot.
    5. Bring a large pot of salted water to a rapid boil. Cook the macaroni according to package directions. Drain the pasta in a colander, then rinse with cold running water until the pasta is cold.
    6. Add the cooked pasta to the cheese sauce and stir to combine. Transfer the mixture to an 11- × 7-inch (2 L) glass or metal baking dish. Top with the panko and bake until bubbling hot in the middle and golden brown on top, 25 to 30 minutes. Remove from the oven and allow to sit for 10 minutes before serving. Allow leftover mac and cheese to cool completely and store in an airtight container in the fridge for up to 1 week.
    """

st.markdown(directions)

# Tips and Tricks
tips = """
    ### Tips and Tricks
    - To soak the cashews, place them in a small bowl and cover with 2 cups (500 mL) hot water for at least 1 hour or overnight, covered, and stored in the fridge. Drain and rinse the cashews, discarding the soaking liquid.
    """

st.write(tips)
