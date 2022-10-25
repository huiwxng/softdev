# notes-and-code: Hui Wang, Ryan Lau, Jonathan Song
# SoftDev  
# K18 -- SQLITE3 BASICS
# 2022-10-25
# time spent:

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
with open('courses.csv') as courses:
    reader = csv.DictReader(courses)
    command = "create table courses (code text, mark int, id int)"
    c.execute(command)
    for row in reader:
        command = f"insert into courses values ('{row['code']}', {row['mark']}, {row['id']})"
        print (command)
        c.execute(command)

with open('students.csv') as students:
    reader = csv.DictReader(students)
    command = "create table students (name text, age int, id int)"
    c.execute(command)
    for row in reader:
        command = f"insert into students values ('{row['name']}', {row['age']}, {row['id']})"
        print (command)
        c.execute(command)

#==========================================================

db.commit() #save changes
db.close()  #close database


