import streamlit as st
import pandas as pd
import numpy as np

st.title("Data App Assignment, on June 20th")

st.write("### Input Data and Examples")

# Load the dataset and handle potential errors
try:
    df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=['Order Date'])
    st.dataframe(df)
except ValueError as e:
    st.error(f"Error loading the CSV file: {e}")
    st.stop()
except KeyError as e:
    st.error(f"Error: The specified column {e} was not found in the CSV file.")
    st.stop()

# Ensure the necessary columns exist in the dataframe
required_columns = ['Category', 'Sub-Category', 'Sales', 'Profit', 'Order Date']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error(f"The following required columns are missing in the CSV file: {missing_columns}")
    st.stop()

# Bar chart of sales by category
st.write("### Bar Chart of Sales by Category")
st.bar_chart(df, x="Category", y="Sales")

# Aggregated bar chart of sales by category
st.write("### Aggregated Bar Chart of Sales by Category")
aggregated_df = df.groupby("Category", as_index=False).sum()
st.dataframe(aggregated_df)
st.bar_chart(aggregated_df, x="Category", y="Sales", color="#04f")

# Aggregated sales by mont




