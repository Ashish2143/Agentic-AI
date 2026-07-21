import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.markdown(
    """
    <style>
    /* Big main title */
    .main-title {
        font-size: 50px;
        color: crimson ;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* Style the input box */
    .stTextInput input {
        background-color: #f0f8ff;
        border: 2px solid teal;
        border-radius: 8px;
        padding: 8px;
        font-size: 16px;
    }

    /* Style the output box */
    .answer-box {
        background-color: #fafafa;
        border-left: 5px solid teal;
        padding: 12px;
        margin-top: 20px;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🔹 Add big title above your existing one
st.markdown("<div class='main-title'>MY AIbot</div>", unsafe_allow_html=True)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant, please respond to the question asked."),
    ("user", "question: {question}")
])

st.title("Where should be begin!")
input_text = st.text_input("What question do you have:")

llm = Ollama(model="gemma2:2b")   

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))