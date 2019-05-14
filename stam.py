import numpy as np; 
np.random.seed(0)

import seaborn as sns; 
sns.set()
uniform_data = np.random.rand(10, 12)

ax = sns.heatmap(data, annot=True)

plt.imshow(data((12,12)));

plt.matshow(data((12, 12)))



# Plot the data
#plt.plot(data[:, 1], data[:, 10])
#plt.axis('equal')
plt.xlabel(headers[1])
plt.ylabel(headers[0])
plt.show()

plt.plot(data[:, 12])
plt.xlabel('Table Index')
plt.ylabel(headers[1])
plt.show()



import matplotlib.pyplot as plt
import numpy as np


def samplemat(dims):
    """Make a matrix with all zeros and increasing elements on the diagonal"""
    aa = np.zeros(dims)
    for i in range(min(dims)):
        aa[i, i] = i
    return aa


# Display matrix
plt.matshow(samplemat((15, 15)))

plt.show()




import numpy as np
import matplotlib.pyplot as plt

plt.imshow(np.random.random((50,50)));
plt.colorbar()
plt.show()