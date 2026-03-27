import pandas as pd

df = pd.read_csv("data_preprocessed.csv")
df.head()

df.info()
df.describe()

#histogram
import matplotlib.pyplot as plt
import seaborn as sns

df.hist(figsize=(10,8))
plt.savefig("summary_plot.png")

#pairplot
sns.pairplot(df)
plt.savefig("pairplot.png")

#heatmap
numeric_df = df.select_dtypes(include=['int64', 'float64'])

plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True)
plt.savefig("heatmap.png")

plt.tight_layout()
plt.savefig("summary_plot.png")