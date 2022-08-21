import streamlit

streamlit.title('My Parents New Healthy Diner')


streamlit.header ('BreakFast Favourities')
streamlit.text('🥣 Omega 3 & Blueberry oat meal')
streamlit.text('🥗 Kale, Spinach & Rocket Smothie')
streamlit.text('🐔 Hard-Boiled Free Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit') # added to display the selected fruit name instead on number.
#streamlit.dataframe(my_fruit_list) # to display the data read from csv.
#Let's put a picklist here so that they can pick the fruit they want to include
streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
