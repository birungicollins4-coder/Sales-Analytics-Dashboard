-- Total Sales and Profit
SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM retail_sales;

-- Sales by Category
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM retail_sales
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Regional Sales
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Regional_Sales
FROM retail_sales
GROUP BY Region
ORDER BY Regional_Sales DESC;
