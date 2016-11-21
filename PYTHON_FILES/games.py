#!F:/Python/python
import sqlite3
import cgi, cgitb 

form = cgi.FieldStorage()

conn = sqlite3.connect('mirage.db')
name=str(form.getvalue('sendtopy'))

conn.execute("INSERT INTO DATA (EMAIL,MODE)VALUES ("+"'"+name+"','games')")
conn.commit()
conn.close()
print ("Location:https://codefights.com\r\n") 
