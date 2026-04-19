import sys
import pandas as pd
import matplotlib.pyplot as plt
import subprocess

if len(sys.argv) < 2:
    sys.exit(1)

file_path = sys.argv[1]
orig_df = pd.read_csv("data_raw.csv")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Plot 1: Top categories (meaningful)
orig_df['Category'].value_counts().head(10).plot(kind='bar', ax=axes[0])
axes[0].set_title('Top Categories')
axes[0].tick_params(axis='x', rotation=45)

# Plot 2: Payment methods (meaningful)
orig_df['Payment Method'].value_counts().plot(kind='pie', ax=axes[1], autopct='%1.1f%%')
axes[1].set_title('Payment Methods')

# Plot 3: Location (meaningful)
orig_df['Location'].value_counts().plot(kind='bar', ax=axes[2])
axes[2].set_title('Location')

plt.tight_layout()
plt.savefig('summary_plot.png')
print("Saved summary_plot.png")

subprocess.run(['python', 'cluster.py', file_path])
