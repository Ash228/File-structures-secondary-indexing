from ast import literal_eval
from surprise import Reader, Dataset, SVD
from surprise.model_selection import cross_validate
import csv
import hashlib
import pathlib
import pandas as pd
from itertools import zip_longest
from primary_index import *
from secondary_index import *
from insert import *
from delete import *
from update import *
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import seaborn as sns

uid = -1
path = str(pathlib.Path().absolute())

features = ['cast', 'crew', 'keywords', 'genres']
df2 = pd.read_csv(path+'/data/movies.csv')
for feature in features:
    df2[feature] = df2[feature].apply(literal_eval)