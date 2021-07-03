def minsert():
    id1 = input("enter the id")
    mindex()
    msecindex()
    dpk_movies = pd.read_csv(path + "\\data\\movprimary.csv", usecols=[0, ], header=None)

    if id1 in dpk_movies:
        print("id already exists")
    else:
        with open(path + "\\data\\movies.csv", "r", encoding='utf-8') as csvfile:
            title = input('enter the title:')
            description = input('enter the description:')
            genre = input('enter the genre:')
            with open(path + '\\data\\movies.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow('')
                filedname = [id1, title, description, genre]
                print(filedname)
                writer = csv.writer(csvfile, lineterminator='')
                writer.writerow(filedname)
        csvfile.close()
        mindex()
        msecindex()

def rinsert():
    id1 = input("enter the id1 ")
    rindex()
    rsecindex()
    dpk_ratings = pd.read_csv(path+"/data/rprimary.csv", usecols=[0,],header=None)
    if id1 in dpk_ratings:
        print("id already exists")
    else:
        with open(path+"/data/ratings.csv", "r", encoding='utf-8') as csvfile:
            movieid = input('enter the movieId: ')
            ratings = input('give ratings: ')
            reviews = input('enter review: ')
            with open(
                path+'/data/ratings.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow('')
                filedname = [id1, movieid, ratings, reviews]
                print(filedname)
                writer = csv.writer(csvfile, lineterminator ='')
                writer.writerow(filedname)
        csvfile.close()
        rindex()
        rsecindex()

def uinsert():
    id1 = input("enter the id1")
    uindex()
    usecindex()
    dpk_user = pd.read_csv(path+"\\data\\uprimary.csv", usecols=[0],header=None)
    if id1 in dpk_user.values:
        print("id already exists")
    else:
        with open(path+"\\data\\user.csv", "r", encoding='utf-8') as csvfile:
            name = input('enter the name :')
            dob = input('enter the dob:')
            gender = input('enter the gender:')
            password = input('enter the password:')
            password = hashlib.md5(password.encode('utf8')).hexdigest()
            with open(
                path+"\\data\\user.cs", 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow('')
                filedname = [id1, name, dob, gender, password]
                writer = csv.writer(csvfile, lineterminator='')
                writer.writerow(filedname)
        csvfile.close()
        uindex()
        usecindex()
        print("Record Inserted")