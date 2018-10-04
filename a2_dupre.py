import numpy as np
import pandas as pd
iris_dataset = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = np.recfromcsv(iris_dataset, encoding=None)  # in numpy
#iris = pd.read_csv(iris_dataset) # in pandas
sepal_length = np.array(iris['sepal_length'])
species = np.array(iris['species'])
species_unique = np.unique(species)
results = np.zeros([3,2]);
for nspecies in range(0,species_unique.size):
	sepLen_currentSpec = sepal_length[np.where(species==species_unique[nspecies])];
	results[nspecies,0] = np.mean(sepLen_currentSpec);
	results[nspecies,1] = np.std(sepLen_currentSpec);
print(results)
