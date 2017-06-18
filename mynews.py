#!/usr/bin/env python
import psycopg2
from tabulate import tabulate
DBNAME = "news"
db = psycopg2.connect("dbname='news'")
c1 = db.cursor()
# c.execute("""select articles.title,count(*) as views from articles join log on
#           log.path = CONCAT('/article/',articles.slug) WHERE log.status = '200
#           OK' GROUP BY articles.title ORDER BY views desc LIMIT 3;""")
c1.execute("""select articles.title,count(*) as views from articles join log on
          log.path = CONCAT('/article/',articles.slug) WHERE log.status =
          '200 OK' GROUP BY articles.title ORDER BY views desc LIMIT 3;""")
posts1 = c1.fetchall()

c2 = db.cursor()
# query1 = "create view secondview as select articles.author,count(*) as
#          "views from articles join log on log.path LIKE CONCAT('%',articles."
#          "slug,'%') GROUP BY articles.author;"
c2.execute("""select name,views from authors join secondview on authors.id =
           secondview.author ORDER BY views desc;""")
posts2 = c2.fetchall()

c3 = db.cursor()
query = "select date(mydate),val from calc2 where val>1;"
c3.execute(query)
posts3 = c3.fetchall()

# for i in posts:
#     print '\n%s %s' %(i[0], i[1])
print("********For Query1 ********")
print("       Title                       Views")
print(tabulate(posts1))

print("********For Query2 ********")
print("    Name                  Views     ")
print(tabulate(posts2))

print("********For Query3 ********")
print("    Date  Error %")
print(tabulate(posts3))

db.close()
