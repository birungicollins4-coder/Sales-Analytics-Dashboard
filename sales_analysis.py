import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('retail_sales.csv')

# Revenue Summary
print("Total Revenue:", sales['Sales'].sum())
print("Total Profit:", sales['Profit'].sum())

# Sales by Category
category_sales = sales.groupby('Category')['Sales'].sum()
print(category_sales)

# Monthly Trend
sales['Order Date'] = pd.to_datetime(sales['Order Date'])
sales['Month'] = sales['Order Date'].dt.month

monthly_sales = sales.groupby('Month')['Sales'].sum()

monthly_sales.plot(kind='line')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
