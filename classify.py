import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.datasets import fetch_20newsgroups


train_data = pd.read_csv('training.csv')
test_data = pd.read_csv('testData.csv')

# Build the model
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model using the training data
model.fit(train_data['Tweet'], train_data['Label'])

# Predict the categories of the test data
predicted_categories = model.predict(test_data['Tweet'])

print("The accuracy is {}".format(accuracy_score(test_data['Label'], predicted_categories)))