#clustering
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data_preprocessed.csv")

X = df[["Price Per Unit", "Quantity", "Total Spent"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

counts = df['cluster'].value_counts()

for cluster, count in counts.items():
    print(f"Cluster {cluster}: {count}")
    
with open("clusters.txt", "w") as f:
    for cluster, count in counts.items():
        f.write(f"Cluster {cluster}: {count}\n")