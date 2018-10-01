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


# region DB_CONTEXT
CONN = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=asdasd")
CONN.set_client_encoding('utf8')
CUR = CONN.cursor()
# endregion

# region GLOBALS
FEED_URL_START = 'https://feedly.com/i/subscription/feed/'
CNN_RSS_URL = 'http://rss.cnn.com/rss/edition_technology'
CNN_PAGEDOWN_NUMBER = 3
CHROME_DRIVER_PATH = 'chromedriver.exe'
RESET_NEWS_LINKS = 0
RESET_ARTICLES = 0
RESET_CORPUS = 1
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
    for i in read_csv_data('stopwords.csv'):
        STOP_WORDS.append(i)
# endregion

# region SCRAPING
def rss_feed_iteration(site_rss_url,browser):
    # region VARIABLES
    selector_commercial_close_button = 'button.SeoSignupModal__close-button'
    number_of_pagedowns = CNN_PAGEDOWN_NUMBER
    # endregion

    # region LOAD_PURE_PAGE

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
    # endregion

    # region ITERATION_ONLY
    while number_of_pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        number_of_pagedowns-=1
    # endregion

    # region SCRAPE
    list_of_urls = []
    post_elems = browser.find_elements_by_class_name("title")
    for post in post_elems:
        list_of_urls.append(post.get_attribute('href'))
    # endregion

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
        CUR.execute('INSERT INTO '+NEWS_LINKS_TABLE_NAME+' VALUES ( %(url)s  )', {"url": url})
    except:
        CONN.rollback()
    else:
        CONN.commit()

def upload_article(article):
    article = article.replace('\n','')
    try:
        CUR.execute('INSERT INTO '+ARTICLES_TABLE_NAME+' (article) VALUES ( %(article)s  )', {"article": article})
    except:
        CONN.rollback()
    else:
        CONN.commit()

def upload_corpus(cleaned_text):
    try:
        CUR.execute('INSERT INTO '+CORPUS_TABLE_NAME+' (data) VALUES ( %(text)s  )', {"text": cleaned_text})
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
# endregion

# region CLEANING
def remove_wrong_chars_from_text(text):
    new_text = ''
    i = 0
    while i<len(text):
        ch = ord(text[i])
        #it only keeps a-z;A-z; ;' characters in the text
        if ( ((ch>=65) & (ch<=90)) | ((ch>=97)&(ch<=122)) | (ch == 32) | (ch == 39)):
            new_text = new_text + text[i]
        else:
            new_text = new_text + ' '
        i+=1
    return ' '.join(new_text.split())

def clean_text(text):
    plain_text = remove_wrong_chars_from_text(text)
    plain_text = plain_text.lower()
    word_list = []
    for word in plain_text.split():
        if(len(word)>=2):
            if(STOP_WORDS.count(word)==0):
                word_list.append(word)

    plain_text = ' '.join(word_list)
    return plain_text
# endregion

# region ACTIONS
def load_news_urls():
    browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    if RESET_NEWS_LINKS == 1:
        remove_table_rows(NEWS_LINKS_TABLE_NAME)

    for feed_url in load_rss_links():
        for link in rss_feed_iteration(feed_url,browser):
            upload_news_link(link)
        time.sleep(3)

def load_articles():
    if RESET_ARTICLES == 1:
        remove_table_rows(ARTICLES_TABLE_NAME)

    CUR.execute("""SELECT url from """+NEWS_LINKS_TABLE_NAME)
    rows = CUR.fetchall()

    for link in rows:
        time.sleep(2)
        article = get_article_from_page(link[0])
        upload_article(article)

def clean_articles():
    if RESET_CORPUS == 1:
        remove_table_rows(CORPUS_TABLE_NAME)

    CUR.execute("""SELECT article from """ + ARTICLES_TABLE_NAME)
    rows = CUR.fetchall()

    for text in rows:
        upload_corpus(clean_text(text[0]))
# endregion

def main():
    #load_news_urls()
    #load_articles()
    #clean_articles()



main()
