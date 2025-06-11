import streamlit as st

st.title("My Shopping List")

shopping_items = ["Bananas", "Apples", "Salad", "Pasta", "Milk"]

st.write("Here is your list:")

for item in shopping_items:
    st.write(f"• {item}")