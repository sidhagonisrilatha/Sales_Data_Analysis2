import pandas as pd
import matplotlib.pyplot as plt

#load dataset
df = pd.read_csv("sales_data.csv")

#create a revenue colomn
df["Revenue"] = df["Quantity"] * df["Price"]

#Total sales
total_sales = df["Revenue"].sum()
print("Total sales:", total_sales)

#Top product
top_product = df.groupby("Product")["Revenue"].sum().idxmax()
print("Top product:", top_product)

#sales by region
region_sales = df.groupby("Region")["Revenue"].sum()
print(region_sales)

#plot chart 
region_sales.plot(kind="bar")
plt.title("Sales by region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()