# UNSUPERVISED DATA

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Mall_Customers.csv")
print(data)

print("customer data")
print(df.isnull().sum())
X=df.iloc[:,[3,4]].values
print(X)

wcss = []

for i in range(1,11)
    kmeans = KMeans(n_clusters = i,init = "k-means++",random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
sns.set()
plt.plot(range(1,11),wcss)
plt.title("elbow graph")
plt.xlabel("number of clusters")
plt.ylabel("wcss")
plt.show()

clusters = 5

kmeans = KMeans(n_clusters = 5,init = "k-means++",random_state = 0)

Y = kmeans.fit_predict(X)

print(Y)

clusters=0,1,2,3,4#plotting #scattering

plt.figure(figsize=(8,8))
plt.scatter(X[Y==0,0],X[Y==0,1],s=50, c='blue',label='cluster 1')
plt.scatter(X[Y==1,0],X[Y==1,1],s=50, c='red',label='cluster 2')
plt.scatter(X[Y==2,0],X[Y==2,1],s=50, c='green',label='cluster 3')
plt.scatter(X[Y==3,0],X[Y==3,1],s=50, c='yellow',label='cluster 4')
plt.scatter(X[Y==4,0],X[Y==4,1],s=50, c='violet',label='cluster 5')


# centroids
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='cyan',label='centroids')
plt.title("customer groups")
plt.xlabel("annual income")
plt.show()

# STEPS:
# preprocessing
# load algorithm
# predict elbow graph
# clusters of elbow graph given to algorithm
# plot graph
