import csv 
from itertools import zip_longest
import pandas as pd
import hashlib

def index():
           Offset_address=[]
           Primary_key=[]
           movieId=[]
           csv_columns=["userId", "movieId", "offset"]
           fi=open(r"/Users/souravnarayan/Desktop/FS mini/ratings.csv","r",encoding='utf-8')
           pos=fi.tell()
           line=fi.readline()
           pos=fi.tell()
           line=fi.readline()
           pos = fi.tell()
           line = fi.readline()
           while line:
               
               a=line.split(",")
               print(a)
               print(pos,",",a[0],",",a[1])
               Offset_address.append(pos)
               Primary_key.append(a[0])
               movieId.append(a[1])
               pos=fi.tell()
               line=fi.readline()
           list= [Primary_key, movieId, Offset_address]
           export_data = zip_longest(*list, fillvalue = '')
           with open(r'/Users/souravnarayan/Desktop/FS mini/pk3.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
                wr = csv.writer(myfile)
                wr.writerow(("userId", "movieId", "offset"))
                wr.writerows(export_data)
           myfile.close()
    
def secindex():
    ratings = []
    Primary_key = []
    csv_columns = ["ratings", "id"]
    fi = open(r"/Users/souravnarayan/Desktop/FS mini/ratings.csv", "r", encoding='utf-8')
    pos = fi.tell()
    line = fi.readline()
    print("Sec")
    pos = fi.tell()
    line = fi.readline()
    while line:
        #pos = fi.tell()
        #line = fi.readline()
        #if line[0] == '\n':
            #break
        line = line.rstrip()
        a = line.split(",")
        print(a)
        #print(pos, ",", a[1])
        ratings.append(a[2])
        Primary_key.append(a[0]+'|'+a[1])
        pos = fi.tell()
        line = fi.readline()
    list = [ratings, Primary_key]
    print(list)
    export_data = zip_longest(*list, fillvalue='')
    with open(r"/Users/souravnarayan/Desktop/FS mini/sk3.csv", 'w', encoding="ISO-8859-1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("ratings", "id"))
        wr.writerows(export_data)
    myfile.close()
    
def insert():
    id1 = input("enter the id1")
    index()
    secindex()
    d = pd.read_csv(r"/Users/souravnarayan/Desktop/FS mini/pk3.csv", usecols=[0,],header=None)
    if id1 in d:
        print("id already exists")
    else:
        with open(r"/Users/souravnarayan/Desktop/FS mini/ratings.csv", "r", encoding='utf-8') as csvfile:
            movieId = input('enter the movieId: ')
            ratings = input('give ratings: ')
            reviews = input('enter review:')
            with open(
                r'/Users/souravnarayan/Desktop/FS mini/ratings.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow('')
                filedname = [id1, movieId, ratings, reviews]
                print(filedname)
                writer = csv.writer(csvfile, lineterminator ='')
                writer.writerow(filedname)
        csvfile.close()
        index()
        secindex()




#data = pd.read_csv(r"C:\Users\ashok\Desktop\Movie fs\user.csv")
with open(r"/Users/souravnarayan/Desktop/FS mini/ratings.csv", "r") as csvfile:
    # print('successful read')
    choice = int(input('Enter the Choice 1.insert :\n'))

    if (choice == 1):
        insert()


           

