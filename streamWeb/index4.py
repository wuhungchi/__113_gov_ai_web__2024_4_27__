import streamlit as st 
import time


placehoder = st.empty()

with st.empty():
    for seconds in range(60):
        st.write(f"{seconds}seconds have passed")
        time.sleep(1)
        
    st.write("1 minute over!")

time.sleep(5)
placehoder.empty()