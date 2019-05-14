import cdsw
import csv
import numpy as np

# this is for the none suited cards
data_path = 'test_ns.csv'
with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # get header from first row
    headers = next(reader)
    # get all the rows as a list
    data2 = list(reader)
    # transform data into numpy array
    data2 = np.array(data2).astype(float)
    

def getOddsNS(args):
  result = data2[args["a"],args["b"]]
  return result

