import streamlit as st
from resume_parser import get_resume_text
from question_generator import extract_skills, generate_questions
#import streamlit as st

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}     /* Hides GitHub + Menu */
    header {visibility: hidden;}        /* Hides top bar */
    footer {visibility: hidden;}        /* Hides “Made with Streamlit” */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("AI Interview Question Generator")

uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf","docx"])

if uploaded_file:
    st.info("Extracting resume text...")
    text = get_resume_text(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.write(text)

    skills = extract_skills(text)
    st.subheader("Extracted Skills")
    st.write(skills)

    questions = generate_questions(skills)
    st.subheader("Generated Interview Questions")

    if questions:
        for q in questions:
            st.write("➡️", q)
    else:
        st.warning("No matching skills found")

