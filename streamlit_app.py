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
streamlit.dataframe(my_fruit_list)
