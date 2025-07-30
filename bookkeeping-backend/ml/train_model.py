import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load labeled training data
data = pd.read_csv('ml/transaction_training_data.csv')  # your labeled data CSV

descriptions = data['description'].astype(str)
categories = data['category'].astype(str)

# Vectorize descriptions
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(descriptions)

# Train classifier
clf = LogisticRegression(max_iter=1000)
clf.fit(X, categories)

# Save vectorizer and model
with open('ml/model.pkl', 'wb') as f:
    pickle.dump((vectorizer, clf), f)

print("Training complete, model saved at ml/model.pkl")
