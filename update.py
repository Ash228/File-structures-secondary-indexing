def mupdate():
    id1 = input("Enter genre to modify ")
    dsk_movies = pd.read_csv(path+"\\data\\\movsecondary.csv")
    dsk_movies = dsk_movies.loc[dsk_movies['genre'] == id1]
    if id1 in list(dsk_movies['genre']):
        print("Id exists")
        print(dsk_movies)
        while(1):
            id2 = input("enter one of the primary keys from above to modify ")
            if int(id2) in list(dsk_movies['id']):
                break
        dsk_movies = pd.read_csv(path+"\\data\\\movsecondary.csv")
        isk =dsk_movies.query('genre == @id1 & id == @id2').index
        dpk_movies = pd.read_csv(path+"\\data\\\movprimary.csv")
        ipk = dpk_movies.query('id == @id2').index
        df_movies = pd.read_csv(path+"\\data\\\movies.csv")
        iu = df_movies.query('id == @id2').index
        title = input('enter the title:')
        description = input('enter the description:')
        genre = input('enter the genre:')
        df_movies.loc[iu,['title', 'description', 'genre']] =[title, description, genre]
        df_movies.to_csv(path+"\\data\\movies.csv", index=False)
        mindex()
        msecindex()
    else:
        print("Record does not exist")

def rupdate():
    id1 = int(input("Enter id to modify "))
    dsk_ratings = pd.read_csv(path+"\\data\\rsecondary.csv")
    dsk_ratings = dsk_ratings.loc[dsk_ratings['ratings'] == id1]
    if id1 in list(dsk_ratings['ratings']):
        print("Id exists")
        print(dsk_ratings)
        while(1):
            id2 = input("enter one of the primary keys from above to modify ")
            if id2 in list(dsk_ratings['id']):
                break
        dsk_ratings = pd.read_csv(path+"\\data\\rsecondary.csv")
        dpk_ratings = pd.read_csv(path+"\\data\\rprimary.csv")
        #i = d.index[d['id'] == id2]
        id3=id2.split('|')
        id3 = [int(i) for i in id3]
        df_ratings = pd.read_csv(path+"\\data\\ratings.csv")
        iu = df_ratings.query('userId == @id3[0] & movieId == @id3[1]').index
        movieId = input('enter the movieId : ')
        ratings = input('enter ratings : ')
        reviews = input('enter the review : ')
        df_ratings.loc[iu,['movieId', 'ratings', 'reviews']] =[movieId, ratings, reviews]
        df_ratings.to_csv(path+"\\data\\ratings.csv", index=False)
        rindex()
        rsecindex()
        print("Modification Successful ")
    else:
        print("Record does not exist ")

def uupdate():
    id1 = input("Enter id to delete")
    dsk_user = pd.read_csv(path+"\\data\\usecondary.csv")
    dsk_user = dsk_user.loc[dsk_user['name'] == id1]
    if id1 in list(dsk_user['name']):
        print("Id exists")
        while(1):
            id2 = input("enter one of the primary keys from above to modify")
            print(list(dsk_user['userId']))
            if int(id2) in list(dsk_user['userId']):
                print(list(dsk_user['userId']))
                break
        dsk_user = pd.read_csv(path+"\\data\\usecondary.csv")
        isk =dsk_user.query('name == @id1 & id == @id2').index
        dpk_user = pd.read_csv(path+"\\data\\uprimary.csv")
        ipk = dpk_user.query('id == @id2').index
        df_user = pd.read_csv(path+"\\data\\user.csv")
        iu = df_user.query('id == @id2').index
        name = input('enter the name :')
        dob = input('enter the dob:')
        gender = input('enter the gender:')
        password = input('enter the password:')
        password = hashlib.md5(password.encode('utf8')).hexdigest()
        df_user.loc[iu,['name', 'dob', 'gender', 'password']] =[name, dob, gender, password]
        rindex()
        rsecindex()
        df_user.to_csv(path+"\\data\\user.csv", index=False)
        print("Record modified")
    else:
        print("Record does not exist")