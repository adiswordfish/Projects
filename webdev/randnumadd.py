import random 
import streamlit as st
import time

start = st.button("Start")
howmany = st.number_input("How many numbers to add", 5, 15)
if start: 
    # s = rand(1,99)
    # for i in range(howmany):
    #     s = random.random(1,99)
    # st.text(s)   
    [random.randrange(99) for i in range(howmany)]
    

    
    
