import numpy as np
import pandas as pd

size = 1000

for j in range(5):
	vals = np.zeros(size)
	for i in range(size):
		vals[i] = np.random.random()

	d = {'data': vals}
	df = pd.DataFrame(data=d)
	df.to_csv("datafile_{}.csv".format(j+1),index=False)