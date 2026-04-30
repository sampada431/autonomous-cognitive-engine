import streamlit as st

st.title("Autonomous Cognitive Engine 🧠")

st.write("This is your AI-powered system")

user_input = st.text_input("Enter your input:")

if st.button("Run Model"):
    result = f"Processed Output: {user_input}"
    st.success(result)
