# Retail Sales Analytics Dashboard
- Python
- Excel

---

## Business Questions Solved

- Which products generate the highest revenue?
- Which regions perform best?
- What are the monthly sales trends?
- Which customer segments are most profitable?
- Which products should be promoted more?

---

## Key Insights

- Total Revenue exceeded $2.2M
- Technology products generated the highest sales
- Western region had the strongest performance
- Sales increased significantly during Q4

---

## Dashboard Preview

![Dashboard Preview](screenshots/dashboard-preview.png)

---

## SQL Analysis Example

```sql
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM retail_sales
GROUP BY category
ORDER BY total_sales DESC;
```

---

## Python Analysis Example

```python
import pandas as pd

sales = pd.read_csv('retail_sales.csv')

print(sales.groupby('Category')['Sales'].sum())
```

---

## Business Impact

This dashboard enables businesses to:

- Identify profitable products
- Improve sales strategy
- Monitor regional performance
- Support executive decision-making
