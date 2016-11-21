#!F:/Python/python
import sqlite3
import cgi, cgitb 

 
form = cgi.FieldStorage() 

fnm=str(form.getvalue('name'))
lnm=str(form.getvalue('last'))
eml = str(form.getvalue('email'))
pwd  = str(form.getvalue('password'))

conn = sqlite3.connect('mirage.db')

conn.execute("INSERT INTO LOGIN (EMAIL,PASSWORD)VALUES ("+"'"+eml+"','"+pwd+"')")
conn.execute("INSERT INTO STAT (EMAIL,html_text,ebook,games,oc,video,slides,anim) values("+"'"+eml+"',0,0,0,0,0,0,0)")
conn.execute("INSERT INTO USER (EMAIL,PASSWORD,NAME,LAST,AGE,COLLEGE,CONTACT,BRANCH)VALUES ("+"'"+eml+"','"+pwd+"','"+fnm+"','"+lnm+"',null,null,null,null)")
conn.commit()
cursor = conn.execute("SELECT name,last from USER where email="+"'"+eml+"'")

for row in cursor:
   Name= row[0]
   Last_name= row[1]

conn.close()
print ("Content-type:text/html\n\n")
print ("<html>")
print ("<head>")
print ("<title>Signup Successful</title>")
print ("</head>")
print ("<body>")
print ("<h2>Hello %s %s .Signup Successful, go back and login</h2>" % (Name, Last_name))
print ("</body>")
print ("</html>")

