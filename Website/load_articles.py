
import psycopg2
# region DB_CONTEXT
CONN = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=asdasd")
CONN.set_client_encoding('utf8')
CUR = CONN.cursor()
CORPUS_TABLE_NAME = 'selected_articles'
# endregion

def load_corpus():
    CUR.execute("""SELECT article FROM """ + CORPUS_TABLE_NAME)
    rows = CUR.fetchall()
    articles = []
    i = 0
    for corpus in rows:
        articles.append(corpus[0])
    return articles
