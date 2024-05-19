import streamlit as st
import os

st.title("Mielie Meal Planner")

st.write('Test')


os.environ["SUPABASE_URL"] == st.secrets["SUPABASE_URL"]
os.environ["SUPABASE_KEY"] == st.secrets["SUPABASE_KEY"]
url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]

st.write(url)

supabase: Client = create_client(url, key)

response = supabase.table('recipe').select("*").execute()
recipes = response.data

for recipe in recipes:
        # print(recipe)
        recipe_id = recipe['recipe_id']
        recipe_name = recipe['name']
        # print(f'Recipe id: {recipe_id}')
        # print(f'Recipe name: {recipe_name}')

        st.write(f'Recipe name: {recipe_name}')

# options = st.multiselect(
#     "What are your favorite colors",
#     ["Green", "Yellow", "Red", "Blue"],
#     ["Yellow", "Red"])

# st.write("You selected:", options)