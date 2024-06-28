import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data App Assignment, on June 20th")

# Load the dataset
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=['Order Date'])

# Display the dataframe
st.dataframe(df)

# Display the column names
st.write("### DataFrame Columns")
st.write(df.columns)

# Identify the correct column names for Category and Sub-Category
# Replace 'Category' and 'Sub-Category' with actual column names from your dataset
category_col = "Category"  # Replace with actual column name for Category
sub_category_col = "Sub-Category"  # Replace with actual column name for Sub-Category

# Ensure 'Category' and 'Sub-Category' are in the dataframe
if category_col in df.columns and sub_category_col in df.columns:
    
    # (1) Add a drop down for Category
    category = st.selectbox("Select a Category", df[category_col].unique())

    # (2) Add a multi-select for Sub-Category in the selected Category
    sub_categories = df[df[category_col] == category][sub_category_col].unique()
    selected_sub_categories = st.multiselect("Select Sub-Categories", sub_categories)

    if selected_sub_categories:
        filtered_df = df[df[sub_category_col].isin(selected_sub_categories)]

        # (3) Show a line chart of sales for the selected items in (2)
        sales_by_month_filtered = filtered_df.resample('M', on='Order Date')['Sales'].sum()
        st.line_chart(sales_by_month_filtered)

        # (4) Show three metrics for the selected items in (2)
        total_sales = filtered_df['Sales'].sum()
        total_profit = filtered_df['Profit'].sum()
        overall_profit_margin = (total_profit / total_sales) * 100
        
        st.metric(label="Total Sales", value=f"${total_sales:,.2f}")
        st.metric(label="Total Profit", value=f"${total_profit:,.2f}")
        st.metric(label="Overall Profit Margin", value=f"{overall_profit_margin:.2f}%")

        # (5) Use the delta option in the overall profit margin metric
        overall_avg_profit_margin = (df['Profit'].sum() / df['Sales'].sum()) * 100
        profit_margin_delta = overall_profit_margin - overall_avg_profit_margin

        st.metric(
            label="Profit Margin Delta",
            value=f"{overall_profit_margin:.2f}%",
            delta=f"{profit_margin_delta:.2f}%"
        )
else:
    st.write("Error: 'Category' and 'Sub-Category' columns not found in the dataset")




