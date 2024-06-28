import streamlit as st
import pandas as pd
import numpy as np

st.title("Data App Assignment, on June 20th")

# Load and display the dataset
st.write("### Input Data and Examples")
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=['Order Date'])
st.dataframe(df)

# Bar chart of sales by category
st.write("### Bar Chart of Sales by Category")
try:
    st.bar_chart(df, x="Category", y="Sales")
except KeyError:
    st.write("Error: 'Category' or 'Sales' column not found in the dataset")

# Aggregated bar chart of sales by category
st.write("### Aggregated Bar Chart of Sales by Category")
try:
    aggregated_df = df.groupby("Category", as_index=False).sum()
    st.dataframe(aggregated_df)
    st.bar_chart(aggregated_df, x="Category", y="Sales", color="#04f")
except KeyError:
    st.write("Error: 'Category' or 'Sales' column not found in the dataset")

# Aggregated sales by month
st.write("### Aggregated Sales by Month")
try:
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df.set_index('Order Date', inplace=True)
    sales_by_month = df.filter(items=['Sales']).groupby(pd.Grouper(freq='M')).sum()
    st.dataframe(sales_by_month)
    st.line_chart(sales_by_month, y="Sales")
except KeyError:
    st.write("Error: 'Order Date' or 'Sales' column not found in the dataset")

st.write("## Your additions")

# Data for categories and sub-categories
data = {
    'Category': ['Technology', 'Furniture', 'Office Supplies'],
    'Sub_Category': {
        'Technology': ['Phones', 'Appliances', 'Machines', 'Copiers'],
        'Furniture': ['Bookcases', 'Chairs', 'Tables', 'Storage', 'Furnishings'],
        'Office Supplies': [
            'Labels', 'Art', 'Binders', 'Paper', 'Accessories', 'Envelopes',
            'Fasteners', 'Supplies'
        ]
    }
}

# Step (1): Add a dropdown for Category
category = st.selectbox("Select a Category", data['Category'])

# Step (2): Add a multi-select for Sub_Category in the selected Category
if category:
    sub_categories = data['Sub_Category'][category]
    selected_sub_categories = st.multiselect(f"Select Sub-Categories in {category}", sub_categories)

# Display selected options
st.write(f"Selected Category: {category}")
st.write(f"Selected Sub-Categories: {selected_sub_categories}")

# Filter the dataframe based on selected category and sub-categories
if selected_sub_categories:
    try:
        filtered_df = df[(df['Category'] == category) & (df['Sub-Category'].isin(selected_sub_categories))]

        # Step (3): Show a line chart of sales for the selected items in (2)
        st.write("### Sales Line Chart")
        sales_chart = filtered_df.resample('M')['Sales'].sum().reset_index()
        st.line_chart(sales_chart, x='Order Date', y='Sales')

        # Calculate metrics
        total_sales = filtered_df['Sales'].sum()
        total_profit = filtered_df['Profit'].sum()
        overall_profit_margin = total_profit / total_sales * 100

        # Overall average profit margin for all products across all categories
        overall_avg_profit_margin = df['Profit'].sum() / df['Sales'].sum() * 100
        delta_profit_margin = overall_profit_margin - overall_avg_profit_margin

        # Step (4): Show three metrics
        st.write("### Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Sales", f"${total_sales:,.2f}")
        col2.metric("Total Profit", f"${total_profit:,.2f}")
        col3.metric("Overall Profit Margin", f"{overall_profit_margin:.2f}%", delta=f"{delta_profit_margin:.2f}%")
    except KeyError:
        st.write("Error: Required columns not found in the dataset")

st.write(f"Selected Category: {category}")
st.write(f"Selected Sub-Categories: {selected_sub_categories}")

