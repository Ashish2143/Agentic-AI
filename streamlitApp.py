import streamlit as st
import pandas as pd
import numpy as np

st.title("hello, Streamlit")
st.write(" :Streamlit: this is your first app")
st.text("lets get started ")

# First text input
name = st.text_input("Enter your name", key="name_input")
if st.button("great"):
    st.success(f"Hello {name}, welcome to Streamlit!")

df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])
st.line_chart(df)
st.bar_chart(df)

uploaded_file = st.file_uploader("Choose a file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    st.header("this is header")
    st.subheader("this is subheader")
    st.markdown(" **Bold**,*Italic*,'code',[link](https://streamlit.io/)")

    # Second text input with a different key
    st.text_input("Enter your name", key="name_input_2")
    st.text_area("Enter your message")
    st.number_input("Enter a number", min_value=0, max_value=100)
    st.slider("Select a range", 0, 100)
    st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
    st.multiselect("choose a color", ["Red", "Green", "Blue"])
    st.radio("Select a gender", ["Male", "Female"])
    st.checkbox("I agree to the terms and conditions")


option = st.radio("choose view", ["show chart", "show table"])
if option == "show chart":
    st.write("Displaying chart")
else:
    st.write("Displaying table")
 
 #form 
with st.form("Login Form"):
    username = st.text_input("Enter username:")
    password = st.text_input("Enter password", type="password")
    submitted = st.form_submit_button("Login")
    if submitted:
        st.success(f"Welcome {username}!")