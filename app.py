import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header("I am learning Streamlit")
st.subheader('And I am Loving it')

st.write('This is a normal text')

email = st.text_input('Enter email')
password = st.text_input('Enter Password')
btn = st.button('Login')
gender = st.selectbox('Select gender',['Male','female','others'])
if btn:
    if email == 'ronak@gmail.com' and password == '1234':
        st.balloons()
        st.write(gender)
        st.success('Login Successfull')

    else:
        st.error('Login Failed')

file = st.file_uploader('upload a csv file')
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())
st.markdown("""
### My favorite movies
 - Race 3
 - Housefull
 - Race 2
""")

st.code("""
def foo(input):
    return foo**2
    
x = foo(23)
""")

st.latex('x^2 + y^2 + 2 = 0')

df = pd.DataFrame({
    'name':['Nitish','Ankit','Anupam'],
    'marks':[50,60,70],
    'package':[10,12,14]
})
st.dataframe(df)
st.metric('Revenue','Rs 3L','-3%')
st.json({
    'name':['Nitish','Ankit','Anupam'],
    'marks':[50,60,70],
    'package':[10,12,14]
})

st.image('unnamed.jpeg')
st.sidebar.title('Sidebar Title')

col1 , col2 , col3 = st.columns(3)
with col1:
    st.image('unnamed.jpeg')

with col2:
    st.image('unnamed.jpeg')

with col3:
    st.image('unnamed.jpeg')

st.error('Login Failed')
st.success('Login Successful')
st.info('Login Successful')
st.warning('Login Successful')

bar = st.progress(0)

for i in range(1,101):
    bar.progress(i)


email = st.text_input('Enter Email')
number = st.number_input('Enter number')
date = st.date_input('Enter Date')


