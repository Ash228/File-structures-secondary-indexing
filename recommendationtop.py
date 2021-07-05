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
'''
features = ['cast', 'crew', 'keywords', 'genres']
df2 = pd.read_csv(path+'/data/movies.csv')
for feature in features:
    df2[feature] = df2[feature].apply(literal_eval)'''
df2 = pd.read_csv(path+'/data/movies.csv')
print(df2)
df2 = df2.drop(['description','genre'],axis=1)
C=df2['average_ratings'].mean()
m = df2['no_of_ratings'].quantile(0.9)
q_movies = df2.copy().loc[df2['no_of_ratings'] >= m]
q_movies.shape
print(q_movies.shape)

def weighted_rating(x, m=m, C=C):
    v = x['no_of_ratings']
    R = x['average_ratings']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values('score', ascending=False)

#Print the top 15 movies
print(q_movies[['movieId','title', 'no_of_ratings', 'average_ratings', 'score']].head(10))
