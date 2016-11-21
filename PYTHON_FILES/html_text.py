#!F:/Python/python
import sqlite3
import cgi, cgitb 

form = cgi.FieldStorage()

conn = sqlite3.connect('mirage.db')
name=str(form.getvalue('sendtopy'))

conn.execute("INSERT INTO DATA (EMAIL,MODE)VALUES ("+"'"+name+"','html_text')")
conn.commit()
conn.close()
print ("Location:http://localhost:81/mirageproto _ Algo Discuss.html\r\n") 
