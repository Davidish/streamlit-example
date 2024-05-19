import streamlit as st
import os
from supabase import create_client, Client

st.title("Mielie Meal Planner")
st.write('Welcome!')

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

response = supabase.table('recipe').select("*").execute()
recipes = response.data

recipe_display = [recipe['name'] for recipe in recipes]
options = st.multiselect(
    "Choose your recipes:",
    recipe_display)

st.write("You selected:", options)

matching_recipe_ids = [recipe['recipe_id'] for recipe in recipes if recipe['name'] in options]
st.write(matching_recipe_ids)

for recipe_id in matching_recipe_ids:
        recipe_name = recipes.get(recipe_id)
        st.write(recipe_name)
        
        st.write('Ingredients:')
        reponse_ingredients = supabase.table('recipeingredient').select("*").eq('recipe_id', recipe_id).execute()

        ingredient_ids = reponse_ingredients.data
        for ingredient_id in ingredient_ids:
            id = ingredient_id['ingredient_id']
            quantity = ingredient_id['quantity']

            reponse_final = supabase.table('ingredient').select("*").eq('ingredient_id',id).execute()
            final = reponse_final.data[0]

            ingredient_name = final['name']
            ingredient_type = final['type']
            ingredient_category = final['category']
            ingredient_unit = final['unit']

            
            st.write(f'{ingredient_category}: {ingredient_name} {ingredient_type} = {quantity} {ingredient_unit}')