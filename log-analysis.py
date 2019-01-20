import psycopg2

def connect_db():
    """ Connect to the news database """
    return psycopg2.connect("dbname=news")

def get_top_three_articles():
    db = connect_db()
    cur = db.cursor()
    cur.execute('SELECT * from top_three_articles')
    articles = cur.fetchall()
    cur.close()
    db.close()

    return articles

def show_top_three_articles():
    articles = get_top_three_articles()
    text = [ '\nTop three articles of all time are:\n' ]
    article_no = 1

    for article in articles:
        text.append('{}. {} - {} views'.format(article_no, article[0], str(article[1])))
        article_no += 1

    print('\n'.join(text))

def get_most_popular_authors():
    db = connect_db()
    cur = db.cursor()
    cur.execute('SELECT * from most_popular_authors')
    authors = cur.fetchall()
    cur.close()
    db.close()

    return authors

def show_most_popular_authors():
    authors = get_most_popular_authors()
    text = [ '\nThe most popular article authors of all time are:\n' ]
    author_no = 1

    for author in authors:
        text.append('{}. {} - {} views'.format(author_no, author[0], str(author[1])))
        author_no += 1

    print('\n'.join(text))

def main():
    show_top_three_articles()
    show_most_popular_authors()

main()