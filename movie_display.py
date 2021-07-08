import pandas as pd
import pathlib
import base64
import io
from PIL import Image

path = str(pathlib.Path().absolute())


# Function to for formatted display
def display_single(df_movies):
    print("Movie id: ", df_movies["movieId"])
    print("Title:  ", df_movies["title"])
    print("Description:  ",df_movies["description"])
    print("Genre:  ",df_movies["genre"] + "\n")
    imgdata = base64.b64decode(df_movies['img'])
    im_file = io.BytesIO(imgdata)
    img = Image.open(im_file)
    img.show(img)


def display_df(df_movies):
    for index,row in df_movies.iterrows():
        print("Movie id: ",row["movieId"])
        '''
        imgdata = base64.b64decode(row['img'])
        im_file = io.BytesIO(imgdata) 
        img = Image.open(im_file)
        img.show(img)
    '''
        print("Title:  ",row["title"])
        print("Genre:  ",row["genre"]+"\n")
