import streamlit as st
from corrector import correct_code

st.set_page_config(page_title="Code Syntax & Semantic Corrector", layout="centered")

st.title("🛠️ Code Corrector with CodeT5")
st.write("Type or paste buggy code below and get corrected suggestions!")

code_input = st.text_area("Enter your code here:", height=300, placeholder="def foo(x)\n    return x+1")

if st.button("Correct Code"):
    if code_input.strip():
        with st.spinner("Analyzing and correcting code..."):
            corrected = correct_code(code_input)
            st.success("✅ Corrected Code")
            st.code(corrected, language="python")
    else:
        st.warning("Please enter some code.")
