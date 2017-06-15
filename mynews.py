import psycopg2
DBNAME = "news"
db = psycopg2.connect("dbname='news'")
c=db.cursor()
query = "select articles.title,count(*) as views from articles join log on log.path LIKE CONCAT('%',articles.slug,'%') GROUP BY articles.title ORDER BY views desc LIMIT 3;"
c.execute(query)
posts =c.fetchall()
db.close()
print(posts)
