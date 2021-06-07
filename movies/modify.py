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
    name = []
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
        b=a[-1].split("|")
        for i in b:
            genre.append(i)
            Primary_key.append(a[0])
        #print(pos, ",", a[1])
        '''
        name.append(a[1])
        Primary_key.append(a[0])
        '''
        pos = fi.tell()
        line = fi.readline()
    list = [genre, Primary_key]
    print(list)
    export_data = zip_longest(*list, fillvalue='')
    with open(r"C:\Users\Nishitha\Documents\movsecondary.csv", 'w', encoding="ISO-8859-1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("genre", "id"))
        wr.writerows(export_data)
    myfile.close()

def modify():
    id1 = input("Enter id to delete")
    ds = pd.read_csv(r"C:\Users\Nishitha\Documents\movsecondary.csv")
    print(ds)
    #i = d.iloc[d['name'] == id1]
    #print(i)
    ds = ds.loc[ds['genre'] == id1]
    print(list(ds['genre']))
    if id1 in list(ds['genre']):
        print("Id exists")
        print(ds)
        #id2 = ''
        while(1):
            id2 = input("enter one of the primary keys from above to modify")
            print(list(ds['id']))
            if int(id2) in list(ds['id']):
                print(list(ds['id']))
                break
        ds = pd.read_csv(r"C:\Users\Nishitha\Documents\movsecondary.csv")
        #i = d.iloc[d['name']==id1 & d['id']==int(id2)]
        isk =ds.query('genre == @id1 & id == @id2').index
        #print("i sk" + str(i))
        #ds.to_csv(r"C:\Users\ashok\Desktop\Movie fs\sk.csv", index=False)
        dp = pd.read_csv(r"C:\Users\Nishitha\Documents\movprimary.csv")
        #i = d.index[d['id'] == id2]
        ipk = dp.query('id == @id2').index
        #print("i pk"+str(i))
        #id2 = d.get_value(i, 'offset')
        #id2 = d['offset']
        #print(list(d['id']))
        '''imp = open('pk.csv', 'rb')
        out = open('pk.csv', 'wb')
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
        du = pd.read_csv(r"C:\Users\Nishitha\Documents\movies.csv")
        iu = du.query('id == @id2').index
        print("i movie" + str(iu))
        #index()
        #secindex()
        title = input('enter the title:')
        description = input('enter the description:')
        genre = input('enter the genre:')
        #password = input('enter the password:')
        #password = hashlib.md5(password.encode('utf8')).hexdigest()
        du.loc[iu,['title', 'description', 'genre']] =[title, description, genre]
        #id2 = d['offset']
        #d = d.drop(i)
        #print(d)
        du.to_csv(r"C:\Users\Nishitha\Documents\movies.csv", index=False)
        index()
        secindex()
        #print(list(d['id']))
        '''imp = open('user.csv', 'rb')
        out = open('user.csv', 'wb')
        writer = csv.writer(out)
        for row in csv.reader(imp):
            if row == id1:
                continue
            writer.writerow(row)
        imp.close()
        out.close()
        #print(d)
        #d.loc[d['id'] == id1]
        #id2 = d['offset']
        #print(id2)
        #new_df = d[~d.id.isin(id1)]
        #new_df.to_csv('pk.csv', index=False, sep=',')'''
    else:
        print("Record does not exist")

with open(r"C:\Users\Nishitha\Documents\movies.csv", "r") as csvfile:
    # print('successful read')
    choice = int(input('Enter the Choice 1.insert :\n'))

    if (choice == 1):
        modify()