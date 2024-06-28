import streamlit as st
import pandas as pd

st.title("Data App Assignment, on June 20th")

# Load the dataset
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=True)

# Display the dataframe
st.dataframe(df)

# Display the column names
st.write("### DataFrame Columns")
st.write(df.columns)


