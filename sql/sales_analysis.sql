
-- Retail Sales Analysis
-- Calculate Total Revenue

SELECT
    SUM(total_sales) AS total_revenue
FROM retail_sales;

-- Best-Selling Products by Revenue

SELECT
    product_name,
    SUM(quantity) AS total_quantity_sold,
    SUM(total_sales) AS total_revenue
FROM retail_sales
GROUP BY product_name
ORDER BY total_revenue DESC;

-- Category-Wise Sales Analysis

SELECT
    category,
    SUM(quantity) AS total_items_sold,
    SUM(total_sales) AS category_revenue
FROM retail_sales
GROUP BY category
ORDER BY category_revenue DESC;
