from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.linear_model import LogisticRegression 

texts = [
    "Win a free iPhone now!",
    "Your meeting is at 10am",
    "Congratulations, claim your prize",
    "Please review the report",
    "Earn money quickly online",
    "Lunch tomorrow?"
]
labels = [1,0,1,0,1,0]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)
new_messages = ["Get free Tickets to show"]
new_x = vectorizer.transform(new_messages)
prediction = model.predict(new_x)

print("Spam" if prediction == 1 else "Not spam")