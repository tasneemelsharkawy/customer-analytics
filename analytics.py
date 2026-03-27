import pandas as pd

# 1. load cleaned data
df = pd.read_csv("data_preprocessed.csv")

# 2. total revenue
total_revenue = df["Total Spent"].sum()
print("Total Revenue:", total_revenue)

# 3. most used payment method
top_payment = df["Payment Method"].value_counts().idxmax()
print("Most used payment method:", top_payment)

# 4. top selling category
top_category = df["Category"].value_counts().idxmax()
print("Top selling category:", top_category)
# 5. top selling (Online/Instore)
top_location = df["Location"].value_counts().idxmax()
print("Top selling (Online/Instore):", top_location)