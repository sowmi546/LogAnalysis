# LogAnalysis

Navigate to the folder containing the python file (mynews.py) and we need to run the command
python mynews.py

But before running the file, we need to create a couple of views to perform the necessary actions for queries 2 and 3.
Here are the views :

Creating Views:
For Question 2 :
query1 = "create view secondview as select articles.author,count(*) as views from articles join log on log.path = CONCAT('/article/',articles.slug) GROUP BY articles.author;"


For Question 3:
query1 = "create view q1 as select date(time), count(status) as total from log where status like '%4%' group by date(time);"
query2 = "create view q2 as select date(time), count(status) as total from log group by date(time);"
query3 = "create view calc2 as select (q1.total*100.0/q2.total) as val,q1.date as mydate from q1 join q2 on q1.date=q2.date;"

Once the views are created run the following command

python mynews.py which would execute the three commands 

