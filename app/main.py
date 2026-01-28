import streamlit as st
# (Presupunem că importăm funcția de mai sus)

st.title("💎 InsightHub Pro")
topic = st.text_input("Introdu subiectul cercetării:")

if st.button("Lansează Cercetarea"):
    st.info(f"Agentul caută informații despre: {topic}")
    # Aici vom integra logica reală mai târziu