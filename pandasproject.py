import pandas as pd
from datetime import datetime

# Simulate Sales Data
data = {
    "Date": ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05"],
    "Product": ["Product_A", "Product_B", "Product_A", "Product_C", "Product_B"],
    "Quantity": [10, 5, 8, 2, 7],
    "Price": [20, 30, 20, 50, 30]
}
df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)

# Read Sales Data
df = pd.read_csv("sales_data.csv")
print("Sales Data:")
print(df)

# Data Cleaning
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df.drop_duplicates(inplace=True)
print("Cleaned Data:")
print(df.info())

# Data Analysis
df['Total_Sales'] = df['Quantity'] * df['Price']
average_sales = df['Total_Sales'].mean()
print(f"Average Sales: {average_sales}")
sales_by_product = df.groupby('Product')['Total_Sales'].sum()
print("Total Sales by Product:")
print(sales_by_product)
df['Month'] = df['Date'].dt.to_period('M')
sales_by_month = df.groupby('Month')['Total_Sales'].sum()
print("Total Sales by Month:")
print(sales_by_month)

# Save Results
df.to_csv("cleaned_sales_data.csv", index=False)
sales_by_product.to_csv("sales_by_product.csv")
sales_by_month.to_csv("sales_by_month.csv")
print("Data cleaning and analysis results have been saved to CSV files.")
