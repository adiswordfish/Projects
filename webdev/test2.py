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
    timer_duration = 30
    start_time = time.time()
    paused_time = 0
    ans = st.text_input('Answer')
    pause_button = st.button("Submit")
    while True:
        
        if not pause_button:  # Check if the Pause button is not clicked
            elapsed_time = time.time() - start_time - paused_time
            seconds = int(elapsed_time)
            milliseconds = int((elapsed_time - seconds) * 1000)
            status_text.text(f" Elapsed Time: {seconds} seconds {milliseconds} milliseconds")
        while pause_button == True or False:
            if sum_of_numbers == ans:
                st.text("Congratulations! You got it right")
                time.sleep(100)
                if st.button("Restart"):
                    break
            else:
                st.text("Oh No! You didnt get it in time!")
                time.sleep(100)
                if st.button("Restart"):
                    break
        
        time.sleep(0.1)  # Adjust the sleep duration for better accuracy in milliseconds
        
        # Check if the 30 seconds timer is completed
        if elapsed_time >= timer_duration:
            st.text("Sorry you were not able to finish the addition in time. Try again?")
            if st.button("Restart"):
                    break
            break
            
        
