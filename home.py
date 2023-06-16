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

   html_8 = """
<div style="background-color:#EC7063;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")