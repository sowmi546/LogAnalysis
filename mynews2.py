import psycopg2
DBNAME = "news"
db = psycopg2.connect("dbname='news'")
c=db.cursor()
query1="create view secondview as select articles.author,count(*) as views from articles join log on log.path LIKE CONCAT('%',articles.slug,'%') GROUP BY articles.author;"
query="select name,views from authors join secondview on authors.id = secondview.author ORDER BY views desc;"
c.execute(query)
posts =c.fetchall()
db.close()
print(posts)
