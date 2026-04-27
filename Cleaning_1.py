import pandas as pd
df=pd.read_csv("C:/Users/Lenovo/OneDrive/Desktop/Data analysis Project_1 (data set)/online_retail_2.csv")

print("Display First 10 Rows")
print(df.head(10))

print("Display Last 10 Rows")
print(df.tail(10))

print("Dispaly the Information About the Dataset")
print(df.info())

print("Shape of the Data set : ")
print(df.shape)

print("Column Names :")
print(df.columns)

df = df.dropna(subset=["Customer ID"])

df = df[~df["Invoice"].astype(str).str.startswith("C")]

df = df[df["Quantity"] > 0]

df = df[df["Price"] > 0]

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df.info()

df["Revenue"] = df["Quantity"] * df["Price"]

df.head()

total_revenue = df["Revenue"].sum()
print("Total Revenue:", total_revenue)

total_customers = df["Customer ID"].nunique()
print("Total Customers:", total_customers)

total_transactions = df["Invoice"].nunique()
print("Total Transactions:", total_transactions)

average_order_value = total_revenue / total_transactions
print("Average Order Value:", average_order_value)

start_date = df["InvoiceDate"].min()
end_date = df["InvoiceDate"].max()

print("Start Date:", start_date)
print("End Date:", end_date)

df.to_csv("online_retail_cleaned.csv", index=False)





