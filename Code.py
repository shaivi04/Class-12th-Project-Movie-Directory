import pickle
from os import remove, rename
def create():
    file=open("movie.dat",'wb')
    ans='y'
    while ans in 'Yy':
        movie_id=int(input("Enter movie ID:"))
        movie_nm=input("Enter movie name:")
        Genre=input("Enter Genre:")
        Director=input("Enter director's name:")
        Producer=input("Enter producer's name:")
        Duration=input("Enter duration of the movie:")
        Date=input("Enter release date:")
        Awards=input("Enter awards won:")
        rating=float(input("Enter rating :"))
        Tot_collection=input("Enter total box office collection:")
        Tot_parts=int(input("Enter total no of seasons/parts:"))
        Type=input("Enter type(series/movie):")
        movie_rec = [movie_id,movie_nm,Genre,Director,Producer,Duration,Date,Awards,rating,Tot_collection,Tot_parts,Type]
        
        ans=input("want to continue(Y/N):")
        pickle.dump(movie_rec,file)
    file.close()

def display():
    file=open('movie.dat','rb')
    try:
        while True:
            f=pickle.load(file)
            print(f)
    except:
        pass
    file.close()

        
def search_id():
    file=open('movie.dat','rb')
    rec=pickle.load(file)
    uid=int(input('enter movie id'))
    try:
        if rec[0]==uid:
            print(rec)
        else:
            print('no such record')
    except EOFError:
        file.close()
        
def search_nm():
    file=open('movie.dat','rb')
    unm=input('enter movie name')
    rec=pickle.load(file)
    try:
        if rec[1]==unm:
                print(rec)
        else:
            print('no such record')
    except EOFError:
        file.close()

def search_genre():
    file=open('movie.dat','rb')
    ug=input('enter moviie genre')
    rec=pickle.load(file)
    try:
        if rec[2]==ug:
            print(rec)
        else:
            print('no such record')
    except EOFError:
        file.close()

def search_dir():
    file=open('movie.dat','rb')
    ud=input('enter movie director')
    rec=pickle.load(file)
    try:
        if rec[3]==ud:
            print(rec)
        else:
            print('no such record')
    except EOFError:
        file.close()

def search_prod():
    file=open('movie.dat','rb')
    uprod=input('enter movie producer')
    rec=pickle.load(file)
    try:
        if rec[4]==uprod:
            print(rec)
        else:
            print('no such record')
    except EOFError:
        file.close()
              
    
def count_all():
    fin=open("movie.dat","rb")
    ctr=0
    try:
        while True:
            rec=pickle.load(fin)
            print(rec)
            ctr+=1
    except EOFError:
        fin.close()
        print('Total records =',ctr)

def count_dur():
    fin=open("movie.dat","rb")
    ctr=0
    udur=input("Enter duration - ")
    try:
        while True:
            rec=pickle.load(fin)
            if rec[5]==udur:
                ctr+=1
    except EOFError:
        fin.close()
        print('movies of',udur,'are',ctr)


def count_rat():
    fin=open("movie.dat","rb")
    ctr=0
    urat=input("Enter Ratings - ")
    try:
        while True:
            rec=pickle.load(fin)
            if rec[8]==urat:
                ctr+=1
    except EOFError:
        fin.close()
        print("movies with rating=",urat,ctr)

def count_gen():
    fin=open("movie.dat","rb")
    ctr=0
    ugen=input("Enter genre - ")
    try:
        while True:
            rec=pickle.load(fin)
            if rec[2]==ugen:
                ctr+=1
    except EOFError:
        fin.close()
        print('Total',ugen,'movies=',ctr)


def count_type():
    fin=open("movie.dat","rb")
    ctr=0
    utype=input("Enter type - ")
    try:
        while True:
            rec=pickle.load(fin)
            if rec[11]==utype:
                ctr+=1
    except EOFError:
        fin.close()
        print(utype,'-',ctr)





def edit_rec():
    file = open("movie.dat","rb")
    temp = open("temp.dat","wb")
    found ='n'
    n=int(input('enter record no'))
    try:
        cnt=1
        while True:
            rec= pickle.load(file)
            temprec=rec
            if cnt==n:
                temprec[0] = int(input("Enter edited id -"))
                temprec[1] = input("Enter edited name -")
                temprec[2]==input("Enter edited genre ")
                temprec[3] = input("Enter edited director -")
                temprec[4] = input("Enter edited producer -")
                temprec[5] = input("Enter edited duration -")
                temprec[6] = input("Enter edited release date -")
                temprec[7] = input("Enter edited awards -")
                temprec[8] = float(input("Enter edited rating -"))
                temprec[9] = input("Enter edited total collection -")
                temprec[10] = int(input("Enter edited total parts -"))
                temprec[11] = input("Enter edited type -")
                found='y'
                cnt+=1
                pickle.dump(temprec,temp)
    except EOFError:
        file.close()
        temp.close()
        if found == "n":
            print("No such record")
            remove('temp.dat')
        else:
            remove("movie.dat")
            rename("temp.dat","movie.dat")

def edit_id():
    file = open("movie.dat","rb")
    temp = open("temp.dat","wb")
    found = 'n'
    uid=int(input('enter movie id'))
    try:
        while True:
            rec= pickle.load(file)
            temprec=rec
            if rec[0]==uid:
                temprec[1] = input("Enter edited name -")
                temprec[2]==input("Enter edited genre ")
                temprec[3] = input("Enter edited director -")
                temprec[4] = input("Enter edited producer -")
                temprec[5] = input("Enter edited duration -")
                temprec[6] = input("Enter edited release date -")
                temprec[7] = input("Enter edited awards -")
                temprec[8] = float(input("Enter edited rating -"))
                temprec[9] = input("Enter edited total collection -")
                temprec[10] = int(input("Enter edited total parts -"))
                temprec[11] = input("Enter edited type -")
                found='y'
                pickle.dump(temprec,temp)
    except EOFError:
        file.close()
        temp.close()
        if found == "n":
            print("No such record")
            remove('temp.dat')
        else:
            remove("movies.dat")
            rename("temp.dat","movie.dat")

def edit_nm():
    file = open("movie.dat","rb")
    temp = open("temp.dat","wb")
    found = 'n'
    unm=input('enter movie name')
    try:
        while True:
            rec= pickle.load(file)
            temprec=rec
            if rec[1]==unm:
                temprec[0] = int(input("Enter edited id -"))
                temprec[2]==input("Enter edited genre ")
                temprec[3] = input("Enter edited director -")
                temprec[4] = input("Enter edited producer -")
                temprec[5] = input("Enter edited duration -")
                temprec[6] = input("Enter edited release date -")
                temprec[7] = input("Enter edited awards -")
                temprec[8] = float(input("Enter edited rating -"))
                temprec[9] = input("Enter edited total collection -")
                temprec[10] = int(input("Enter edited total parts -"))
                temprec[11] = input("Enter edited type -")
                found='y'
                pickle.dump(temprec,temp)
    except EOFError:
        file.close()
        temp.close()
        if found == "n":
            print("No such record")
            remove('temp.dat')
        else:
            remove("movies.dat")
            rename("temp.dat","movie.dat")




def insertnth():
     print("ENTER record to be inserted")
     file=open('movie.dat','rb+')

     movie_id=int(input("\nEnter movie ID:"))
     movie_nm=input("Enter movie name:")
     Genre=input("Enter Genre:")
     Director=input("Enter director's name:")
     Producer=input("Enter producer's name:")
     Duration=input("Enter duration of the movie:")
     Tot_collection=input("Enter total box office collection:")
     Tot_parts=int(input("Enter total no of seasons/parts:"))
     Type=input("Enter type(series/movie):")
     pos=int(input("enter record no to add"))
     new_rec = [movie_id,movie_nm,Genre,Director,Producer,Duration,Tot_collection,Tot_parts,Type]
     try:
          itrec=pickle.load(file)
          itrec.insert(pos-1,new_rec)
          file.seek(0)
          pickle.dump(itrec,file)
     except:
          file.close()


def insert_after():
         file=open('movie.dat','rb')
         temp=open('temp.dat','wb')
         movieid=int(input("enter movie id of record to insert after:"))
         ctr=0
         movie_id=int(input("Enter movie ID:"))
         movie_nm=input("Enter movie name:")
         Genre=input("Enter Genre:")
         Director=input("Enter director's name:")
         Producer=input("Enter producer's name:")
         Duration=input("Enter duration of the movie:")
         Date=input("Enter release data:")
         Awards=input("Enter awards won:")
         rating=float(input("Enter rating :"))
         Tot_collection=input("Enter total box office collection:")
         Tot_parts=int(input("Enter total no of seasons/parts:"))
         Type=input("Enter type(series/movie):")
         new_rec = [movie_id,movie_nm,Genre,Director,Producer,Duration,Date,Awards,rating,Tot_collection,Tot_parts,Type]
         try:
             while True:
                 itrec=pickle.load(file)
                 ctr+=1
                 if itrec[0]==movieid:
                    pickle.dump(new_rec,temp)
         except EOFError:
              file.close()
              temp.close()
         remove('movie.dat')
         rename('temp.dat','movie.dat')




def insert_before():                    #insert before movie ID
    file=open('movie.dat','rb')
    temp=open('temp.dat','wb')
    name_=int(input("enter movie id to insert this record before:"))

    movie_id=int(input("Enter movie ID:"))
    movie_nm=input("Enter movie name:")
    Genre=input("Enter Genre:")
    Director=input("Enter director's name:")
    Producer=input("Enter producer's name:")
    Duration=input("Enter duration of the movie:")
    Date=input("Enter release data:")
    Awards=input("Enter awards won:")
    rating=float(input("Enter rating :"))
    Tot_collection=input("Enter total box office collection:")
    Tot_parts=int(input("Enter total no of seasons/parts:"))
    Type=input("Enter type(series/movie):")
    new_rec = [movie_id,movie_nm,Genre,Director,Producer,Duration,Date,Awards,rating,Tot_collection,Tot_parts,Type]
    try:
        while True:
            itrec=pickle.load(file)
            if itrec[0]==name_:
                pickle.dump(new_rec,temp)
            pickle.dump(itrec,temp)
    except EOFError:
        file.close()
        temp.close()
    remove('item.dat')
    rename('temp.dat','item.dat')





def delete():
    file = open("movie.dat","rb")
    temp = open("temp.dat","wb")
    recno = int(input("enter record no:"))
    try:
        while True:
            itrec=pickle.load(file)
            ctr+=1
            if ctr==recno:
                print("record to be deleted")
                print(itrec)
            else:
                pickle.dump(itrec,temp)
    except EOFError:
        file.close()
        temp.close()
    remove('item.dat')
    rename('temp.dat','item.dat')





    
def delete_id():
    file=open("movie.dat","rb+")
    found='n'
    recid=input("enter record id to delete:")
    ctr=0
    try:
        recs=pickle.load(file)
        for i in recs:
            ctr+=1
            if i[0]==recid:
                studrecs.pop(ctr-1)
                found='y'
        if found=='y':
            file.seek(0)
            pickle.dump(recs,file)
    except:
        file.close()



def deletename():
    file=open("movie.dat","rb+")
    found='n'
    nm=input("enter record name to be deleted:")
    ctr=0
    try:
        recs=pickle.load(file)
        for i in recs:
            ctr+=1
            if i[1]==nm:
                studrecs.pop(ctr-1)
                found='y'
        if found=='y':
            file.seek(0)
            pickle.dump(recs,file)
    except:
        file.close()
    file=open("movie.dat",'rb')
    try:
        while True:
            recs=pickle.load(file)
            print(recs)
    except EOFError:
        file.close()



            
while True:
    print("\n\nMENU FOR DATA MANIPULATION")
    print("1. ICREATE FILE")
    print("2. DISPLAY ALL RECORDS")
    print("3. SEARCH  & DISPLAY")
    print("4. COUNT & DISPLAY")
    print("5. EDIT RECORD")
    print("6. INSERT RECORD")
    print("7. DELETE RECORD")
    ch= int(input("Enter your choice- "))
    if ch==1:
        create()
    elif ch==2:
        display()
    elif ch==3:
        print("\n*************************************")
        ch1 = int(input("1. SEARCH ON MOVIE ID\n2. SEARCH ON NAME\n3. SEARCH ON GENRE\n4. SEARCH ON DIRECTOR\n5. SEARCH ON PRODUCER\nENTER YOUR   CHOICE(1-5) - "))
        if ch1==1:
            search_id()
        elif ch1==2:
            search_nm()
        elif ch1==3:
            search_genre()
        elif ch1==4:
            search_dir()
        elif ch1==5:
            search_prod()
    elif ch==4:
        print("\n*************************************")
        ch1 = int(input("1. COUNT ON ALL RECORDS\n2. COUNT ON DURATION\n3. COUNT ON RATING\n4. COUNT ON GENRE\n5. COUNT ON TYPE\nENTER YOUR   CHOICE(1-5) - "))
        if ch1==1:
            count_all()
        elif ch1==2:
            count_dur()
        elif ch1==3:
            count_rat()
        elif ch1==4:
            count_gen()
        elif ch1==5:
            count_type()
        
    elif ch==5:
        print("\n*************************************")
        ch1 = int(input("1. EDIT ON RECORD NO.\n2. EDIT ON MOVIE ID\n3. EDIT ON NAME\nENTER YOUR   CHOICE(1-3) - "))
        if ch1==1:
            edit_rec()
        elif ch1==2:
            edit_id()
        elif ch1==3:
            edit_nm()
        
        
    elif ch==6:
        print("\n*************************************")
        ch1 = int(input("1. INSERT AFTER RECORD NO.\n2. INSERT AFTER MOVIE ID\n3. INSERT BEFORE MOVIE NAME\nENTER YOUR   CHOICE(1-3) - "))
        if ch1==1:
            insertnth()
        elif ch1==2:
            insert_after()
        elif ch1==3:
            insert_before()


            
    elif ch==7:
        print("\n*************************************")
        ch1 = int(input("1. DELETE ON RECORD NO.\n2. DELETE ON MOVIE ID\n3. DELETE ON MOVIE NAME\nENTER YOUR   CHOICE(1-3) - "))
        if ch1==1:
            delete()
        elif ch1==2:
            delete_id()
        elif ch1==3:
            deletename()
       
    else:
        print('wrong choice')
        
    ans=input("\n want to continue program furthers(y/n)")
    if ans in ("nN"):
        break 
