# 🍕 Pizza Revenue Analytics Project

## 📊 Overview
This project is a **Data Analytics pipeline built with Python (Pandas)** that calculates **accurate pizza revenue over time** using historical pricing instead of current prices.

It simulates a real-world business scenario where product prices change over time.

---

## 🎯 Problem Statement
We have 3 datasets:

- `transaction.csv` → customer orders
- `product.csv` → pizza details (current price)
- `price_history.csv` → historical price changes

👉 The goal is to compute **true revenue based on the correct price at the time of each order**, not the current price.

---

## 🧠 Solution Approach

1. Load datasets using Pandas
2. Convert date columns to datetime
3. Match each order with the correct historical price:
   - `effective_date <= order_date`
   - Select the latest valid price

---

## 📈 Key Output

### 🧾 Sample Result

| order_id | pizza_id   | quantity | price | revenue |
|----------|------------|----------|-------|---------|
| 1001     | margherita | 2        | 8.0   | 16.0    |
| 1001     | pepperoni  | 1        | 9.0   | 9.0     |
| 1002     | hawaiian   | 3        | 9.5   | 28.5    |

---

## 💰 Total Revenue
