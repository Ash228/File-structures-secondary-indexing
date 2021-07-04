from primary_index import *
from secondary_index import *
import csv
import hashlib
import pathlib
import pandas as pd
from itertools import zip_longest

path = str(pathlib.Path().absolute())


def mdelete():
    id1 = input("Enter genre to delete ")
    dsk_movies= pd.read_csv(path+"\\data\\movsecondary.csv")
    dsk_movies = dsk_movies.loc[dsk_movies['genre'] == id1]
    if id1 in list(dsk_movies['genre']):
        print("Id exists")
        print(dsk_movies)
        while(1):
            id2 = int(input("enter one of the primary keys from above to delete "))
            if int(id2) in list(dsk_movies['movieId']):
                break
        dsk_movies = pd.read_csv(path+"\\data\\movsecondary.csv")
        i=dsk_movies.query('genre == @id1 & movieId == @id2').index
        dsk_movies = dsk_movies.drop(i)
        dsk_movies.to_csv(path+"\\data\\movsecondary.csv", index=False)
        dpk_movies = pd.read_csv(path+"\\data\\movprimary.csv")
        i = dpk_movies.query('id == @id2').index
        dpk_movies = dpk_movies.drop(i)
        dpk_movies.to_csv(path+"\\data\\movprimary.csv", index=False)
        df_movies = pd.read_csv(path+"\\data\\movies.csv")
        i = df_movies.query('movieId == @id2').index
        df_movies = df_movies.drop(i)
        df_movies.to_csv(path+"\\data\\movies.csv", index=False)
        print("Record deleted ")
    else:
        print("Record does not exist")


def rdelete():
    id1 = int(input("Enter ratings to delete "))
    dsk_ratings = pd.read_csv(path+"\\data\\rsecondary.csv")
    dsk_ratings = dsk_ratings.loc[dsk_ratings['ratings'] == id1]
    if id1 in list(dsk_ratings['ratings']):
        print("id exists")
        print(dsk_ratings)
        while (1):
            id2 = input("enter one of the primary keys from above to delete ")
            if id2 in list(dsk_ratings['id']):
                break
        dsk_ratings = pd.read_csv(path+"\\data\\rsecondary.csv")
        i = dsk_ratings.query('ratings == @id1 & id == @id2').index
        print(id1, id2)
        dsk_ratings = dsk_ratings.drop(i)
        dsk_ratings.to_csv(path+"\\data\\rsecondary.csv", index=False)
        dpk_ratings = pd.read_csv(path+"\\data\\rprimary.csv")
        id3 = id2.split('|')
        id3 = [int(i) for i in id3]
        i = dpk_ratings.query('userId == @id3[0] & movieId == @id3[1]').index
        dpk_ratings = dpk_ratings.drop(i)
        dpk_ratings.to_csv(path+"\\data\\rprimary.csv", index=False)
        df_ratings = pd.read_csv(path+"\\data\\ratings.csv")
        i = df_ratings.query('userId == @id3[0] & movieId == @id3[1]').index
        df_ratings = df_ratings.drop(i)
        df_ratings.to_csv(path+"\\data\\ratings.csv", index=False)
    else:
        print("Record does not exist")

def udelete():
    id1 = input("Enter id to delete")
    dsk_user = pd.read_csv(path+"\\data\\usecondary.csv")
    dsk_user = dsk_user.loc[dsk_user['name'] == id1]
    if id1 in list(dsk_user['name']):
        print("Id exists")
        print(dsk_user)
        while(1):
            id2 = input("enter one of the primary keys from above to delete")
            if int(id2) in list(dsk_user['userId']):
                break
        dsk_user = pd.read_csv(path+"\\data\\usecondary.csv")
        i=dsk_user.query('name == @id1 & userId == @id2').index
        dsk_user = dsk_user.drop(i)
        dsk_user.to_csv(path+"\\data\\usecondary.csv", index=False)
        dpk_user = pd.read_csv(path+"\\data\\pk.csv")
        i = dpk_user.query('userId == @id2').index
        dpk_user = dpk_user.drop(i)
        dpk_user.to_csv(path+"\\data\\uprimary.csv", index=False)
        df_user = pd.read_csv(path+"\\data\\user.csv")
        i = df_user.query('id == @id2').index
        df_user = df_user.drop(i)
        df_user.to_csv(path+"\\data\\user.csv", index=False)
        print("Record deleted")
    else:
        print("Record does not exist")
