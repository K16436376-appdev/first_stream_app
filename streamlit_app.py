import streamlit
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Bolied Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


imprt pandas
my_fruit_list = panda.read_csv("https://uni-lab-.s3.us-west-2.amazonsaws.com/dawb/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
