import streamlit as st
import PyPDF2
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.title("📘 AI Study Helper")

# ✅ File uploader
uploaded_file = st.file_uploader("Upload notes (PDF/TXT)", type=["pdf", "txt"])

llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()

if uploaded_file:
    # Handle PDF
    if uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    else:
        # Handle TXT
        text = uploaded_file.read().decode("utf-8", errors="ignore")

    st.success("✅ File uploaded successfully!")
    st.write("### Preview of content:")
    st.write(text[:500])  # show first 500 characters

    # Summarization
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful study assistant."),
        ("user", "Summarize the following text:\n{text}")
    ])
    chain = prompt | llm | output_parser
    summary = chain.invoke({"text": text})

    st.subheader("📖 Summary")
    st.write(summary)

    # Flashcards
    prompt_flashcards = ChatPromptTemplate.from_messages([
        ("system", "Create 3 flashcards from the text."),
        ("user", "{text}")
    ])
    chain_flashcards = prompt_flashcards | llm | output_parser
    flashcards = chain_flashcards.invoke({"text": text})

    st.subheader("🃏 Flashcards")
    st.write(flashcards)

    # Quiz
    prompt_quiz = ChatPromptTemplate.from_messages([
        ("system", "Generate 3 multiple-choice questions with answers."),
        ("user", "{text}")
    ])
    chain_quiz = prompt_quiz | llm | output_parser
    quiz = chain_quiz.invoke({"text": text})

    st.subheader("📝 Quiz")
    st.write(quiz)
