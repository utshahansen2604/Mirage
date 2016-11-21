library("DBI") 
library("RSQLite")

 dbfile = "C:/Users/my/Downloads/mirage.db";

 sqlite =dbDriver("SQLite");

 mydb=dbConnect(sqlite,dbfile);


dbListTables(mydb);

res=dbSendQuery(mydb,"Select * from user_stat;")

data <- fetch(res)

t_data<-table(data)

barplot(t_data, main="User Statistics", xlab="Mode",ylab="User", col=c("darkblue","red"),  beside=TRUE)
dev.copy(jpeg,'my_plot.png')
dev.off()



  