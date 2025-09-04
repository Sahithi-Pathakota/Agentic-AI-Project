# 📌 Save this as main.py
%%writefile main.py
import streamlit as st
from auth import login, signup, logout
import google.generativeai as genai

# 🔑 Configure Gemini
genai.configure(api_key="AIzaSyBCsR_YpBDIeonq3UcdQPl10bIK29ylLVM")  # Replace with your actual key
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(user_query):
    try:
        response = model.generate_content(user_query)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

# 🚀 Main App
def main():
    st.set_page_config(page_title="FindMyStore Chatbot", page_icon="🛍")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.sidebar.title("🔐 Account Access")
        choice = st.sidebar.radio("Choose an option", ["Login", "Sign Up"])
        if choice == "Login":
            login()
        else:
            signup()
        return

    # ✅ Logged-in section
    st.sidebar.success(f"Logged in as {st.session_state.username}")
    logout()

    st.title("🛍 FindMyStore Chatbot")
    st.caption("Ask about nearby stores and availability")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("💬 Ask something:", placeholder="e.g. Where to buy iPhone near me?")
        submitted = st.form_submit_button("Ask")

    if submitted and user_input:
        st.session_state.chat_history.append(("You", user_input))
        with st.spinner("Gemini is thinking..."):
            reply = get_gemini_response(user_input)
        st.session_state.chat_history.append(("Bot", reply))

        # 🏬 Simulated store results
        stores = [
            {"name": "SmartBuy Electronics", "location": "Banjara Hills", "distance": "1.5 km", "available": "Yes"},
            {"name": "GadgetZone", "location": "Ameerpet", "distance": "3.2 km", "available": "Limited"},
            {"name": "Tech Hub", "location": "Hitech City", "distance": "5.1 km", "available": "Out of Stock"},
        ]
        st.markdown("### 🏬 Nearby Stores")
        for s in stores:
            map_link = f"https://www.google.com/maps/search/?api=1&query={s['name'].replace(' ', '+')}+{s['location'].replace(' ', '+')}"
            st.markdown(f"""📍 {s['name']}**
- 🗺 Location: {s['location']}
- 📏 Distance: {s['distance']}
- 📦 Available: {s['available']}
[🧭 Directions]({map_link})
---
""")

    # 💬 Display chat history
    if st.session_state.chat_history:
        st.markdown("### 🗨 Chat History")
        for sender, msg in st.session_state.chat_history:
            st.markdown(f"{sender}:** {msg}")

if __name__ == "__main__":
    main()