import sys
import load_articles as la
import sentimental

def format(res):
    return "pos="+str(res['pos'])+'&neg='+str(res['neg'])

corpus_list =la.load_corpus()
#print(corpus_list)
result = sentimental.classify_corpus_list(corpus_list)
#print(result)