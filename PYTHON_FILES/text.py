#!F:/Python/python
import sqlite3
import cgi, cgitb 

form = cgi.FieldStorage()

conn = sqlite3.connect('mirage.db')
name=form.getvalue('usrname')

conn.execute('''CREATE TABLE IF NOT EXISTS DATA
      (EMAIL TEXT ,
       MODE TEXT  );''');)
conn.execute("INSERT INTO DATA (EMAIL,MODE)VALUES ("+"'"+name+"','text')")
conn.commit()
conn.close()
print ("Location:http://localhost:81/mirageproto.html\r\n") 
