import pandas as pd
df=pd.read_csv("C:/Users/Lenovo/OneDrive/Desktop/Data anylst Project_1/online_retail_cleaned.csv")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df.head()

df.info()
df.head(10)
print("Shape of the Datasets:")
print(df.shape)

customer_df = df.groupby("Customer ID").agg({
    "Revenue": "sum",
    "Invoice": "nunique",
    "Quantity": "sum",
    "InvoiceDate": ["min", "max"]
})

customer_df.columns = [
    "Total_Revenue",
    "Total_Orders",
    "Total_Items",
    "First_Purchase",
    "Last_Purchase"
]

customer_df= customer_df.reset_index()
customer_df.head()

customer_df["Customer_Lifespan"] = (
    customer_df["Last_Purchase"] - customer_df["First_Purchase"]
).dt.days

customer_df["AvgOrderValue"] = (
    customer_df["Total_Revenue"] / customer_df["Total_Orders"]
)

customer_df.to_csv("customer_dataset.csv", index=False)

