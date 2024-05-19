import streamlit as st
import os
from supabase import create_client, Client

st.title("Mielie Meal Planner")

st.write('Choose your meals!')

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]

st.write(url)

supabase: Client = create_client(url, key)

response = supabase.table('recipe').select("*").execute()
recipes = response.data

import streamlit as st

recipe_display = [recipes['name'] for reciple in recipe.values()]

# for recipe in recipes:
#         # print(recipe)
#         recipe_id = recipe['recipe_id']
#         recipe_name = recipe['name']
#         recipe_display.append(recipe_display)

options = st.multiselect(
    "Choose recipes for the week",
    [recipe_display])

st.write("You selected:", options)


# for recipe in recipes:
#         # print(recipe)
#         recipe_id = recipe['recipe_id']
#         recipe_name = recipe['name']
#         # print(f'Recipe id: {recipe_id}')
#         # print(f'Recipe name: {recipe_name}')

#         st.write(f'Recipe name: {recipe_name}')

# options = st.multiselect(
#     "What are your favorite colors",
#     ["Green", "Yellow", "Red", "Blue"],
#     ["Yellow", "Red"])

# st.write("You selected:", options)