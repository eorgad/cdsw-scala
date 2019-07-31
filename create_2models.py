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


# this is for the none suited cards
data_path = 'test_ns.csv'
with open(data_path, 'r') as f2:
    reader2 = csv.reader(f2, delimiter=',')
    # get header from first row
    headers2 = next(reader2)
    # get all the rows as a list
    data2 = list(reader2)
    # transform data into numpy array
    data2 = np.array(data2).astype(float)
    

def getOddsNS(args):
  result = data2[args["a"],args["b"]]
  return result

def getOdds2(args):
  if args["a"].startswith ('s'):
    result = data[args["b"],args["c"]]
  else:
    result = data2[args["b"],args["c"]]
  return result
