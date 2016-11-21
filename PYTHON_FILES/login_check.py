#!F:/Python/python
import sqlite3
import cgi, cgitb 
from http import cookies
import os;



form = cgi.FieldStorage()

conn = sqlite3.connect('mirage.db')
cur= conn.cursor()

userName= form.getvalue('email')
userPW= form.getvalue('password')
userPWDatabase = conn.execute("SELECT email,password FROM login WHERE email=? and password=?",[userName,userPW])
cur.fetchone()
for result in userPWDatabase:
    userDb= result[0]
    pwDb= result[1]
    if userDb == userName and pwDb == userPW:
        print ("Location:http://localhost:81/mirageproto.html\r\n") 
   
    else:
        print ("Content-type: text/html\n\n") 
        print ("<HTML><HEAD><TITLE>INVALID</TITLE></HEAD>\n" )
        print ("<BODY><H3>Please go back and enter a valid login.</H3>")
        print ("</BODY></HTML>")
conn.close()
