# .venv\Scripts\Activate.ps1
import pandas as pd

# Read csv file and create a dataframe, run standard data cleaning operations
df = pd.read_csv('/kaggle/input/datasets/sid321axn/malicious-urls-dataset/malicious_phish.csv')

print("Number of null values: ")
print(df.isnull().sum())
print()
# No code for removing empty values since there were not any

dupes = df.duplicated().sum()
print("Duplicates removed: ")
print(dupes)
print()
df = df.drop_duplicates()

# rename values in second coloumn to benign or malicious only (since training on a subset of the dataset)
df['type'] = df['type'].apply(
    lambda x: 'benign' 
    if x == 'benign' 
    else 
    'malicious'
)

# print(df.head(10)) commented this line since the links are clickable on kaggle
print("Total number of entires: ")
print(len(df))

from sklearn.model_selection import train_test_split
from sentence_transformers import SentenceTransformer

# Model
model = SentenceTransformer('BAAI/bge-small-en-v1.5')

df = df.sample(n=6000, random_state=17).reset_index(drop=True) # smaller sample size
X = model.encode(df['url'].tolist())
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=17, test_size=0.2)

from sklearn.ensemble import RandomForestClassifier

# Prepare random forest model
rf = RandomForestClassifier(class_weight='balanced')
rf.fit(X_train, y_train)

# Score model
y_prob = rf.predict_proba(X_test)[:, 1]
y_pred = (y_prob > 0.3).astype(int)
y_test_binary = (y_test == 'malicious').astype(int)

rf.score(X_test, y_test)

from sklearn.metrics import classification_report
print(classification_report(y_test_binary, y_pred)) # Good f1-score nephew! Just this once!

import os
import joblib

if not os.path.exists('url_model_1.pkl'):
    joblib.dump(rf, 'url_model_1.pkl')
    print("Model saved!")
else:
    print("Model already exists.")