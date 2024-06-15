import streamlit as st 
if 'wu' not in st.session_state:
    st.session_state['wu']= 29
    
st.session_state['wu']
st.session_state.wu = 20
st.session_state.wu