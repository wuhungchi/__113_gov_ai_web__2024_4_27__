import streamlit as st
col1 ,col2 = st.columns(2)

with col1:
    st.title("這是欄位1")
    st.header("欄位1header")
    st.subheader("欄位1subheader")
    
with col2:
    st.title("這是欄位s")
    st.header("欄位2header")
    st.subheader("欄位2subheader")