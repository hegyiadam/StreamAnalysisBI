import load_vectors as loader
from sklearn.ensemble import RandomForestClassifier
import keras

wordvectors = loader.load('vectors.csv')

vectors = []
for v in wordvectors:
    vectors.append(v["vector"])
words = []
for w in wordvectors:
    words.append(w["word"])

vector = []
for v in wordvectors:
    if v["word"] == 'trump':
        vector = v["vector"]
        break

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=200))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(train_vecs_w2v, y_train, epochs=9, batch_size=32, verbose=2)














# matrix =  csr_matrix(vectors)
# searched = csr_matrix(vector)
#
#
#
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# from sklearn.model_selection import train_test_split
#
# target = [1 if i < 12500 else 0 for i in range(25000)]
#
# X_train, X_val, y_train, y_val = train_test_split(
#     matrix, target, train_size=0.75
# )
#
# for c in [0.01, 0.05, 0.25, 0.5, 1]:
#     lr = LogisticRegression(C=c)
#     lr.fit(X_train, y_train)
#     print("Accuracy for C=%s: %s"
#           % (c, accuracy_score(y_val, lr.predict(X_val))))
#
#
#
#
# final_model = LogisticRegression(C=0.05)
# final_model.fit(matrix, target)
# print ("Final Accuracy: %s"
#        % accuracy_score(target, final_model.predict(searched)))
#
# feature_to_coef = {
#     word: coef for word, coef in zip(
#         words, final_model.coef_[0]
#     )
# }
# for best_positive in sorted(
#     feature_to_coef.items(),
#     key=lambda x: x[1],
#     reverse=True)[:5]:
#     print (best_positive)