import streamlit as st
from PIL import Image, UnidentifiedImageError
import requests
from io import BytesIO

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

def main():
    st.title("Vegan AI for Chefs")
    st.write("Hey there, plant-powered peeps! Feeling peckish? Let's whip up something delicious!")

    # Ask about cooking level
    cook_level = st.selectbox("What is your level of cooking experience?", ["","Homecook", "Chef"])

    # Ask about meal type
    meal_choice = st.selectbox("What are you planning to make?", ["","Breakfast", "Lunch", "Dinner", "Dessert"])

    # Ask about cuisine preference (optional)
    cuisine_choice = st.selectbox("Do you have a specific cuisine in mind? (optional)", ["", "American", "Asian", "Italian", "Mexican", "Indian", "Other"])

    # Ask about flavor profile
    flavor_profile = st.selectbox("What flavor profile are you looking for?", ["", "Savory", "Sweet", "Spicy", "Sour", "Herbal"])

    if cook_level == "Homecook":
        st.write("Let's see what vegan goodies you have on hand!")

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

        # Button to get recommendations
        if st.button("Get Recommendations"):
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

            # Recommendation logic based on cuisine, meal type, and flavor profile
            if selected_ingredients.get("Vegetables") and selected_ingredients.get("Nuts/Seeds") and selected_ingredients.get("Others") and (cuisine_choice in ["", "American"]) and meal_choice in ["Lunch", "Dinner"] and flavor_profile in ['Herbal','Spicy']:
                st.subheader("- Creamy Butternut Squash Mac and Cheese")
                img_url = "https://sallysbakingaddiction.com/wp-content/uploads/2015/10/butternut-squash-mac-and-cheese-2.jpg"
                st.markdown(f'<img src="{img_url}" alt="Creamy Butternut Squash Mac and Cheese" style="width:400px;height:300px;">', unsafe_allow_html=True)
                st.write("**Tips and Tricks:**")
                st.write("- Add a touch of nutmeg for a warming flavor.")
                st.write("- Use nutritional yeast for a cheesy taste.")
                st.write("**Cookbooks to Buy:** [Doug McNish's Cookbooks](https://www.amazon.com/stores/author/B00E5FEE5S/allbooks?ingress=0&visitId=131f99ec-8628-4c07-85cd-4f4dd8d2ff1d)")

            if selected_ingredients.get("Starchy Base") and selected_ingredients.get("Vegetables") and (cuisine_choice in ["", "American"]) and meal_choice in ["Lunch", "Dinner"]:
                st.subheader("- Vegan BBQ Pack (with Oven roasted lemon garlic baby potatoes and Seasoned asparagus)")
                img_url = "https://veggiesociety.com/wp-content/uploads/2019/02/Best-Vegan-Ribs-1-500x489.jpg"
                st.markdown(f'<img src="{img_url}" alt="Vegan BBQ Pack" style="width:400px;height:300px;">', unsafe_allow_html=True)
                st.write("**Tips and Tricks:**")
                st.write("- Marinate the vegetables overnight for deeper flavor.")
                st.write("- Use smoked paprika for a smoky taste.")
                st.write("**Cookbooks to Buy:** [Doug McNish's Cookbooks](https://www.amazon.com/stores/author/B00E5FEE5S/allbooks?ingress=0&visitId=131f99ec-8628-4c07-85cd-4f4dd8d2ff1d)")

            if selected_ingredients.get("Fruits") and (cuisine_choice in ["", "American"]) and meal_choice in ["Breakfast", "Lunch"]:
                st.subheader("- Vegan Benedict Reuben Sandwich")
                img_url = "https://pbnm.org/wp-content/uploads/Reuben-sandwich.jpg"
                st.markdown(f'<img src="{img_url}" alt="Vegan Benedict Reuben Sandwich" style="width:400px;height:300px;">', unsafe_allow_html=True)
                st.write("**Tips and Tricks:**")
                st.write("- Use avocado instead of traditional hollandaise for a creamy twist.")
                st.write("- Add a pinch of black salt for an eggy flavor.")
                st.write("**Cookbooks to Buy:** [Doug McNish's Cookbooks](https://www.amazon.com/stores/author/B00E5FEE5S/allbooks?ingress=0&visitId=131f99ec-8628-4c07-85cd-4f4dd8d2ff1d)")

            if selected_ingredients.get("Nuts/Seeds") and selected_ingredients.get("Vegetables") and (cuisine_choice in ["", "Indian"]) and meal_choice in ["Lunch", "Dinner"]:
                st.subheader("- Curried Cashews and Mixed Vegetables")
                img_url = "https://savoryspin.com/wp-content/uploads/2021/04/PlantBased-Cashew-Curry.jpg"
                st.markdown(f'<img src="{img_url}" alt="Curried Cashews and Mixed Vegetables" style="width:400px;height:300px;">', unsafe_allow_html=True)
                st.write("**Tips and Tricks:**")
                st.write("- Toast the cashews before adding them to the curry for extra flavor.")
                st.write("- Use coconut milk for a rich and creamy texture.")
                st.write("**Cookbooks to Buy:** [Doug McNish's Cookbooks](https://www.amazon.com/stores/author/B00E5FEE5S/allbooks?ingress=0&visitId=131f99ec-8628-4c07-85cd-4f4dd8d2ff1d)")

            if selected_ingredients.get("Vegetables") and selected_ingredients.get("Fruits") and (cuisine_choice in ["", "Mexican"]) and meal_choice in ["Breakfast", "Lunch"]:
                st.subheader("- Tofu Scramble Breakfast Burrito")
                img_url = "https://veganhuggs.com/wp-content/uploads/2017/03/tofu-scramble-breakfast-burrito.jpg"
                st.markdown(f'<img src="{img_url}" alt="Tofu Scramble Breakfast Burrito" style="width:400px;height:300px;">', unsafe_allow_html=True)
                st.write("**Tips and Tricks:**")
                st.write("- Add a splash of lime juice for a fresh, tangy kick.")
                st.write("- Use fresh cilantro for an authentic taste.")
                st.write("**Cookbooks to Buy:** [Doug McNish's Cookbooks](https://www.amazon.com/stores/author/B00E5FEE5S/allbooks?ingress=0&visitId=131f99ec-8628-4c07-85cd-4f4dd8d2ff1d)")

    elif cook_level == "Chef":
        st.write("Professional Vegan Chef's Recipe and Recommendation")

        # Display professional recipes
        if st.button("Show Professional Recipes"):
            st.write(f"Here are some professional vegan meal ideas for {meal_choice}:")

            # Example professional recipe based on meal type and cuisine preference
            if cuisine_choice in ["", "Asian"] and meal_choice in ["Lunch", "Dinner"] and flavor_profile in ['Savory','Spicy']:
                     st.subheader("**Recipe:** Szechuan Tofu Stir Fry with Spicy Garlic Sauce")
                     st.image(load_image2("https://savoryspin.com/wp-content/uploads/2021/04/PlantBased-Cashew-Curry.jpg"), caption="Szechuan Tofu Stir Fry")
                     st.subheader("**Services:**")
                     # Create columns for each category
                     col1, col2, col3 = st.columns(3)

                     with col1:
                        st.write("Product Development and Culinary Services")
                        st.image(load_image3("https://hospitalityinsights.ehl.edu/hubfs/Blog-EHL-Insights/Blog-Header-EHL-Insights/commercial%20food.jpeg"), caption="")
                        st.write("- [Development of Consumer Packaged Goods](https://www.dougmcnish.com/services)")
                        st.write("- [Menu & Recipe Development](https://www.dougmcnish.com/services)")
                        st.write("- [Food Costing & Menu Engineering](https://www.dougmcnish.com/services)")

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
            

            if cuisine_choice in ["", "Italian"] and meal_choice in ["Lunch", "Dinner"]:
                     st.subheader("**Recipe:** Vegan Mushroom Risotto")
                     st.image(load_image("https://veganhuggs.com/wp-content/uploads/2018/02/mushroom-risotto-featured.jpg"), caption="Vegan Mushroom Risotto")
                     st.write("**Services:**")

                     col1, col2, col3 = st.columns(3)

                     with col1:
                        st.write("Product Development and Culinary Services")
                        st.image(load_image3("https://hospitalityinsights.ehl.edu/hubfs/Blog-EHL-Insights/Blog-Header-EHL-Insights/commercial%20food.jpeg"), caption="")
                        st.write("- [Development of Consumer Packaged Goods](https://www.dougmcnish.com/services)")
                        st.write("- [Menu & Recipe Development](https://www.dougmcnish.com/services)")
                        st.write("- [Food Costing & Menu Engineering](https://www.dougmcnish.com/services)")

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


            if cuisine_choice in ["", "Mexican"] and meal_choice in ["Lunch", "Dinner"]:
                     st.subheader("**Recipe:** Vegan Enchiladas with Cashew Cheese")
                     st.image(load_image("https://i2.wp.com/www.evolvingtable.com/wp-content/uploads/2019/01/Black-Bean-Spinach-Enchiladas_1.jpg"), caption="Vegan Enchiladas")
                     st.write("**Services:**")

                     col1, col2, col3 = st.columns(3)

                     with col1:
                        st.write("Product Development and Culinary Services")
                        st.image(load_image3("https://hospitalityinsights.ehl.edu/hubfs/Blog-EHL-Insights/Blog-Header-EHL-Insights/commercial%20food.jpeg"), caption="")
                        st.write("- [Development of Consumer Packaged Goods](https://www.dougmcnish.com/services)")
                        st.write("- [Menu & Recipe Development](https://www.dougmcnish.com/services)")
                        st.write("- [Food Costing & Menu Engineering](https://www.dougmcnish.com/services)")

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


if __name__ == "__main__":
    main()
