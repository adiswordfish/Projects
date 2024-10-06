import streamlit as st
import random
import time

# st.set_page_config(
#     page_title="Multipage App",
#     page_icon="👋",
# )
# start_button = st.button("Start")

sum_of_numbers = 0
howmany = st.number_input("How many numbers to add", 2, 15)

# if start_button:
numbers = [random.randrange(99) for _ in range(howmany)]
for number in numbers:
        sum_of_numbers += number 
        st.text(number)
        time.sleep(1.5)
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
my_input = st.text_input("Answer:", st.session_state["my_input"])

submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)
    