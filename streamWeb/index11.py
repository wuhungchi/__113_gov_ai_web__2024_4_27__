import streamlit as st 
tab1,tab2,tab3 = st.tabs(['cat','dog','owl'])

with tab1:
    st.header("A Cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A Dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("A Owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)