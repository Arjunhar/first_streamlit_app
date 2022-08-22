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
#Let's put a picklist here so that they can pick the fruit they want to include. Assigned the selected fruits to variable fruits_selected.
furits_selected = streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#Extract all the details from the csv file for the fruits in variable fruits_selected.
fruits_to_show = my_fruit_list.loc[furits_selected]

#display the table on the page with all the details for only selected fruits.
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruitvice fruit advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi') 
streamlit.write('The user entered ', fruit_choice)#accept user input

import requests
fruitvice_response= requests.get("https://www.fruityvice.com/api/fruit/watermelon" + fruit_choice)
streamlit.text(fruitvice_response.json()) #Just writes data to screen

#Normalise the json data using pandas 
fruityvice_normalized = pandas.json_normalize(fruitvice_response.json())
#Display the normalized data.
streamlit.dataframe(fruityvice_normalized)
