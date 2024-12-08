# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Customize Your Smoothie!:cup_with_straw:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at.
    """
)


# option = st.selectbox(
#     "What is your favorite fruit",
#     ("Apple", "banana", "Mango","Pineapple"),
# )[docs.streamlit.io](https://docs.streamlit.io)

# st.write("Your Favorite fruit is:", option)

name_an_order = st.text_input("Name On Smoothie")
st.write("The name on Smoothie will be", name_an_order)

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)

ingrediants_list = st.multiselect(
    'Choose up to five element'
    , my_dataframe,max_selections=5
)
if ingrediants_list:
    ingrediants_string =''
    for fruit_chosen in ingrediants_list:
        ingrediants_string+=fruit_chosen + ' '
    # st.write(ingrediants_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingrediants_string + """','"""+name_an_order+"""')"""

    time_to_insert = st.button('Submit Order')

    # st.write(my_insert_stmt)
    
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered '+name_an_order+'!', icon="✅")

