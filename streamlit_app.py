import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Oatmeal')
streamlit.text('🥗 Kale spinach smoothie')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# We want pandas to read our CSV file from that S3 bucket so we use a pandas function called read_csv to pull the data into a dataframe we'll call my_fruit_list. 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# After pulling the data into a pandas dataframe called my_fruit_list, we will ask the streamlit library to display it on the page by typing:
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page
streamlit.dataframe(my_fruit_list)

# The picker works, but the numbers don't make any sense! We want the customer to be able to choose the fruits by name!!
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

# We want to filter the table data based on the fruits a customer will choose, so we'll pre-populate the list to set an example for the customer
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

