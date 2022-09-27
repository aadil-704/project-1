import streamlit as st
import pandas as pd

st.write('hello this is my python project')
st.title('komal')
st.text_input('enter your name')
st.button('submit')
st.selectbox('select your education',
             (''
              'bsc','msc','phd'))
gender=st.radio("select your gender",('male','female','other')) # single value selection
if gender=="male":
    st.write("you have been selected male")
elif gender=="female":
    st.write("you have been selected female ")
else:
   st.write("others")
st.file_uploader("choose a file")
st.checkbox("machine learning")
st.checkbox("data warehouse")
st.checkbox("data mining")
st.sidebar.title("farhat")
st.sidebar.button("click")
df=pd.read_csv("Data/A.csv")
st.table(df)
st.sidebar.slider("choose a planet",['jupiter','mars','neptune'])
st.slider("pick a number",0,50)

