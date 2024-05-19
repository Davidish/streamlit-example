import streamlit as st

st.title("Mielie Meal Planner")

st.write('Test')

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]

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