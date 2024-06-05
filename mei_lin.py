import streamlit as st
from streamlit_extras.stateful_button import button
from PIL import Image, UnidentifiedImageError
import requests
from io import BytesIO
from streamlit_image_select import image_select
import webbrowser
import io
import base64
button_clicked = False
def load_image3(url, resize_to=(200, 200)):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img = img.resize(resize_to)
        return img
    except (requests.exceptions.RequestException, UnidentifiedImageError):
        return None



def recommend_recipe():
    image_path = "logo.png"
    image = Image.open(image_path)

    # Convert the image to RGB format
    image_rgb = image.convert("RGB")

    # Save the image to a BytesIO object
    img_byte_arr = io.BytesIO()
    image_rgb.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    st.markdown(
    """
    <div style="display: flex; align-items: center;">
        <div style="flex: 0.2;">
            <img src="data:image/png;base64,{}" style="width:70px; margin-left: 10px; margin-right: 10px;margin-top: -10px;">
        </div>
        <div style="flex: 1.8; display: flex; align-items: center;">
            <h4>Chef Mei Lin's Prescriptive AI</h4>
        </div>
    </div>
    """.format(base64.b64encode(img_byte_arr).decode("utf-8")),
    unsafe_allow_html=True
)

    cuisine_preference = st.selectbox(
        "Choose the type of Cuisine you prefer?",
        ("Asian", "Western", "Fusion", "No Preference")
    )
    
    basic_recipe_pref = image_select(
        label="Select recipe preference",
        images=[
            "https://img.hellofresh.com/f_auto,fl_lossy,q_auto,w_1200/hellofresh_s3/image/southwest-plant-based-protein-over-rice-11710d4e.jpg",
            "https://www.indianhealthyrecipes.com/wp-content/uploads/2022/02/veg-noodles-vegetable-noodles-recipe-500x500.jpg",
            "https://myfoodstory.com/wp-content/uploads/2017/12/Homemade-Creamy-Vegetable-Soup-2-1-1170x617.jpg",
            "https://www.onceuponachef.com/images/2009/08/grilled-flank-steak.jpg",
            "https://www.allrecipes.com/thmb/5GyuoPVxz5H-ljYftjKANrCsDuM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/216758-moms-fabulous-chicken-pot-pie-with-biscuit-crust-DDMFS-4x3-98b21fcdaa5e40acad57bd9a48822694.jpg"
        ],
        captions=["Rice-based", "Noodle-based", "Soup-based", "Grill-based", "Biscuit-based"], use_container_width= False
    )

    protein_preference = image_select(
        label="Select protein preference",
        images=[
            "https://www.thedailymeal.com/img/gallery/can-you-go-to-a-steakhouse-and-order-a-completely-raw-steak/raw%20steak.JPG",
            "https://osfbl01.justfoodfordogs.com/wp-content/uploads/2023/08/raw-pork.jpg",
            "https://media.healthyfood.com/wp-content/uploads/2017/03/Ask-the-experts-Raw-chicken.jpg",
            "https://www.tastingtable.com/img/gallery/every-cut-of-lamb-ranked-worst-to-best/intro-1652107513.jpg",
            "https://www.macspharmacy.com/wp-content/uploads/2019/08/vegetables.jpg"
        ],
        captions=["Beef", "Pork", "Chicken", "Lamb", "Plant-based"], use_container_width= False
    )

    if protein_preference == "https://media.healthyfood.com/wp-content/uploads/2017/03/Ask-the-experts-Raw-chicken.jpg":
        selected_cut = image_select(
            label="Select cut of chicken",
            images=[
                "https://cdn.womensrunning.com/wp-content/uploads/2020/07/Chicken.jpg?crop=1:1&width=1000",
                "https://recipes.net/wp-content/uploads/2023/10/how-to-cut-raw-chicken-breast-1696859426.jpg",
                "https://madbutchermeat.com/cdn/shop/products/Untitleddesign_42_6d120263-fb82-4c14-ac8b-4ea8847c654a.png?v=1677017661",
                "https://images.ctfassets.net/ttw7uwgviuml/5lgifjI7wTef64dwxIli9V/ed5979cc3ca44e3287474d4b923935a8/4432_WF_RAW_Chicken_Wings_Sections_Poultry.jpg?fm=jpg&fl=progressive"
            ],
            captions=["Whole Chicken", "Chicken Breast", "Chicken Thighs", "Chicken Wings"], use_container_width= False
        )
    elif protein_preference == "https://www.thedailymeal.com/img/gallery/can-you-go-to-a-steakhouse-and-order-a-completely-raw-steak/raw%20steak.JPG":
        selected_cut = image_select(
            label="Select cut of beef",
            images=[
                "https://www.southernliving.com/thmb/vIe1diteC_Mq6wEfr1XJCVOmqJc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Ground_Beef_004-1-085c019aefff471d852d4b5ad7495374.jpg",
                "https://mrsteak.com/cdn/shop/files/BonelessRibeyeIGPorst3_1800x1800.jpg?v=1689017280",
                "https://www.betterbeefcompany.com/wp-content/uploads/2022/12/Sirloin-Steaks.jpg",
                "https://eltoroviandes.com/wp-content/uploads/2021/02/T-Bone-Steak-1.jpg"
            ],
            captions=["Ground Beef", "Rib Eye", "Sirloin", "T-Bone"], use_container_width= False
        )
    elif protein_preference == "https://osfbl01.justfoodfordogs.com/wp-content/uploads/2023/08/raw-pork.jpg":
        selected_cut = image_select(
            label="Select cut of pork",
            images=[
                "https://www.cooksinfo.com/wp-content/uploads/ground-pork.jpg",
                "https://www.tastingtable.com/img/gallery/you-should-never-cook-cold-pork-chops-heres-why/l-intro-1653671935.jpg",
                "https://haassmeats.com/wp-content/uploads/2021/07/BELLY.jpg",
                "https://recipes.net/wp-content/uploads/2021/03/a-rack-of-fresh-spare-ribs-1024x682.jpeg",
                "https://images.ctfassets.net/ttw7uwgviuml/6Y5v5uOrTJZTcA3fzWtKky/aa0ab88e90be876b840122fcbcea7ced/3130_WF_Raw_Pork_Tenderloin_-_Family_Size_Pork.jpg"
            ],
            captions=["Ground Pork", "Pork Chops", "Pork Belly", "Pork Ribs", "Pork Loin"], use_container_width= False
        )
    elif protein_preference == "https://www.tastingtable.com/img/gallery/every-cut-of-lamb-ranked-worst-to-best/intro-1652107513.jpg":
        selected_cut = image_select(
            label="Select cut of lamb",
            images=[
                "https://farmingdalemeatmarket.com/cdn/shop/products/lambribchops3sq_1080x.jpg?v=1642613384",
                "https://www.hgwalter.com/cdn/shop/products/lambshoulder_f483ba4c-2d3b-41c5-b917-d9ee21d2ce69.jpg?v=1674473127",
                "https://allnaturalmeats.ca/wp-content/uploads/2016/12/16177284_xl.jpg",
                "https://www.misterbrisket.com/wp-content/uploads/rack-of-lamb-raw-1.jpg"
            ],
            captions=["Lamb Chops", "Lamb Shoulder", "Lamb Leg", "Lamb Rack"], use_container_width= False
        )

    cooking_method_preference = image_select(
        label="Select cooking method",
        images=[
            "https://static.toiimg.com/thumb/82287593.cms?resizemode=4&width=1200",
            "https://hips.hearstapps.com/hmg-prod/images/22-del-explainer-roasting-baking-1667919834.jpg?crop=1xw:1xh;center,top&resize=1200:*",
            "https://cdn.cdnparenting.com/articles/2019/02/28170826/235152028-H-1024x700.webp",
            "https://static01.nyt.com/images/2013/10/23/dining/23FLEX_SPAN/23FLEX-articleLarge.jpg?quality=75&auto=webp&disable=upscale",
            "https://learntocook.com/wp-content/uploads/2016/04/outdoor-activities-grilling-barbque-13214878.jpg"
        ],
        captions=["Steaming", "Baking", "Boiling", "Frying", "Grilling"], use_container_width= False
    )

    
    cooking_time = st.selectbox(
        "Maximum time you have for preparation and cooking",
        ("Less than 30 minutes", "30-60 minutes", "More than 60 minutes", "No Preference")
    )    
    
    flavor_preference = st.selectbox(
        "What flavor profile do you prefer?",
        ("Sweet", "Savory", "Spicy", "No Preference")
    )

    # Recommend a recipe based on answers
    if button("Get Recipe Recommendation", key="button1"):
    #if st.button("Get Recipe Recommendation"):
        recommended_recipe = None
        recipe_image_url = None

        if (selected_cut == "https://www.cooksinfo.com/wp-content/uploads/ground-pork.jpg" and 
            flavor_preference in ["Sweet", "Savory"] and 
            basic_recipe_pref == "https://img.hellofresh.com/f_auto,fl_lossy,q_auto,w_1200/hellofresh_s3/image/southwest-plant-based-protein-over-rice-11710d4e.jpg" and 
            cuisine_preference in ["Asian", "Fusion"]):
            recommended_recipe = "Congee & Caramelized Pork with Crispy Shallots and Black Garlic"
            recipe_image_url = "https://media.blueapron.com/recipes/481/square_newsletter_images/20141218-2133-2-9033/square_1200x1200_larger-txt_20_1_.jpg?quality=80&width=1300&format=pjpg"
        
        elif (selected_cut == "https://madbutchermeat.com/cdn/shop/products/Untitleddesign_42_6d120263-fb82-4c14-ac8b-4ea8847c654a.png?v=1677017661" and 
              flavor_preference in ["Sweet", "Savory"] and 
              basic_recipe_pref == "https://www.onceuponachef.com/images/2009/08/grilled-flank-steak.jpg" and 
              cuisine_preference in ["Asian", "Fusion"]):
              recommended_recipe = "Char Siu Chicken Kebab"
              recipe_image_url = "https://robbreport.com/wp-content/uploads/2021/07/char_siu_chicken_mei_lin_plated.jpg?w=1000"
        
        elif (flavor_preference in ["Savory", "Spicy"] and 
              basic_recipe_pref == "https://www.allrecipes.com/thmb/5GyuoPVxz5H-ljYftjKANrCsDuM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/216758-moms-fabulous-chicken-pot-pie-with-biscuit-crust-DDMFS-4x3-98b21fcdaa5e40acad57bd9a48822694.jpg" and 
              cuisine_preference in ["Asian", "Fusion"]):
              recommended_recipe = "Okonomiyaki"
              recipe_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2022/01/Okonomiyaki-pg13-363c802-03b59be.jpg?resize=768,574"
        
        elif (selected_cut == "https://recipes.net/wp-content/uploads/2021/03/a-rack-of-fresh-spare-ribs-1024x682.jpeg" and 
              flavor_preference in ["Sweet", "Savory"] and 
              basic_recipe_pref == "https://www.onceuponachef.com/images/2009/08/grilled-flank-steak.jpg" and 
              cuisine_preference in ["Asian", "Fusion"]):
              recommended_recipe = "Char Siu BBQ RIBS"
              recipe_image_url = "https://cdn.shopify.com/s/files/1/0034/6610/0806/files/feed_1_2_1024x1024.png?v=1628792417"
        
        elif (selected_cut == "https://tasteofartisan.com/wp-content/uploads/2019/03/how-to-cook-pork-belly.jpg" and 
              flavor_preference in ["Savory", "Spicy"] and 
              basic_recipe_pref == "https://www.indianhealthyrecipes.com/wp-content/uploads/2022/02/veg-noodles-vegetable-noodles-recipe-500x500.jpg" and 
              cuisine_preference in ["Asian", "Fusion"]):
              recommended_recipe = "Pork Belly Dumplings with Crispy Lace"
              recipe_image_url = "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2023/11/21/FN_Mei-Lin_Pork-Belly-Dumplings-Crispy-Lace_H1.jpg.rend.hgtvcom.826.620.suffix/1700601503466.jpeg"
        
        elif (selected_cut == "https://madbutchermeat.com/cdn/shop/products/Untitleddesign_42_6d120263-fb82-4c14-ac8b-4ea8847c654a.png?v=1677017661" and 
              flavor_preference in ["Savory", "Spicy"] and 
              basic_recipe_pref == "https://www.allrecipes.com/thmb/5GyuoPVxz5H-ljYftjKANrCsDuM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/216758-moms-fabulous-chicken-pot-pie-with-biscuit-crust-DDMFS-4x3-98b21fcdaa5e40acad57bd9a48822694.jpg" and 
              cuisine_preference in ["Western", "Fusion"]):
              recommended_recipe = "Fried Chicken and Biscuit Sandwich"
              recipe_image_url = "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2023/12/12/FRIED_CHICKEN_BISCUIT_SANDWICH_H_f.jpg.rend.hgtvcom.826.620.suffix/1702483964041.jpeg"
        
        elif (selected_cut == "Whole Chicken" and 
              flavor_preference in ["Sweet", "Savory"] and 
              basic_recipe_pref == "https://toriavey.com/images/2010/02/IMG_0602-2.jpg" and 
              cuisine_preference in ["Asian", "Fusion"]):
              recommended_recipe = "Nam Yu Roasted Chicken"
              recipe_image_url = "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2024/01/31/FNK_Nam-Yu-Roasted-Chicken_H2.jpg.rend.hgtvcom.826.620.suffix/1706738178601.jpeg"

        if recommended_recipe and recipe_image_url:
            st.subheader(f"We recommend: {recommended_recipe}")
            img = load_image3(recipe_image_url)
            if img:
                st.image(img, caption=recommended_recipe)
            if button("Purchase branded Mei Lin merchandizes here", key="button2"):
                umamei_preference = image_select(
                          label="Enhance the flavors of this recipe with the Micro-Seasoning Kits of other similar recipes",
                          images=[
                              "https://cdn.sanity.io/images/9giw3y1g/production/10f84bd86d4e8b4253f08928ce5c7e6d61734065-1440x1800.jpg?fm=webp",
                              "https://cdn.sanity.io/images/9giw3y1g/production/0fe465bfb627423d1b5caf2b13909953cf426e0c-1440x1800.jpg?fm=webp",
                              "https://cdn.sanity.io/images/9giw3y1g/production/de335e485f74cb3ebdd82e10044e73d5c1c42a58-1440x1800.png?fm=webp",
                              "https://cdn.sanity.io/images/9giw3y1g/production/f6a68cdfac724191706a4e026833ba9e6de5f924-1440x1800.jpg?fm=webp"                   
                          ],
                          captions=["Kit for Char Siu Chicken Kebab", "Kit for Dearborn Chicken Lule", "Kit for Pho Spiced Beef Shish Kebab", "Kit for This Lamb Is On Fire- Kefta"], use_container_width= False
                      )
                umamei_preference = image_select(
                          label="Enhance the flavors of this recipe with UMAMEI",
                          images=[
                              "https://images.squarespace-cdn.com/content/v1/5e7c5affa08f0658413b18b1/1704389840049-23AVTBPKQJRMQR51179M/IMG_9413.jpg?format=1000w",
                              "https://images.squarespace-cdn.com/content/v1/5e7c5affa08f0658413b18b1/1704390404084-8055UXL8K1GJE93IUBF6/IMG_9419.jpg?format=1000w",
                              "https://images.squarespace-cdn.com/content/v1/5e7c5affa08f0658413b18b1/1702038226287-Q3OB22NCFXB325IKNM1V/77030BDD-5235-4891-92BA-88A143DC179D?format=1000w",
                              "https://images.squarespace-cdn.com/content/v1/5e7c5affa08f0658413b18b1/1607582638426-DTSQVXXBRRSXIG26DOJM/IMG_3766.jpg?format=1000w",
                              "https://images.squarespace-cdn.com/content/v1/5e7c5affa08f0658413b18b1/1607582748596-APS1DYSYQX1NDMONZZJS/IMG_3755.jpg?format=1000w",
                              "https://images.squarespace-cdn.com/content/v1/5e7c5affa08f0658413b18b1/1607582908893-6WCCQOZSRFOQXA7VA5EL/IMG_3765.jpg?format=1000w"
                             
                          ],
                          captions=["Umamei Truffle XO (8oz)", "Umamei Chili Oil (8oz)", "Umamei Chili Oil Dropper", "Umamei XO (8oz)", "Umamei Vegan XO (8oz)", "Umamei Chili Oil (4oz)"], use_container_width= False
                      )
                tea_preference = image_select(
                          label="Purchase fragrant tea from MEI'S DAY & MEI'S NIGHT",
                          images=[
                              "https://www.smithtea.com/cdn/shop/files/MeiLinTea_Day-tin_441.jpg?v=1698448825&width=1000",
                              "https://www.smithtea.com/cdn/shop/files/MeiLinTea_Night-holding_179.jpg?v=1698448825&width=1000"
                          ],
                          captions=["MEI'S DAY", "MEI'S NIGHT"], use_container_width= False
                      )
            
            
            if button("Order Food from My Restaurant- Daybird!", key="button3"):
                webbrowser.open("https://www.daybirdla.com/")
            if button("Recipe Purchase and Get Tips & Tricks Video for $1", key="button3"):
                webbrowser.open("https://drinkolipop.com/blogs/digest/out-of-the-fire-mei-lin-s-vintage-cola-bbq-sauce-braised-greens")
        else:
            st.write("We couldn't find a perfect match based on your preferences. Please try different options.")

if __name__ == "__main__":
    recommend_recipe()
