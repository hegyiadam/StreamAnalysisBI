import csv

def load(filename):
    with open(filename, 'r',encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, dialect='excel')
        word_vector_list = []
        for row in spamreader:
            list = eval(row[1])
            word_vector = {"word": row[0], "vector": list}
            word_vector_list.append(word_vector)
    return word_vector_list