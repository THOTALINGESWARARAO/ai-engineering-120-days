# GaussianNB

from sklearn.naive_bayes import GaussianNB
import numpy as np

X = np.array([
    [1.0, 2.0],
    [1.2, 1.8],
    [1.1, 2.2],
    [5.0, 6.0],
    [5.2, 5.8],
    [4.8, 6.2]
])

y = np.array([
    0, 0, 0,
    1, 1, 1
])

model = GaussianNB()
model.fit(X,y)
x_new = [[1.1,2.0]]
prediction = model.predict(x_new)
print(prediction)

probabilites = model.predict_proba(x_new)
print(probabilites)

# MultinomialNB

from sklearn.feature_extraction.text import CountVectorizer

texts = [
    "free money",
    "free offer",
    "project meeting",
    "team meeting"
]
vectorizer = CountVectorizer()
X1 = vectorizer.fit_transform(texts)
print(vectorizer.get_feature_names_out())
print(X1.toarray())

from sklearn.naive_bayes import MultinomialNB

y1 = [1,1,0,0]

model1 = MultinomialNB()

model1.fit(X1,y1)
new_text = ["free money"]

X1_new = vectorizer.transform(new_text)
prediction = model1.predict(X1_new)
print(prediction)

print(model1.predict_proba(X1_new))



#BernouliNB

from sklearn.naive_bayes import BernoulliNB

vectorizer1 = CountVectorizer(binary=True)
X2 = vectorizer1.fit_transform(texts)
print(vectorizer1.get_feature_names_out())
print(X2.toarray())

model2 = BernoulliNB()
model2.fit(X2,y1)
X2_new = vectorizer1.transform(new_text)
prediction = model2.predict(X2_new)
print(prediction)
print(model2.predict_proba(X2_new))