# LogAnalysis
## Purpose:
The purpose of the project is to gain hands on experience with dealing with large databases and running complex queries to retrieve the required information


First we need to bring the virtual machine back online (with **vagrant up**), and log into it with **vagrant ssh** command

Download the data file and put it in vagrant directory (newsdata.sql)

To load the data, use the command psql -d news -f newsdata.sql

So the database is created with name **news**

We can explore the tables in it \dt and to see the details of a particular table run the command \d tablename

The three tables in it are  **articles**,**authors** and **logs**

We will now need to create a python file (say mynews.sql) and connect to the above database in it

In the python file we need to write the sql queries for the three mentioned in the project that would fetch the results accordingly.

To run the program, navigate to the folder containing the python file (mynews.py) and we need to run the command
python mynews.py

But before running the file, we need to create a couple of views to perform the necessary actions for queries 2 and 3.
Here are the views :

### Creating Views:
#### For Question 2 :

query1 = "create view secondview as select articles.author,count(*) as views from articles join log on log.path = CONCAT('/article/',articles.slug) GROUP BY articles.author;"


#### For Question 3:

query1 = "create view q1 as select date(time), count(status) as total from log where status like '%4%' group by date(time);"
query2 = "create view q2 as select date(time), count(status) as total from log group by date(time);"
query3 = "create view calc2 as select (q1.total*100.0/q2.total) as val,q1.date as mydate from q1 join q2 on q1.date=q2.date;"

Once the views are created run the following command

python mynews.py which would execute the three commands 

