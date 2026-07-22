import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.title("🍳 AI Recipe Generator")

ingredients = st.text_area("Enter ingredients you have at home:")

llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()

if ingredients:
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a creative chef."),
        ("user", "Suggest 3 unique recipes using these ingredients:\n{ingredients}")
    ])
    chain = prompt | llm | output_parser
    recipes = chain.invoke({"ingredients": ingredients})
    
    st.subheader("✨ Suggested Recipes")
    st.write(recipes)
