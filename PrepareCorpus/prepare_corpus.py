import db_connection as db
import load_vectors as lv
import scipy.spatial as spatial
import re
import psycopg2
import sys

CONN = db.get_connection()
CUR = db.get_cursor(CONN)
VECTORS = lv.load("vectors.csv")
SEARCHED_EXPRESSION_TABLE_NAME = "searched_expression"
SELECTED_ARTICLES_TABLE_NAME = "selected_articles"
CORPUS_TABLE_NAME = "corpus"
EXPRESSION = ''
ID = -1
RAW_CORPUS = ""
WORD_LIST = []
VECTOR_LIST = []
NEIGHBORS = []
NEIGHBORS_NUM = 10
CORPUS = ""

def load_expression():
    try:
        CUR.execute("SELECT * FROM "+SEARCHED_EXPRESSION_TABLE_NAME)
    except:
        CONN.rollback()
    else:
        CONN.commit()

    rows = CUR.fetchall()
    global EXPRESSION
    global ID
    if rows != []:
        EXPRESSION = rows[0][1]
        ID = rows[0][0]

def delete_expression():
    global ID

    try:
        CUR.execute("DELETE FROM "+SEARCHED_EXPRESSION_TABLE_NAME+" WHERE id = " + str(ID) )
    except:
        CONN.rollback()
    else:

        CONN.commit()

def get_raw_corpus():
    global RAW_CORPUS
    global EXPRESSION
    try:
        CUR.execute("SELECT data FROM corpus WHERE data ILIKE %(exp)s",{"exp": "%"+EXPRESSION+"%"})
    except:
        CONN.rollback()
    else:
        CONN.commit()
    rows = CUR.fetchall()
    RAW_CORPUS = ""
    for row in rows:
        RAW_CORPUS += ' . '+row[0]

def prepare_arrays():
    global WORD_LIST
    global VECTOR_LIST
    for vector in VECTORS:
        WORD_LIST.append(vector["word"])
        VECTOR_LIST.append(vector["vector"])


def get_closest_neighbors():
    global VECTOR_LIST
    global NEIGHBORS_NUM
    global EXPRESSION
    global WORD_LIST
    vector_modified_list = VECTOR_LIST
    word_modified_list = WORD_LIST

    pos_of_expression = -1
    actual_pos = 0
    found = 0
    for word in WORD_LIST:
        actual_pos += 1
        if word == EXPRESSION:
            found = 1
            break
    if found == 0:
        return
    found_num = 0
    vector = VECTOR_LIST[actual_pos]
    while found_num != NEIGHBORS_NUM:
        found_num += 1
        tree = spatial.KDTree(vector_modified_list)
        actual_pos = tree.query(vector)[1]
        NEIGHBORS.append(WORD_LIST[actual_pos])
        del word_modified_list[actual_pos]
        del vector_modified_list[actual_pos]

def create_corpus():
    global RAW_CORPUS
    global NEIGHBORS
    global CORPUS
    global EXPRESSION
    sentences = RAW_CORPUS.split(".")
    NEIGHBORS.append(EXPRESSION)
    print(NEIGHBORS)
    for s in sentences:
        for n in NEIGHBORS:
            if(re.search(".* "+n+" .*",s)):
                if CORPUS != "":
                    CORPUS += '. '
                CORPUS += s

def upload_result():
    global CORPUS

    try:
        CUR.execute("INSERT INTO " + SELECTED_ARTICLES_TABLE_NAME + " (article) VALUES (%(corpus)s)",{"corpus": CORPUS})
    except psycopg2.Error as e:
        print(e)
        CONN.rollback()
    else:
        CONN.commit()
try:
    load_expression()
    get_raw_corpus()
    prepare_arrays()
    get_closest_neighbors()

    create_corpus()
    empty_corpus_check = CORPUS
    if empty_corpus_check .replace(' ', '') == "":
        exit(0)
    upload_result()
    delete_expression()
except:
    print(sys.exc_info()[0])