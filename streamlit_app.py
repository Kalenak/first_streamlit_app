import streamlit

streamlit.title('My Dad\'s Healthy Diner')

streamlit.header('Breakfast Favourites')

streamlit.text('Omega 3 & Blueberry Oatmeal🥣')
streamlit.text('Kale, Spinach & Rocket Smoothie🥗')
streamlit.text('Hard-Boiled Free Range Eggs🐔')
streamlit.text('Avocado on Toast🥑')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick a few fruits:", list(my_fruit_list.index), ['Banana','Lime'])

#display the table on the page
streamlit.dataframe(my_fruit_list)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

my_cur = my_cnx.cursor()

my_cur.execute("SELECT name from fruityvice")

my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
streamlit.text("The fruit load list contains:")

streamlit.text(my_data_rows)
