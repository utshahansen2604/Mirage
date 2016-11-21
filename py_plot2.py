import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas



conn=sqlite3.connect('mirage.db')

conn.execute("CREATE table if not exists user_stat (username varchar(30) not null ,mode varchar(20) not null);")

conn.commit()
x=[]
y=[]
data=conn.execute("Select * from user_stat;")

for i in data:
	x.append(i[0])
	y.append(i[1])
	



conn.close()


ps = pandas.Series([tuple(i) for i in x])
counts = ps.value_counts()
print (counts)

ps = pandas.Series([tuple(i) for i in y])
counts = ps.value_counts()
print (counts)



