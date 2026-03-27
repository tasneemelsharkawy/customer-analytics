import sys
import pandas as pd

filepath = sys.argv[1]

df = pd.read_csv(filepath)
df.to_csv("data_raw.csv", index=False)

print("Loaded", len(df), "rows")
print("Saved to data_raw.csv")

import subprocess
subprocess.run(["python", "preprocess.py", "data_raw.csv"])
