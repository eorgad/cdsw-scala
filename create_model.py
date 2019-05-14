import cdsw
import csv
import numpy as np
import matplotlib.pyplot as plt

data_path = 'test.csv'
with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # get header from first row
    headers = next(reader)
    # get all the rows as a list
    data = list(reader)
    # transform data into numpy array
    data = np.array(data).astype(float)
    
print(headers)
print(data.shape)
print(data[:14])

import seaborn as sns; 
sns.set()
ax = sns.heatmap(data, annot=True)


data_path2 = 'test_ns.csv'
with open(data_path2, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # get header from first row
    headers = next(reader)
    # get all the rows as a list
    data2 = list(reader)
    # transform data into numpy array
    data2 = np.array(data2).astype(float)
    
print(headers)
print(data2.shape)
print(data2[:14])

import seaborn as sns; 
sns.set()
ax = sns.heatmap(data2, annot=True)



###############################################


