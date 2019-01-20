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
    text = [ "\nTop three articles of all time are:\n" ]
    article_no = 1

    for article in articles:
        text.append('{}. {} - {} views'.format(article_no, article[0], str(article[1])))
        article_no += 1

    print('\n'.join(text))

def main():
    show_top_three_articles()

main()