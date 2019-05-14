import cdsw
import csv
import numpy as np

data_path = 'test.csv'
with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # get header from first row
    headers = next(reader)
    # get all the rows as a list
    data = list(reader)
    # transform data into numpy array
    data = np.array(data).astype(float)
    

def getOdds(args):
  result = data[args["a"],args["b"]]
  return result
