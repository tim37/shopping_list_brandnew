import streamlit as st

st.title("My Shopping List")

if "shopping_items" not in st.session_state:
    st.session_state.shopping_items = ["Bananas", "Apples", "Salad", "Pasta", "Milk"]

st.title("Shopping List")

# Show current items
st.write("Current items:")
for item in st.session_state.shopping_items:
    st.write(f"- {item}")

# Input to add new item
new_item = st.text_input("Add a new item:")

# Button to add the new item
if st.button("Add item"):
    if new_item.strip():  # Check that input isn't empty or just spaces
        st.session_state.shopping_items.append(new_item.strip())
        st.success(f'Added "{new_item.strip()}" to the list.')
    else:
        st.warning("Please enter a valid item.")

# Show updated list
st.subheader("Updated Shopping List:")
for item in st.session_state.shopping_items:
    st.write(f"- {item}")