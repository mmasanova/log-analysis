create view top_three_articles as
select title, count (log.time) as num from log, articles
where path = concat('/article/', slug)
and status = '200 OK'
group by title
order by num desc
limit 3;

create view most_popular_authors as 
select name, count(log.time) as num from authors, articles, log
where author = authors.id
and path = concat('/article/', slug)
and status = '200 OK'
group by authors.name
order by num desc;

create view more_than_one_percent_errors as
select date(time) as log_date, round(count(errlog.id) * 100 /count(log.id)::decimal, 2) as perc
from log left join (select id from log where status LIKE '4%' or status LIKE '5%') as errlog
on log.id = errlog.id
group by log_date
having round(count(errlog.id) * 100 /count(log.id)::decimal, 2) > 1;