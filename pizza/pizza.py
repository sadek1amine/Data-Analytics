import pandas as pd
import matplotlib.pyplot as plt

transactions = pd.read_csv("transaction.csv")
products = pd.read_csv("product.csv") 
price_history = pd.read_csv("price_history.csv")


transactions["order_date"] = pd.to_datetime(transactions["order_date"])
price_history["effective_date"] = pd.to_datetime(price_history["effective_date"])


merged = transactions.merge(price_history, on="pizza_id", how="left")


valid_prices = merged[merged["effective_date"] <= merged["order_date"]]


valid_prices = valid_prices.sort_values(
    ["order_detail_id", "effective_date"],
    ascending=[True, False]
)

latest_price = valid_prices.drop_duplicates("order_detail_id")


latest_price["revenue"] = latest_price["quantity"] * latest_price["price"]


result = latest_price[[
    "order_detail_id",
    "order_id",
    "order_date",
    "pizza_id",
    "quantity",
    "price",
    "revenue"
]]

print(result)


total_revenue = result["revenue"].sum()
print("\nTOTAL REVENUE:", total_revenue)

result.groupby("order_date")["revenue"].sum().plot(kind="line")
plt.title("Daily Revenue")
plt.show()
