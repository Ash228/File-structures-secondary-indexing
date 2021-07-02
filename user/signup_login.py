import csv
from itertools import zip_longest
import pandas as pd
import hashlib
import pathlib

path = str(pathlib.Path().absolute())

def index():
    Offset_address = []
    Primary_key = []
    csv_columns = ["id", "offset"]
    fi = open(path+"\\user.csv", "r", encoding='utf-8')
    pos = fi.tell()
    line = fi.readline()
    pos = fi.tell()
    line = fi.readline()
    while line:
        #if line[0]=='\n':
            #break
        a = line.split(",")
        #print(a)
        #print(pos, ",", a[0])
        Offset_address.append(pos)
        Primary_key.append(a[0])
        pos = fi.tell()
        line = fi.readline()
    list = [ Primary_key, Offset_address]
    export_data = zip_longest(*list, fillvalue='')
    with open(path+"\\pk.csv", 'w', encoding="ISO-8859-1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("id", "offset"))
        wr.writerows(export_data)
    myfile.close()

def secindex():
    name = []
    Primary_key = []
    csv_columns = ["name", "id"]
    fi = open(path+"\\user.csv", "r", encoding='utf-8')
    pos = fi.tell()
    line = fi.readline()
    #print("Sec")
    pos = fi.tell()
    line = fi.readline()
    while line:
        #pos = fi.tell()
        #line = fi.readline()
        #if line[0] == '\n':
            #break
        line = line.rstrip()
        a = line.split(",")
        #print(a)
        #print(pos, ",", a[1])
        name.append(a[1])
        Primary_key.append(a[0])
        pos = fi.tell()
        line = fi.readline()
    list = [name, Primary_key]
    #print(list)
    export_data = zip_longest(*list, fillvalue='')
    with open(path+"\\sk.csv", 'w', encoding="ISO-8859-1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("name", "id"))
        wr.writerows(export_data)
    myfile.close()

def signup():
    id1 = input("enter the id1")
    index()
    secindex()
    d = pd.read_csv(path+"\\pk.csv", usecols=[0],header=None)
    #print(d)
    if id1 in d.values:
        print("id already exists")
    else:
        with open(path+"\\user.csv", "r", encoding='utf-8') as csvfile:
            name = input('enter the name :')
            dob = input('enter the dob:')
            gender = input('enter the gender:')
            password = input('enter the password:')
            password = hashlib.md5(password.encode('utf8')).hexdigest()
            with open(
                path+"\\user.cs", 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow('')
                filedname = [id1, name, dob, gender, password]
                #print(filedname)
                writer = csv.writer(csvfile, lineterminator='')
                writer.writerow(filedname)
        csvfile.close()
        index()
        secindex()
        print("Record Inserted")

def login():
    id = input("Enter user id:")
    ds = pd.read_csv(path+"\\user.csv")
    print(ds)
    ds = ds.loc[ds['id'] == int(id)]
    print(ds)
    if ds.empty:
        print("user does not exist")
    else:
        password = input('enter the password:')
        password = hashlib.md5(password.encode('utf8')).hexdigest()
        if ds.loc[int(id)-1].at['password'] == password:
            '''login placeholder '''
            print("Success")
        else:
            print("Incorrect password")



#data = pd.read_csv(r"C:\Users\ashok\Desktop\Movie fs\user.csv")
with open(path+"\\user.csv", "r") as csvfile:
    # print('successful read')
    choice = int(input('Enter the Choice 1.signup\n2.login :\n'))

    if (choice == 1):
        signup()
    elif(choice==2):
        login()