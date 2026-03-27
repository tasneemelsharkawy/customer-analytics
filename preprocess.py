import pandas as pd

df = pd.read_csv("data_raw.csv")
#first check
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))

print("\nDuplicates:", df.duplicated().sum())

print("\nMissing values per column:")
print(df.isnull().sum())

# drop rows where item is missing
df = df.dropna(subset=["Item"])

# fill with median
df["Price Per Unit"] = df["Price Per Unit"].fillna(df["Price Per Unit"].median())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Total Spent"] = df["Total Spent"].fillna(df["Total Spent"].median())

# fill discount with 0
df["Discount Applied"] = df["Discount Applied"].fillna(0)

df.to_csv("data_preprocessed.csv", index=False)
# second check
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))

print("\nDuplicates:", df.duplicated().sum())

print("\nMissing values per column:")
print(df.isnull().sum())