from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import pickle
import os.path as osp

# SOURCE LINK
# https://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/
def word_feats(words):
    return dict([(word, True) for word in words])

def init_classifier():
    if osp.exists("classifier.pickle"):
        return (load_classifier())
    else:
        negids = movie_reviews.fileids('neg')
        posids = movie_reviews.fileids('pos')

        negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
        posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

        trainfeats = negfeats + posfeats
        classifier = NaiveBayesClassifier.train(trainfeats)
        save_classifier(classifier)
        return (classifier)


def classify_corpus(corpus = ''):
    classifier = init_classifier()

    probabilty_distance = classifier.prob_classify(word_feats(corpus))

    pos_result = round(probabilty_distance.prob("pos"), 2)
    neg_result = 1 - pos_result
    return({'pos' : pos_result, 'neg' : neg_result})

def classify_corpus_list(list = []):
    sum_pos = 0
    sum_neg = 0
    for corpus in list:
        res = classify_corpus(corpus)
        sum_pos += res['pos']
        sum_neg += res['neg']
    sum = sum_pos + sum_neg
    pos = sum_pos / sum
    neg = sum_neg / sum
    return({'pos' : pos, 'neg' : neg})

def save_classifier(classifier):
    f = open('classifier.pickle', 'wb')
    pickle.dump(classifier, f)
    f.close()

def load_classifier():
    f = open('classifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()
    return  classifier