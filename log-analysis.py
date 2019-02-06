#!/usr/bin/env python2.7

import psycopg2


def connect_db():
    """ Connect to the news database """
    try:
        db = psycopg2.connect("dbname=news")
        return db
    except psycopg2.DatabaseError, e:
        print('Could not connect to news database.')
        return None


def query_view(view):
    db = connect_db()

    if db is not None:
        cur = db.cursor()
        cur.execute('select * from {}'.format(view))
        results = cur.fetchall()
        cur.close()
        db.close()

        return results


def show_top_three_articles():
    articles = query_view('top_three_articles')
    text = ['\nTop three articles of all time are:\n']
    article_no = 1

    if articles is not None:
        for article in articles:
            article_info = '{}. {} - {} views'.format(
                article_no, article[0], str(article[1]))
            text.append(article_info)
            article_no += 1

        print('\n'.join(text))


def show_most_popular_authors():
    authors = query_view('most_popular_authors')
    text = ['\nThe most popular article authors of all time are:\n']
    author_no = 1

    if authors is not None:
        for author in authors:
            author_formatted = '{}. {} - {} views'.format(
                author_no, author[0], str(author[1]))
            text.append(author_formatted)
            author_no += 1

        print('\n'.join(text))


def show_dates_with_many_errors():
    dates = query_view('more_than_one_percent_errors')
    text = ['\nOn following dates more than 1% of requests lead to errors:\n']

    if dates is not None:
        for date in dates:
            formated_date = date[0].strftime('%B %d, %Y')
            text.append('{} - {}% errors'.format(formated_date, str(date[1])))

        print('\n'.join(text))


def main():
    show_top_three_articles()
    show_most_popular_authors()
    show_dates_with_many_errors()
    print('\n')


if __name__ == '__main__':
    main()
