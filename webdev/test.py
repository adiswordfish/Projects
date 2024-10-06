import random 
import streamlit as st
import time

start_button = st.button("Start")

sum_of_numbers = 0
howmany = st.number_input("How many numbers to add", 5, 15)

if start_button:
    numbers = [random.randrange(99) for _ in range(howmany)]
    for number in numbers:
        sum_of_numbers += number 
        st.text(number)
        time.sleep(1.5)
        
    
    status_text = st.empty()  # Create an empty slot for updating text
    status_text.text("Timer started.")

    start_time = time.time()
    paused_time = 0
    pause_button = st.button("Submit")
    while True:
        elapsed_time = time.time() - start_time - paused_time
        seconds = int(elapsed_time)
        milliseconds = int((elapsed_time - seconds) * 1000)
        status_text.text(f"Elapsed Time: {seconds} seconds {milliseconds} milliseconds")
        
        if pause_button:
            paused_time += time.time() - start_time
            status_text.text("Timer paused.")
            break
        
        time.sleep(0.1)  # Adjust the sleep duration for better accuracy in milliseconds

    done = status_text.text("Timer completed.")

    if done:
        st.text('Sorry you werent able to add in time. Try again next time')
