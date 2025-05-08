from sklearn.cluster import KMeans
import numpy as np
#define data set
x = np.array([
    [1, 1], [2, 1], [3, 1], 
    [10, 10], [11, 12], [12, 10], 
    [20, 20], [22, 21], [23, 20] 
])
#number of clusters - nc
nc=int(input("Enter the number of clusters: "))
kmeans = KMeans(nc,random_state=0)
kmeans.fit(x)
print(f"for {nc} clusters on given dataset\nthe centroids will be: \n {kmeans.cluster_centers_}")