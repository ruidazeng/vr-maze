# code 2
import pandas as pd

filename = 'AAAA.csv'

# read in the tab-separated values
df = pd.read_csv(filename, sep=',', lineterminator='\n')

print(df.shape)

print('finish loading into pandas')

df = df[df.index % 30 == 0]

from turtle import *

speed(10)
# penup()
color('olive')

setpos(df['posZ'][0] * 50, df['posX'][0] * -50)
for index, row in df.iterrows():
    goto(df['posZ'][index] * 50, df['posX'][index] * -50)
    dot()
done()

print('done')
