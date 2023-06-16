import streamlit as st

st.header('Treedanai')
st.image("./Pic/Treedanai.png")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Versicolor")
   st.image("./Pic/iris1.jpg")

with col2:
   st.header("Verginiga")
   st.image("./Pic/iris2.jpg")

with col3:
   st.header("Setosa")
   st.image("./Pic/iris3.jpg")