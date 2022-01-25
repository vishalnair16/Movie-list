import sqlite3 as db
import os

#it will automatically create a db file if does not exist
conn = db.connect('movies.db')

c = conn.cursor()

#Creating Movies table
if os.path.exists('movies.db'):
    print('exist')
    pass
else:
    print('creating')
    c.execute("""CREATE TABLE MOVIES(
                Name text,
                Lead_actor text,
                Lead_actress text,
                Year_of_release datetime,
                director_name text
              )""")



#inserting Multiple data(MOVIES) into the tables using insert command

c.execute("""INSERT INTO MOVIES (Name,Lead_actor,Lead_actress,Year_of_release,director_name) VALUES('Lord of the Rings','Ian McKellen','Liv tyler','2001-03-15','Peter Jackson'),
('Titanic','Leonardo DiCaprio','Kate Winslet','1997-12-17','James Cameron'),
('Harry Potter and the Philosophers Stone','Daniel Radcliffe','Emma Watson','2001-04-12','Chris Columbus'),
('Fight Club','Brad Pitt','Helena','1999-11-11','David Fincher'),
('Troy','Brad Pitt','Diane Kruger','2004-05-14','Wolfgang Petersen'),
('Mr & Mrs Smith','Brad Pitt','Angelina Jolie','2005-06-10','Doug Liman')""")

c.execute("""SELECT * FROM MOVIES""")
n=0
movie=c.fetchall()
print("Name of the Movie | Lead Actor | Lead Actress | Year Of Release | Director")
for i in range(len(movie)):
        print("\n")
        n+=1
        print(n)
        for j in range(len(movie[i])):
            print(movie[i][j]+" | ",end=" ")
n=0

#user to input favorite actor name to show movie list and detail of the movie

a=input("\nEnter Lead actor name:")

c.execute("SELECT * FROM MOVIES WHERE Lead_actor='%s'"%a)

actor=c.fetchall()
print("Name of the Movie | Lead Actor | Lead Actress | Year Of Release | Director")
for i in range(len(actor)):
        print("\n")
        n+=1
        print(n)
        for j in range(len(actor[i])):
            print(actor[i][j]+" | ",end=" ")

#Delete the inserted Data

c.execute("DELETE FROM MOVIES")

conn.commit()

conn.close()