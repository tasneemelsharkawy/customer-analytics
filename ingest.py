import sys
import pandas as pd

# 1. get file path from command line
file_path = sys.argv[1]

# 2. load dataset
df = pd.read_csv(file_path)

# 3. save a copy
df.to_csv("data_raw.csv", index=False)

print("Dataset loaded and saved as data_raw.csv")