import streamlit as st 
st.bar_chart({"data":[1,2,5,3,4]})

with st.expander("See explanation"):
    st.markdown('''
## Chart above
- The chart above shows some numbers I picked for you.
- I rolled actual dice for these, so they're **guaranteed** 
                
> to be random. 
''')
    st.image("https://static.streamlit.io/examples/dice.jpg")