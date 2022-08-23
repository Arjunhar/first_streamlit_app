import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents New Healthy Diner')


streamlit.header ('BreakFast Favourities')
streamlit.text('🥣 Omega 3 & Blueberry oat meal')
streamlit.text('🥗 Kale, Spinach & Rocket Smothie')
streamlit.text('🐔 Hard-Boiled Free Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit') # added to display the selected fruit name instead on number.
#streamlit.dataframe(my_fruit_list) # to display the data read from csv.
#Let's put a picklist here so that they can pick the fruit they want to include. Assigned the selected fruits to variable fruits_selected.
furits_selected = streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#Extract all the details from the csv file for the fruits in variable fruits_selected.
fruits_to_show = my_fruit_list.loc[furits_selected]

#display the table on the page with all the details for only selected fruits.
streamlit.dataframe(fruits_to_show)
#import requests
streamlit.header('Fruitvice fruit advice!')

def get_fruityvice_data(this_fruit_choice):
     fruitvice_response= requests.get("https://www.fruityvice.com/api/fruit/" + this_fruit_choice)
     #streamlit.text(fruitvice_response.json()) #Just writes data to screen
     #Normalise the json data using pandas 
     fruityvice_normalized = pandas.json_normalize(fruitvice_response.json())
     return fruityvice_normalized

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?') 
  if not fruit_choice:
     streamlit.error('Please select a fruit to get information')#accept user input
  else:
     back_from_function = get_fruityvice_data(fruit_choice)
     #Display the normalized data.
     streamlit.dataframe(back_from_function)
    
except urlerror as e:
    streamlit.error()

#import snowflake.connector
streamlit.header("The Fruit Load List Contains:")
def get_fruit_load_list():
     with my_cnx.cursor() as my_cur:
          my_cur.execute("select * from fruit_load_list")
          return my_cur.fetchall()

# add a button to extract the data from SF
if streamlit.button('Get Fruit Load List'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_rows = get_fruit_load_list()
     streamlit.dataframe(my_data_rows)

streamlit.header('Fruitvice fruit advice!')

def insert_row_snowflake(new_fruit):
     with my_cnx.cursor() as my_cur:
          my_cur.execute("insert into fruit_load_list values ('new_fruit')")
          return "Thanks for adding " + new_fruit
         
add_my_fruit = streamlit.text_input('What fruit would you like to add?') 
if streamlit.button('Add a fruit to the list'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     back_from_function = insert_row_snowflake(add_my_fruit)
     streamlit.text(back_from_function)
     
streamlit.stop() #stop running streamlit from this poitn onwards     
streamlit.write('Thanks for adding: ', add_my_fruit)#accept user input

my_cur.execute("INSERT INTO fruit_load_list values ('from streamlit')")
