# code 2
import pandas as pd


filename = 'AAAA.csv'
# read in the tab-separated values
df1 = pd.read_csv(filename, sep=',', lineterminator='\n')
filename = 'ACGN.csv'
# read in the tab-separated values
df2 = pd.read_csv(filename, sep=',', lineterminator='\n')

colorGrad = []
for i in range(0,3000):
    colorGrad.append([i/3000,0, 1-i/3000])

print('finish loading into pandas')
X1 = df1['posX'].values[0:30000:10]
Y1 = df1['posZ'].values[0:30000:10]
X2 = df2['posX'].values[0:30000:10]
Y2 = df2['posZ'].values[0:30000:10]


import matplotlib.pyplot as plt
colorGrad = []
for i in range(0,3000):
    colorGrad.append([i/3000,0, 1-i/3000])

# a scatter plot comparing num_children and num_pets
plt.scatter(X1, Y1, c = colorGrad)
plt.scatter(X2, Y2, c = colorGrad)
plt.show()
