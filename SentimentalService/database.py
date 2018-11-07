
import psycopg2
import db_connection as db_connection
# region DB_CONTEXT
CONNECTION_STRING = db_connection.get_db_connection_string("dbconnection.config")
CONN = psycopg2.connect(CONNECTION_STRING)
CONN.set_client_encoding('utf8')
CUR = CONN.cursor()
CORPUS_TABLE_NAME = 'selected_articles'
# endregion

def load_corpus():
    try:
        CUR.execute("""SELECT article FROM """ + CORPUS_TABLE_NAME)
    except:
        CONN.rollback()
    rows = CUR.fetchall()
    articles = []
    for corpus in rows:
        articles.append(corpus[0])
    return articles
