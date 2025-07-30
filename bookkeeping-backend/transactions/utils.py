
# CATEGORY_RULES = {
#     "uber": "Transport",
#     "lyft": "Transport",
#     "starbucks": "Meals",
#     "mcdonald": "Meals",
#     "office depot": "Office Supplies",
#     "amazon": "Office Supplies",
#     # Add more rules here
# }

# def categorize_transaction(description: str) -> str:
#     description_lower = description.lower()
#     for keyword, category in CATEGORY_RULES.items():
#         if keyword in description_lower:
#             return category
#     return "Uncategorized"
import pickle
import os

clf = None
vectorizer = None

def load_model():
    global clf, vectorizer
    if clf is None or vectorizer is None:
        model_path = os.path.join('ml', 'model.pkl')
        with open(model_path, 'rb') as f:
            vectorizer, clf = pickle.load(f)

# Automatically load when this module is imported
load_model()

def categorize_transaction(description):
    X = vectorizer.transform([description])
    category = clf.predict(X)[0]
    return category
