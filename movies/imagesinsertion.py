import csv
from itertools import zip_longest
import pandas as pd
import hashlib
import pathlib
import re
from IPython.core.display import HTML

path = str(pathlib.Path().absolute())

df_movies = pd.read_csv(path+"\\mov.csv")
country = [
'https://www.countries-ofthe-world.com/flags-normal/flag-of-United-States-of-America.png'
]
df_movies['Country'] = country
def path_to_image_html(path):
    return '<img src="'+ path + '" width="60" >'
df_movies.to_html(escape=False, formatters=dict(Country=path_to_image_html))
HTML(df_movies.to_html(escape=False,formatters=dict(Country=path_to_image_html)))
print(df_movies)