import streamlit as st 

with st.form("my_form"):
    st.write("inside the form")
    slider_val = st.slider("From slider")
    checkbox_val = st.checkbox("From checkbox")
    #每一個form必需要有一個submit button
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")