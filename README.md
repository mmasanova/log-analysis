# Log Analysis
This is my solution for project no 1 of Udacity Full Stack Web Developer Nanodegree.

## Description ##

This is a reporting tool which consists of a python script that runs some SQL commands against the news database.

The news database contains information about articles as well as the web server logs for the site.
The log has a database row for each time a reader loaded a web page. 
The reporting tool answers following questions about the site's user activity:

1. What are the most popular three articles of all time?

2. Who are the most popular article authors of all time?

3. On which days did more than 1% of requests lead to errors?

## Instructions ##
This project is designed to run with python version 2.7.
In order to run the tool clone the project and navigate to the project directory.

Before running the tool a few views need to be added to the database. The commands for these are:

```
create view top_three_articles as
select title, count (log.time) as num from log, articles
where path = concat('/article/', slug)
and status = '200 OK'
group by title
order by num desc
limit 3;
```


```
create view most_popular_authors as 
select name, count(log.time) as num from authors, articles, log
where author = authors.id
and path = concat('/article/', slug)
and status = '200 OK'
group by authors.name
order by num desc
```


```
create view more_than_one_percent_errors as
select date(time) as log_date, round(count(errlog.id) * 100 /count(log.id)::decimal, 2) as perc
from log left join (select id from log where status LIKE '4%' or status LIKE '5%') as errlog
on log.id = errlog.id
group by log_date
having round(count(errlog.id) * 100 /count(log.id)::decimal, 2) > 1;
```

Once all the views are ready, run the following command:

```python log-analysis.py```

