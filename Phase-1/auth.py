# 📌 Save this as auth.py (Colab will auto-create this file)
%%writefile auth.py
import streamlit as st

users = {}  # In-memory user store

def signup():
    st.subheader("Sign Up")
    new_username = st.text_input("Choose a username")
    new_password = st.text_input("Choose a password", type="password")
    if st.button("Create Account"):
        if new_username in users:
            st.warning("Username already exists.")
        else:
            users[new_username] = new_password
            st.success("Account created! You can now log in.")

def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password.")

def logout():
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""