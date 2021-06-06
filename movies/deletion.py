import csv
from itertools import zip_longest
import pandas as pd
import hashlib


def delete():
    id1 = input("Enter id to delete")
    d = pd.read_csv(r"C:\Users\Nishitha\Documents\movsecondary.csv")
    print(d)
    #i = d.iloc[d['name'] == id1]
    #print(i)
    d = d.loc[d['genre'] == id1]
    print(list(d['genre']))
    if id1 in list(d['genre']):
        print("Id exists")
        print(d)
        #id2 = ''
        while(1):
            id2 = int(input("enter one of the primary keys from above to delete"))
            print(list(d['id']))
            if int(id2) in list(d['id']):
                print(list(d['id']))
                break
        d = pd.read_csv(r"C:\Users\Nishitha\Documents\movsecondary.csv")
        #i = d.iloc[d['name']==id1 & d['id']==int(id2)]
        i=d.query('genre == @id1 & id == @id2').index
        #print("i sk" + str(i))
        d = d.drop(i)
        print(d)
        d.to_csv(r"C:\Users\Nishitha\Documents\movsecondary.csv", index=False)
        d = pd.read_csv(r"C:\Users\Nishitha\Documents\movprimary.csv")
        #i = d.index[d['id'] == id2]
        i = d.query('id == @id2').index
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
        d = d.drop(i)
        print(d)
        d.to_csv(r"C:\Users\Nishitha\Documents\movprimary.csv", index=False)
        d = pd.read_csv(r"C:\Users\Nishitha\Documents\movies.csv")
        i = d.query('id == @id2').index
        print("i movie" + str(i))
        #id2 = d['offset']
        d = d.drop(i)
        print(d)
        d.to_csv(r"C:\Users\Nishitha\Documents\movies.csv", index=False)
        print(list(d['id']))
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
        delete()