#!F:/Python/python

import sqlite3

conn = sqlite3.connect('mirage.db')

print ("Opened database successfully");

conn.execute('''CREATE TABLE IF NOT EXISTS USER
      (EMAIL           TEXT PRIMARY KEY     NOT NULL,
       PASSWORD        TEXT NOT NULL ,              
       NAME            TEXT  NOT NULL,
       LAST            TEXT NOT NULL,
       AGE             INT     ,
       COLLEGE         TEXT    ,
       CONTACT         NUMERIC ,
       BRANCH          TEXT );''');
print ("Table user created successfully");

conn.execute('''CREATE TABLE IF NOT EXISTS LOGIN
      (EMAIL           TEXT PRIMARY KEY     NOT NULL,
       PASSWORD TEXT  );''');
print ("Table login created successfully");

conn.execute('''CREATE TABLE IF NOT EXISTS STAT
      (EMAIL           TEXT PRIMARY KEY     NOT NULL,
       html_text int, 
       ebook int,
       games int,
       oc int,
       video int,
       slides int,
       anim int );''');
print ("Table stat created successfully");

conn.execute('''CREATE TABLE IF NOT EXISTS GEN_STAT
      (html_text int, 
       ebook int,
       games int,
       oc int,
       video int,
       slides int,
       anim int );''');
conn.execute("INSERT INTO GEN_STAT (html_text,ebook,games,oc,video,slides,anim) values(0,0,0,0,0,0,0)")

print ("Table gen_stat created successfully");

conn.commit()
conn.close()
