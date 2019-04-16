import scipy as sc
import numpy as np
import pandas as pd
from scipy.spatial.distance import mahalanobis

a = np.array([[1.65, 3, 0, 0, 0, 2, 1],
			  [4.00, 2, 0, 1, 1, 0, 0],
			  [4.00, 2, 0, 0, 2, 0, 0],
			  [3.50, 3, 1, 0, 0, 1, 1]
			  ], dtype=np.float64)
b = np.array([1.67, 2, 0, 2, 0, 0, 0, 0])

df = pd.DataFrame(a)
print(df)

#Calculate covariance matrix
covmx = df.cov()
print(covmx)
invvmx = sc.linalg.det(covmx)
print(invvmx)
invcovmx = sc.linalg.inv(covmx)

print(mahalanobis(b,a, invcovmx))