import os
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits import mplot3d

def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist

def find_quadruple(subdirect, filename):
    quadruple = [0, 0, 0, 0]
    data = pd.read_csv(os.path.join(subdirect, filename))
    X = data['posX'].values
    Y = data['posZ'].values

    for x, y in zip(X, Y):
        one = calculateDistance(x, y, -2.5, 2.1)
        two = calculateDistance(x, y, -1.1, -2.0)
        three = calculateDistance(x, y, 1.5, -2.5)
        four = calculateDistance(x, y, 1.9, 1.35)

        epsilon = 0.8

        if one <= epsilon:
            quadruple[0] += 1

        if two <= epsilon:
            quadruple[1] += 1

        if three <= epsilon:
            quadruple[2] += 1

        if four <= epsilon:
            quadruple[3] += 1

    for i in range(4):
        quadruple[i] /= 30000
        quadruple[i] = round(quadruple[i], 3)

    return quadruple

rootdir = os.getcwd()
arr = list()

# dictionary
row_dict = list()

# actual processing files
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if '.csv' in file:
            qua = find_quadruple(subdir, file)
            arr.append(qua)
            row_dict.append(file)
# print('arr:', arr)
# print('=======================')
X = np.array(arr)
# print('X:', X)
# number of clusters*****************
k = 4

# Machine Learning
kmeans = KMeans(n_clusters = k)
# important code:
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
# print(y_kmeans)

# centers = kmeans.cluster_centers_
# plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);

# in row_dict we store actual meanings of rows, in my case it's russian words
clusters = {}
n = 0
for item in y_kmeans:
    if item in clusters:
        clusters[item].append(row_dict[n])
    else:
        clusters[item] = [row_dict[n]]
    n +=1

for item in sorted(clusters):
    print("Cluster ", item)
    for i in clusters[item]:
        print(i)

# Projection presentation (2D)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.show()
plt.scatter(X[:, 1], X[:, 2], c=y_kmeans, s=50, cmap='viridis')
plt.show()
plt.scatter(X[:, 2], X[:, 3], c=y_kmeans, s=50, cmap='viridis')
plt.show()
plt.scatter(X[:, 0], X[:, 2], c=y_kmeans, s=50, cmap='viridis')
plt.show()
plt.scatter(X[:, 0], X[:, 3], c=y_kmeans, s=50, cmap='viridis')
plt.show()
plt.scatter(X[:, 1], X[:, 3], c=y_kmeans, s=50, cmap='viridis')
plt.show()


# Plotting 3D
plt.axes(projection='3d')
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.show()
plt.axes(projection='3d')
plt.scatter(X[:, 1], X[:, 2], c=y_kmeans, s=50, cmap='viridis')
plt.show()
plt.axes(projection='3d')
plt.scatter(X[:, 2], X[:, 3], c=y_kmeans, s=50, cmap='viridis')
plt.show()
