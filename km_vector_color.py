import os
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
# from mpl_toolkits import mplot3d

def find_vector(subdirect, filename):
    vec = list()
    data = pd.read_csv(os.path.join(subdirect, filename))
    # print(subdirect)
    X = data['posX'].values[0:30000:1000]
    Y = data['posZ'].values[0:30000:1000]
    if len(X) != 30 or len(Y) != 30:
        # false/terminate
        return vec

    # plt.scatter(X, Y)
    # plt.show()

    for x in X:
        vec.append(x)
    for y in Y:
        # print(y)
        vec.append(y)
    # print(vec)
    # quit()
    return vec


rootdir = os.getcwd()
arr = list()

# dictionary
row_dict = list()

# hardcord
SUBDIRECT = None

count = 0
# actual processing files
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if '.csv' in file:
            #quit()

            # ONE TIME THING
            if not SUBDIRECT:
                SUBDIRECT = subdir

            tmp = find_vector(subdir, file)
            if not tmp:
                print('Invalid file (for this decimation strategy): ', file)
                continue
            arr.append(tmp)
            row_dict.append(file)

# print('arr:', arr)
# print('=======================')
X = np.array(arr)
# print('X:', X)
# print(np.unique(list(map(len, X))))
# number of clusters*****************
k = 8

# Machine Learning
kmeans = KMeans(n_clusters = k)
# important code:
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
print(y_kmeans)

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

# for item in clusters:
#     print("Cluster ", item)
#     for i in clusters[item]:
#         print(i)

for item in clusters:
    print("Cluster ", item)
    print(clusters[item])

# Plot points by clusters
# Reorganize the printings
for item in clusters:
    print("Cluster ", item)
    for i in clusters[item]:
        data = pd.read_csv(os.path.join(SUBDIRECT, i))
        X = data['posX'].values[0:30000:1000]
        Y = data['posZ'].values[0:30000:1000]
        plt.scatter(X, Y, cmap='bwr')
    plt.show()
