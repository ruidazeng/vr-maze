# code 2
import pandas as pd


filename = 'AAAA.csv'
# read in the tab-separated values
df = pd.read_csv(filename, sep=',', lineterminator='\n')

print(df.shape)

print('finish loading into pandas')


import matplotlib.pyplot as plt

# a scatter plot comparing num_children and num_pets
df.plot(kind='scatter',x='posX',y='posZ',color='olive')
plt.show()