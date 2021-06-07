import csv
from itertools import zip_longest
import pandas as pd
import hashlib

def index():
    Offset_address = []
    Primary_key = []
    csv_columns = ["id", "offset"]
    fi = open(r"C:\Users\Nishitha\Documents\movies.csv", "r", encoding='utf-8')
    pos = fi.tell()
    line = fi.readline()
    pos = fi.tell()
    line = fi.readline()
    while line:
        #if line[0]=='\n':
            #break
        a = line.split(",")
        print(a)
        print(pos, ",", a[0])
        Offset_address.append(pos)
        Primary_key.append(a[0])
        pos = fi.tell()
        line = fi.readline()
    list = [ Primary_key, Offset_address]
    export_data = zip_longest(*list, fillvalue='')
    with open(r"C:\Users\Nishitha\Documents\movprimary.csv", 'w', encoding="ISO-8859-1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("id", "offset"))
        wr.writerows(export_data)
    myfile.close()

def secindex():
    genre= []
    Primary_key = []
    csv_columns = ["genre", "id"]
    fi = open(r"C:\Users\Nishitha\Documents\movies.csv", "r", encoding='utf-8')
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
        #length=len(a)
        #b=a[length-1].split("|")
        #print(b)
        #print(pos, ",", a[1])
        #genre.append(b[0])
        #Primary_key.append(a[0])
        #genre.append(b[-1])
        #Primary_key.append(a[0])
        b=a[-1].split("|")
        for i in b:
            genre.append(i)
            Primary_key.append(a[0])
        #pos = fi.tell()
        line = fi.readline()
    list = [genre, Primary_key]
    print(list)
    export_data = zip_longest(*list, fillvalue='')
    with open(r"C:\Users\Nishitha\Documents\movsecondary.csv", 'w', encoding="ISO-8859-1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("genre", "id"))
        wr.writerows(export_data)
    myfile.close()

def insert():
    id1 = input("enter the id1")
    index()
    secindex()
    d = pd.read_csv(r"C:\Users\Nishitha\Documents\movprimary.csv", usecols=[0,],header=None)
    
    if id1 in d:
        print("id already exists")
    else:
        with open(r"C:\Users\Nishitha\Documents\movies.csv", "r", encoding='utf-8') as csvfile:
            title = input('enter the title:')
            description = input('enter the description:')
            genre = input('enter the genre:')
            #password = input('enter the password:')
            #password = hashlib.md5(password.encode('utf8')).hexdigest()
            with open(
                r'C:\Users\Nishitha\Documents\movies.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow('')
                filedname = [id1,title,description,genre]
                print(filedname)
                writer = csv.writer(csvfile, lineterminator='')
                writer.writerow(filedname)
        csvfile.close()
        index()
        secindex()




#data = pd.read_csv(r"C:\Users\Nishitha\Documents\movies.csv")
with open(r"C:\Users\Nishitha\Documents\movies.csv", "r") as csvfile:
    # print('successful read')
    choice = int(input('Enter the Choice 1.insert :\n'))

    if (choice == 1):
        insert()
