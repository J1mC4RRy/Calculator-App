import streamlit as st

# Create a Streamlit app title
st.title("Monthly Expense Calculator")

# Input fields for expenses
house_rent = st.number_input("House Rent", value=0)
utilities = st.number_input("Utilities", value=0)
car = st.number_input("Car", value=0)
grocery = st.number_input("Grocery", value=0)

# Calculate the total expense
total_expense = house_rent + utilities + car + grocery

# Display the total expense
st.write(f"Total Expense: ${total_expense:.2f}")
