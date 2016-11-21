import sqlite3



conn=sqlite3.connect('mirage.db')

conn.execute("CREATE table if not exists user_stat (username varchar(30) not null ,mode varchar(20) not null);")

conn.commit()

conn.execute("INSERT into user_stat(username,mode) values (\"aditya\",\"games\");")
conn.commit()

conn.execute("INSERT into user_stat(username,mode) values (\"aditya\",\"html_text\");")
conn.commit()

conn.execute("INSERT into user_stat(username,mode) values (\"pratik\",\"video\");")
conn.commit()

x=[]
y=[]
data=conn.execute("Select * from user_stat;")

for i in data:
	print(i)
	x.append(i[0])
	y.append(i[1])
'''
p1 = plt.bar(ind, x, width, color='r', yerr=menStd)
p2 = plt.bar(ind, y, width, color='y',
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Mode Score')
plt.title('Login user statistics')
plt.xticks(ind + width/2., ('Text','Video','Html_text','Games'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0])
	)

plt.show()


'''

conn.close()		
