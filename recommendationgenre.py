import re
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

features = 'genre'
md = pd.read_csv(path+'/data/movies.csv')
'''
df2[features] = df2[features].apply(literal_eval)
print(df2)
def get_list(x):
    if isinstance(x, list):
        names = [i['name'] for i in x]
        #Check if more than 3 elements exist. If yes, return only first three. If no, return entire list.
        if len(names) > 3:
            names = names[:3]
        return names

    #Return empty list in case of missing/malformed data
    return []

df2

df2[features] = df2[features].apply(get_list)
print(df2)'''
s = md.apply(lambda x: pd.Series(x['genre']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'genre'
gen_md = md.drop('genre', axis=1).join(s)
print(gen_md)


def build_chart(genre, percentile=0.85):
    #df = gen_md[gen_md['genre'] == genre]
    df = gen_md[gen_md['genre'].str.contains(genre, flags=re.IGNORECASE)]
    print(df)
    '''vote_counts = df[df['no_of_ratings'].notnull()]['no_of_ratings'].astype('int')
    vote_averages = df[df['average_ratings'].notnull()]['average_ratings'].astype('int')
    C = vote_averages.mean()
    m = vote_counts.quantile(percentile)'''
    C = df['average_ratings'].mean()
    m = df['no_of_ratings'].quantile(0.9)
    #print(vote_counts.values,vote_averages.values)

    qualified = df[(df['no_of_ratings'] >= m) & (df['no_of_ratings'].notnull()) & (df['average_ratings'].notnull())][
        ['movieId','title', 'no_of_ratings', 'average_ratings']]
    qualified['no_of_ratings'] = qualified['no_of_ratings'].astype('int')
    qualified['average_ratings'] = qualified['average_ratings'].astype('int')

    qualified['wr'] = qualified.apply(
        lambda x: (x['no_of_ratings'] / (x['no_of_ratings'] + m) * x['average_ratings']) + (m / (m + x['no_of_ratings']) * C),axis=1)
    qualified = qualified.sort_values('wr', ascending=False).head(250)

    return qualified

print(build_chart('Comedy'))