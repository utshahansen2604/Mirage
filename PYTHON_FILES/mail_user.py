#!F:/Python/python
import smtplib
import string
import random
import cgi,cgitb
import sqlite3

form=cgi.FieldStorage()
eml=str(form.getvalue('email'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("coderhub.dbs@gmail.com", "meghna.achintya")
pwd=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
msg = "Your Password has been reset to " + pwd
server.sendmail("coderhub.dbs@gmail.com", eml, msg)
server.quit()

con=sqlite3.connect('mirage.db')
con.execute("UPDATE USER SET PASSWORD='"+pwd+"' WHERE EMAIL='"+eml+"';")
con.execute("UPDATE LOGIN SET PASSWORD='"+pwd+"' WHERE EMAIL='"+eml+"';")
con.commit()
con.close()

print ("Location:http://localhost:81/index.html\r\n")


