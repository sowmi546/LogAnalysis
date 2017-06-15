import psycopg2
DBNAME = "news"
db = psycopg2.connect("dbname='news'")
c=db.cursor()
query1="create view q1 as select date(time), count(status) as total from log where status like '%4%' group by date(time);"
query2="create view q2 as select date(time), count(status) as total from log group by date(time);"
query3="create view calc2 as select (q1.total*100/q2.total) as val,q1.date as mydate from q1 join q2 on q1.date=q2.date;"
query="select date(mydate) from calc2 where val>1;"
c.execute(query)
posts =c.fetchall()
db.close()
print(posts)
