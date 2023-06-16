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

dt = pd.read_csv("./data/iris.csv")

st.write(dt.head(10))

dt1 = dt['petal.length'].sum()
dt2 = dt['petal.width'].sum()
dt3 = dt['sepal.length'].sum()
dt4 = dt['sepal.width'].sum()

dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])
if st.button("แสดงการจินตทัศน์ข้อมูล"):
   #st.write(dt.head(10))
   st.bar_chart(dx2)
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")