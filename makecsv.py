prev = 0
started = False
index = 0

filename = 'CW4Test_Data.txt'

# search for the magic 10 minutes
with open(filename) as openfileobject:
    for line in openfileobject:
        # skip blank lines
        if line == '\n': continue
        datetime = line.split('\t')[0]
        num = float(line.split('\t')[1])
        # print(num)
        if index == 0:
            prev = num
            index += 1
            continue
        # this code also ensures only around-10 minutes intervals are printed
        if abs(num - prev) > 1.00:
            if not started:
                tracker = num
                start_index = index
                start_datetime = datetime
                start_prev = prev
                start_num = num
            else:
                end_index = index
                end_datetime = datetime
                end_prev = prev
                end_num = num
                if abs(prev - tracker) > 200 and abs(prev - tracker) < 700:
                    print('start of 10 minutes: ')
                    print('index: ', start_index, '\ntime stamp: ', start_datetime, '---', start_prev, start_num, '\n')
                    print('end of 10 minutes: ')
                    print('index: ', end_index, '\ntime stamp: ', end_datetime, '---', end_prev, end_num, '\n')

                    # unique storage
                    unique_start_index = start_index
                    unique_end_index = end_index


            started = not started
        prev = num
        index += 1

openfileobject.close()

# code 2
import pandas as pd

unique_start_index = unique_end_index
unique_end_index = unique_start_index + 30000

duration = unique_end_index - unique_start_index
# read in the tab-separated values
df = pd.read_csv(filename, sep='\t', lineterminator='\n', header=None, skiprows=unique_start_index, nrows= duration,
names = ['date/time', 'seconds since started', 'is button down?',
'accelX', 'accelY', 'accelZ', 'posX', 'posY', 'posZ', 'rotX', 'rotY', 'rotZ'])

# parse only the useful variables
df = df[['date/time', 'seconds since started','posX', 'posY', 'posZ', 'rotX', 'rotY', 'rotZ']]

print(df.shape)

print('finish loading into pandas')


import matplotlib.pyplot as plt

# a scatter plot comparing num_children and num_pets
df.plot(kind='scatter',x='posX',y='posZ',color='red')
plt.show()

df.to_csv('export_dataframe.csv', index = None, header=True)