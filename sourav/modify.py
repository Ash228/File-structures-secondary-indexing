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

def modify():
    id1 = int(input("Enter id to modify"))
    ds = pd.read_csv(r"/Users/souravnarayan/Desktop/FS mini/sk3.csv")
    print(ds)
    #i = d.iloc[d['name'] == id1]
    #print(i)
    ds = ds.loc[ds['ratings'] == id1]
    print(list(ds['ratings']))
    if id1 in list(ds['ratings']):
        print("Id exists")
        print(ds)
        #id2 = ''
        while(1):
            id2 = input("enter one of the primary keys from above to modify")
            print(list(ds['id']))
            if id2 in list(ds['id']):
                print(list(ds['id']))
                break
        ds = pd.read_csv(r"/Users/souravnarayan/Desktop/FS mini/sk3.csv")
        #i = d.iloc[d['name']==id1 & d['id']==int(id2)]
        isk =ds.query('ratings == @id1 & id == @id2').index
        #print("i sk" + str(i))
        #ds.to_csv(r"C:\Users\ashok\Desktop\Movie fs\sk.csv", index=False)
        dp = pd.read_csv(r"/Users/souravnarayan/Desktop/FS mini/pk3.csv")
        #i = d.index[d['id'] == id2]
        id3=id2.split('|')
        id3 = [int(i) for i in id3]
        i = dp.query('userId == @id3[0] & movieId == @id3[1]').index
        print(id3)
        #ipk = dp.query('id == @id2').index
        #print("i pk"+str(i))
        #id2 = d.get_value(i, 'offset')
        #id2 = d['offset']
        #print(list(d['id']))
        '''imp = open('pk3.csv', 'rb')
        out = open('pk3.csv', 'wb')
        writer = csv.writer(out)
        for row in csv.reader(imp):
            if row == id1:
                continue
            writer.writerow(row)
        imp.close()
        out.close()'''
        #d = d.drop(i)
        print(dp)
        #dp.to_csv(r"C:\Users\ashok\Desktop\Movie fs\pk.csv", index=False)
        du = pd.read_csv(r"/Users/souravnarayan/Desktop/FS mini/ratings.csv")
        iu = du.query('userId == @id3[0] & movieId == @id3[1]').index
        print("i user" + str(iu))
        #index()
        #secindex()
        movieId = input('enter the movieId :')
        ratings = input('enter ratings:')
        reviews = input('enter the review:')
        du.loc[iu,['movieId', 'ratings', 'reviews']] =[movieId, ratings, reviews]
        print(du)
        #id2 = d['offset']
        #d = d.drop(i)
        #print(d)
        du.to_csv(r"/Users/souravnarayan/Desktop/FS mini/ratings.csv", index=False)
        index()
        secindex()
        #print(list(d['id']))
        '''imp = open('ratings'.csv', 'rb')
        out = open('ratings.csv', 'wb')
        writer = csv.writer(out)
        for row in csv.reader(imp):
            if row == id1:
                continue
            writer.writerow(row)
        imp.close()
        out.close()
        #print(d)
        #d.loc[d['userId'] == id1]
        #id2 = d['offset']
        #print(id2)
        #new_df = d[~d.id.isin(id1)]
        #new_df.to_csv('pk.csv', index=False, sep=',')'''
    else:
        print("Record does not exist")

with open(r"/Users/souravnarayan/Desktop/FS mini/ratings.csv", "r") as csvfile:
    # print('successful read')
    choice = int(input('Enter the Choice 1.modify :\n'))

    if (choice == 1):
        modify()