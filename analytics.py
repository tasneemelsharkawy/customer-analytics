import sys
import pandas as pd
import subprocess

if len(sys.argv) < 2:
    sys.exit(1)

df = pd.read_csv(sys.argv[1])
orig_df = pd.read_csv("data_raw.csv")

# Insight 1: total revenue
total_revenue = orig_df["Total Spent"].sum()
insight1 = f"Total Revenue: ${total_revenue:,.2f}"

# Insight 2: most used payment method
top_payment = orig_df["Payment Method"].value_counts().idxmax()
insight2 = f"Most used payment method: {top_payment}"

# Insight 3: top selling category
top_category = orig_df["Category"].value_counts().idxmax()
insight3 = f"Top selling category: {top_category}"

with open("insight1.txt", "w") as f:
    f.write(insight1)

with open("insight2.txt", "w") as f:
    f.write(insight2)

with open("insight3.txt", "w") as f:
    f.write(insight3)

print("3 insights saved")

# Call visualize.py
subprocess.run(["python", "visualize.py", sys.argv[1]])
