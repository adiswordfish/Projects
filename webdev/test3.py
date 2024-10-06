import random 
import streamlit as st
import time

# Initialize session state
if 'start_button_clicked' not in st.session_state:
    st.session_state.start_button_clicked = False

if 'pause_button_clicked' not in st.session_state:
    st.session_state.pause_button_clicked = False

if 'sum_of_numbers' not in st.session_state:
    st.session_state.sum_of_numbers = 0

if 'timer_started' not in st.session_state:
    st.session_state.timer_started = False

if 'start_time' not in st.session_state:
    st.session_state.start_time = 0

if 'elapsed_time' not in st.session_state:
    st.session_state.elapsed_time = 0

start_button = st.button("Start")

howmany = st.number_input("How many numbers to add", 5, 15)

if start_button:
    st.session_state.start_button_clicked = True
    numbers = [random.randrange(99) for _ in range(howmany)]
    for number in numbers:
        st.session_state.sum_of_numbers += number 
        st.text(number)
        time.sleep(1.5)
    
    st.session_state.timer_started = True
    st.session_state.elapsed_time = 0
    st.session_state.start_time = time.time()

status_text = st.empty()  # Create an empty slot for updating text
ans = st.text_input('Answer')

pause_button = st.button("Submit")

if st.session_state.timer_started and not st.session_state.pause_button_clicked:
    st.session_state.elapsed_time = time.time() - st.session_state.start_time
    seconds = int(st.session_state.elapsed_time)
    milliseconds = int((st.session_state.elapsed_time - seconds) * 1000)
    status_text.text(f" Elapsed Time: {seconds} seconds {milliseconds} milliseconds")

if st.session_state.pause_button_clicked:
    if st.session_state.sum_of_numbers == int(ans):
        st.text("Congratulations! You got it right")
        time.sleep(100)
        if st.button("Try again"):
            st.experimental_rerun()
    else:
        st.text("Oh No! You didn't get it in time!")
        time.sleep(100)
        if st.button("Restart"):
            st.experimental_rerun()

# Check if the 30 seconds timer is completed
if st.session_state.elapsed_time >= 30:
    st.text("Sorry, you were not able to finish the addition in time. Try again?")
    if st.button("Once more?"):
        st.experimental_rerun()
