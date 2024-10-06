import random 
import streamlit as st
import time
start_button = st.button("Start")
howmany = st.number_input("How many numbers to add", 5, 15)
SUM_OF_NUMBERS = 0
running_total = 0 
NUMBERS = []
if start_button:
   
    print("hi")
     # Separate variable to store the running total

    NUMBERS = [random.randrange(99) for _ in range(howmany)]

    for number in NUMBERS:
        time.sleep(1.5)
        running_total += number
        st.text(number)
        

    SUM_OF_NUMBERS = running_total  # Set sum_of_numbers after the loop

status_text = st.empty()  # Create an empty slot for updating text
ans = st.text_input('Answer')

submit = st.button("Submit")
# st.text(NUMBERS)
if submit:
    st.text(NUMBERS)
    st.text(ans)
    if SUM_OF_NUMBERS == ans:
        print("Congratulations! You got it right")
        
    else:
        print("Oh No! That's not correct.")
        
    
