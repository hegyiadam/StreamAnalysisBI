import csv
from urllib.request import urlopen
from urllib.request import Request
from time import sleep
from bs4 import BeautifulSoup
import os
import json
import glob, os
import time
from matplotlib.dviread import Encoding
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from newspaper import Article

import psycopg2
import db_connection as db_conn

# region DB_CONTEXT
CONNECTION_STRING = db_conn.get_db_connection_string("dbconnection.config")
CONN = psycopg2.connect(CONNECTION_STRING)
CONN.set_client_encoding('utf8')
CUR = CONN.cursor()
# endregion

# region GLOBALS
FEED_URL_START = 'https://feedly.com/i/subscription/feed/'
CNN_PAGEDOWN_NUMBER = 100
CHROME_DRIVER_PATH = 'chromedriver.exe'
STOP_WORDS = []
NEWS_LINKS_TABLE_NAME = 'news_links'
ARTICLES_TABLE_NAME = 'articles'
CORPUS_TABLE_NAME = 'corpus'
# endregion

# region GENERAL_LOADERS
def read_json_data(path):
    data = []
    with open(path, encoding='utf-8') as fh:
        data = json.load(fh)
    return data

def read_csv_data(path):
    data = []
    with open(path, encoding='utf-8') as fh:
        reader = csv.reader(fh)
        for i in reader:
            data.append(i[0])
    return data
# endregion

# region LOAD_RESOURCES
def load_rss_links():
    return read_json_data('rss_site_links.json')['sites']

def load_stop_words():
    global STOP_WORDS
    STOP_WORDS= read_csv_data('stopwords.csv')

# endregion

# region SCRAPING
def rss_feed_iteration(site_rss_url,browser):
    selector_commercial_close_button = 'button.SeoSignupModal__close-button'
    number_of_pagedowns = CNN_PAGEDOWN_NUMBER


    browser.get(FEED_URL_START+site_rss_url)
    time.sleep(1)
    body = browser.find_element_by_tag_name("body")
    found_element = 0
    while found_element != 1:
        try:
            browser.find_element_by_css_selector(selector_commercial_close_button).click()
        except:
            sleep(1)
        else:
            found_element = 1

    page_height = browser.execute_script("return window.pageYOffset;")
    grace_period_limit = number_of_pagedowns
    while number_of_pagedowns:
        grace_period_counter = 0
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        while((page_height == browser.execute_script("return window.pageYOffset;")) & (grace_period_counter != grace_period_limit)):
            grace_period_counter += 1
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
        if grace_period_counter == grace_period_limit:
            break
        number_of_pagedowns-=1
        page_height = browser.execute_script("return window.pageYOffset;")

    list_of_urls = []
    post_elems = browser.find_elements_by_class_name("title")
    for post in post_elems:
        list_of_urls.append(post.get_attribute('href'))

    return list_of_urls

def get_article_from_page(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text
# endregion

# region DATABASE_HANDLERS
def upload_news_link(url):
    try:
        CUR.execute('INSERT INTO '+NEWS_LINKS_TABLE_NAME+' VALUES ( %(url)s , false  )', {"url": url})
    except:
        CONN.rollback()
    else:
        CONN.commit()

def upload_article(article):
    try:
        CUR.execute("""INSERT INTO """+ARTICLES_TABLE_NAME+""" (article,used) VALUES ( '"""+article+"""',false )""")
    except:
        CONN.rollback()
    else:
        CONN.commit()

def upload_corpus(cleaned_text):
    try:
        CUR.execute('INSERT INTO '+CORPUS_TABLE_NAME+' (data, used) VALUES (  \''+cleaned_text+'\' , false  )')
    except:
        CONN.rollback()
    else:
        CONN.commit()

def set_used(table_name, id, value):
    try:
        CUR.execute('UPDATE '+table_name+' SET used = %(value)s WHERE id = %(id)s', {"value": value,"id": id})
    except:
        CONN.rollback()
    else:
        CONN.commit()


def reset_used(table_name,value):
    try:
        CUR.execute('UPDATE '+table_name+' SET used = %(value)s', {"value": value})
    except:
        CONN.rollback()
    else:
        CONN.commit()


def remove_table_rows(table_name):
    try:
        CUR.execute('DELETE FROM '+table_name)
    except:
        CONN.rollback()
    else:
        CONN.commit()

def upload_loaded_sites(feed_url):
    try:
        CUR.execute('INSERT INTO loaded_sites VALUES ( %(site)s  )', {"site": feed_url})
    except:
        CONN.rollback()
    else:
        CONN.commit()

def select_unused(table_name):
    global CUR
    try:
        CUR.execute("""SELECT * FROM """ + table_name + """ WHERE used = false""")
    except:
        CONN.rollback()
    else:
        CONN.commit()
# endregion

# region CLEANING
def remove_wrong_chars_from_text(text):
    new_text = ''
    i = 0
    while i<len(text):
        ch = ord(text[i])
        #this only keeps a-z;A-z; ;' characters in the text
        if ( ((ch>=65) & (ch<=90)) | ((ch>=97)&(ch<=122)) | (ch == 32) | (ch == 39)| (ch == 46)):
            new_text = new_text + text[i]
        else:
            new_text = new_text + ' '
        i+=1
    return ' '.join(new_text.split())

def clean_text(text):
    plain_text = remove_wrong_chars_from_text(text)
    plain_text = plain_text.lower()
    word_list = []
    print(STOP_WORDS)
    for word in plain_text.split():
        if(len(word)>=2):
            if(STOP_WORDS.count(word)==0):
                word_list.append(word)

    plain_text = ' '.join(word_list)
    return plain_text
# endregion

# region ACTIONS

def load_news_urls(reset):
    browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    if reset:
        remove_table_rows(NEWS_LINKS_TABLE_NAME)

    sites = load_rss_links()
    for feed_url in sites:
        for link in rss_feed_iteration(feed_url,browser):
            upload_news_link(link)
        time.sleep(3)
        upload_loaded_sites(feed_url)

def prepare_article(article):
    article = article.replace('\n', '')
    article = article.replace('\"', ' ')
    article = article.replace('\'', '\'\'')
    return article

def load_articles(reset):
    if reset == 1:
        remove_table_rows(ARTICLES_TABLE_NAME)
        reset_used(NEWS_LINKS_TABLE_NAME, 'false')

    select_unused(NEWS_LINKS_TABLE_NAME)
    rows = CUR.fetchall()

    for link in rows:
        time.sleep(2)
        try:
            article = get_article_from_page(link[0])
        except:
            print(link[2])
        else:
            upload_article(prepare_article(article))
            set_used(NEWS_LINKS_TABLE_NAME,link[2],'true')

def clean_articles(reset):
    if reset == 1:
        remove_table_rows(CORPUS_TABLE_NAME)
        reset_used(ARTICLES_TABLE_NAME, 'false')

    select_unused(ARTICLES_TABLE_NAME)
    rows = CUR.fetchall()

    for text in rows:
        try:
            article_text = text[1]
            cleaned_text = clean_text(article_text)
            upload_corpus(cleaned_text)
        except:
            print(text[0])
        else:
            set_used(ARTICLES_TABLE_NAME,text[0],'true')
# endregion

load_news_urls(0)
load_articles(0)
clean_articles(0)
