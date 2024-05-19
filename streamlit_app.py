import streamlit as st
import os
from supabase import create_client, Client
import pandas as pd

st.title("Mielie Meal Planner")
st.write('Welcome!')

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

response = supabase.table('recipe').select("*").execute()
recipes = response.data

# st.write(recipes)

recipe_display = [recipe['name'] for recipe in recipes]

# option = st.selectbox(
#     "Choose a recipe to add to shopping list?",
#     recipe_display)

options = st.multiselect(
    "Choose your recipes:",
    recipe_display)

# st.write("You selected:", options)

matching_recipe_ids = [recipe['recipe_id'] for recipe in recipes if recipe['name'] in options]
# st.write(matching_recipe_ids)

recipes_dict = {recipe["recipe_id"]: recipe for recipe in recipes}

# servings = st.slider("Number of servings?", 0, 130, 25)


final_ingredients = {}
if len(matching_recipe_ids) > 0:
    for recipe_id in matching_recipe_ids:
        recipe_name = recipes_dict.get(recipe_id)['name']
        # matching_recipe = [recipe for recipe in recipes if recipe["recipe_id"] == recipe_id_to_find]
        st.write(recipe_name)
        
        st.write('Ingredients:')
        reponse_ingredients = supabase.table('recipeingredient').select("*").eq('recipe_id', recipe_id).execute()

        ingredient_ids = reponse_ingredients.data
        for ingredient_id in ingredient_ids:
            id = ingredient_id['ingredient_id']
            
            reponse_final = supabase.table('ingredient').select("*").eq('ingredient_id',id).execute()
            final = reponse_final.data[0]

            ingredient_name = final['name']
            ingredient_type = final['type']
            ingredient_category = final['category']
            ingredient_unit = final['unit']
            ingredient_quantity = ingredient_id['quantity']

            ingredient_key = f"{ingredient_name}_{ingredient_type}"
            if ingredient_key not in final_ingredients:
                final_ingredients[ingredient_key] = {}
                final_ingredients[ingredient_key]['name'] = ingredient_name
                final_ingredients[ingredient_key]['type'] = ingredient_type
                final_ingredients[ingredient_key]['category'] = ingredient_category
                final_ingredients[ingredient_key]['unit'] = ingredient_unit
                final_ingredients[ingredient_key]['quantity'] = ingredient_quantity
            else:
                final_ingredients[ingredient_key]['quantity'] = final_ingredients[ingredient_key]['quantity'] + ingredient_quantity
            
            # st.write(f'{ingredient_category}: {ingredient_name} {ingredient_type} = {quantity} {ingredient_unit}')

# st.write(final_ingredients)
df = pd.DataFrame.from_dict(final_ingredients, orient='index')
df.columns = ['Name','Type','Category','Unit','Quantity']
st.write(df[['Name','Type','Category','Unit','Quantity']])