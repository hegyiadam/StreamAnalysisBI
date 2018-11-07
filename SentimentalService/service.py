import sys
import database as db
import sentimental
import json


corpus_list =db.load_corpus()
result = sentimental.classify_corpus_list(corpus_list)
print(result)