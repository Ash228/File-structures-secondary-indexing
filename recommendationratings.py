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
#rating prediction
reader = Reader()
ratings = pd.read_csv(path+'\\data\\ratings.csv')
print(ratings.head())
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'ratings']], reader)
svd = SVD()
print(cross_validate(svd, data, measures=['RMSE', 'MAE'],cv=5))
trainset = data.build_full_trainset()
print(svd.fit(trainset))
print(ratings[ratings['userId'] == 1])
print(svd.predict(1, 100, 3))'''

movies = pd.read_csv(path+'\\data\\movies.csv')
ratings = pd.read_csv(path+'\\data\\ratings.csv')
print(movies)
print(ratings)
final_dataset = ratings.pivot(index='movieId',columns='userId',values='ratings')
final_dataset.fillna(0,inplace=True)
print(final_dataset)
'''no_user_voted = ratings.groupby('movieId')['ratings'].agg('count')
no_movies_voted = ratings.groupby('userId')['ratings'].agg('count')
f,ax = plt.subplots(1,1,figsize=(16,4))
# ratings['rating'].plot(kind='hist')
plt.scatter(no_user_voted.index,no_user_voted,color='mediumseagreen')
plt.axhline(y=10,color='r')
plt.xlabel('MovieId')
plt.ylabel('No. of users voted')
plt.show()
final_dataset = final_dataset.loc[no_user_voted[no_user_voted > 10].index,:]
final_dataset=final_dataset.loc[:,no_movies_voted[no_movies_voted > 50].index]
print(final_dataset)
f,ax = plt.subplots(1,1,figsize=(16,4))
plt.scatter(no_movies_voted.index,no_movies_voted,color='mediumseagreen')
plt.axhline(y=50,color='r')
plt.xlabel('UserId')
plt.ylabel('No. of votes by user')
plt.show()'''
csr_data = csr_matrix(final_dataset.values)
print(csr_data)
final_dataset.reset_index(inplace=True)
knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
knn.fit(csr_data)

def get_movie_recommendation(movie_name):
    n_movies_to_reccomend = 10
    movie_list = movies[movies['title'].str.contains(movie_name)]
    if len(movie_list):
        movie_idx= movie_list.iloc[0]['movieId']
        movie_idx = final_dataset[final_dataset['movieId'] == movie_idx].index[0]
        distances , indices = knn.kneighbors(csr_data[movie_idx],n_neighbors=n_movies_to_reccomend+1)
        rec_movie_indices = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]
        recommend_frame = []
        for val in rec_movie_indices:
            movie_idx = final_dataset.iloc[val[0]]['movieId']
            idx = movies[movies['movieId'] == movie_idx].index
            recommend_frame.append({'Title':movies.iloc[idx]['title'].values[0],'Distance':val[1]})
        df = pd.DataFrame(recommend_frame,index=range(1,n_movies_to_reccomend+1))
        return df
    else:
        return "No movies found. Please check your input"

print(get_movie_recommendation(input('enter movie name:')))


