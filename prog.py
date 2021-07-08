import csv
import hashlib
import pathlib
import pandas as pd
import re
from itertools import zip_longest
from primary_index import *
from secondary_index import *
from insert import *
from delete import *
from update import *

uid = -1
path = str(pathlib.Path().absolute())

def signup():
    id1 = input("enter the id1")
    uindex()
    usecindex()
    dpk_user = pd.read_csv(path+"/data/pk.csv", usecols=[0],header=None)
    if id1 in dpk_user.values:
        print("id already exists")
    else:
        with open(path+"/data/user.csv", "r", encoding='utf-8') as csvfile:
            name = input('enter the name :')
            dob = input('enter the dob:')
            gender = input('enter the gender:')
            password = input('enter the password:')
            password = hashlib.md5(password.encode('utf8')).hexdigest()
            with open(
                path+"/data/user.cs", 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow('')
                filedname = [id1, name, dob, gender, password]
                writer = csv.writer(csvfile, lineterminator='')
                writer.writerow(filedname)
        csvfile.close()
        uindex()
        usecindex()
        print("You've been signed up\nPlease login using your credentials")

def login():
    id = input("Enter user id:")
    df_user = pd.read_csv(path+"/data/user.csv")
    print(df_user)
    df_user = df_user.loc[df_user['userId'] == int(id)]
    print(df_user)
    if df_user.empty:
        print("user does not exist")
    else:
        password = input('enter the password:')
        password = hashlib.md5(password.encode('utf8')).hexdigest()
        if df_user.loc[int(id)-1].at['password'] == password:
            uid = id
            print("Success")
            logged()
        else:
            print("Incorrect password")

def admin():
    id = int(input("Enter admin id:"))
    password = input("Enter admin password:")
    if id == 1234 and password == 'abcd':
        while(1):
            inp = int(input("Please choose the aspect to work on\n1.Movie\n2.Users\n3.Exit\n"))
            if inp == -1:
                break
            elif inp == 1:
                inp = int(input("What would you like to do\n1.Insert Movie record\n2.Modify Existing Movie Record\n3.Delete Existing Movie Record\n4.Back\n"))
                if inp == 1:
                    minsert()
                elif inp == 2 :
                    mupdate()
                elif inp == 3 :
                    mdelete()
                elif inp == 4 :
                    continue
                else:
                    print("Invalid")
            elif inp == 2:
                inp = int(input("What would you like to do\n1.Insert User record\n2.Modify Existing User Record\n3.Delete Existing User Record\n4.Back\n"))
                if inp == 1:
                    uinsert()
                elif inp == 2 :
                    uupdate()
                elif inp == 3 :
                    udelete()
                elif inp == 4 :
                    continue
                else:
                    print("Invalid")
            elif inp == 3:
                break


def logged():
    #placeholder to recommendation
    exec(compile(open('recommendationtop.py', "rb").read(), 'recommendationtop.py', 'exec'))
    #placeholder to display movies
    movid = -1
    while(1):
        inp = int(input("Please pick a movie(-1 to logout):"))
        if inp == -1:
            uid = -1
            break
        #placeholder for search
        #will set id on select
        #Display selected movie details
        #connect to rfilter
        #recommendation based on ratings
        #connect to rinsert when user enters a rating
        #and reset movie id on exit
        inp1 = input("Enter genre you would like to see:")
        df_movies = pd.read_csv(path + "/movies/movies.csv")
        df_movies = df_movies[df_movies['genre'].str.contains(inp1,re.IGNORECASE)]
        print(df_movies)
        inp = int(input("Would you like to sort these results?\n1.Ascending\n2.Descending\n3.Popularity\n4.No\nEnter choice:\n"))#another option popularity
        if inp == 1:
            sorted = df_movies.sort_values('title', ascending=True)
            print(sorted)
        elif inp == 2:
            sorted = df_movies.sort_values('title', ascending=False)
            print(sorted)
        elif inp == 3:
            #exec(compile(open('recommendationgenre.py', "rb").read(), 'recommendationgenre.py', 'exec'))
            import recommendationgenre
            recommendationgenre.build_chart(inp1) 
        elif inp == 4:
            pass
        # will set id on select
        # Display selected movie details
        # connect to rfilter
        # connect to rinsert when user enters a rating
        # and reset movie id on exit

while(uid == -1):
    inp = int(input("Would you like to :\n1.Login\n2.Signup\n3.Login(Admin)\n4.Exit\n"))
    if inp == 1:
        login()
    elif inp == 2:
        signup()
    elif inp == 3:
        admin()
    elif inp == 4:
        print("Finished")
        break
    else:
        print('invalid input')




