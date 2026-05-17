# .venv\Scripts\Activate.ps1
import pandas as pd

# Prepare data
# Read csv file and create a dataframe, run standard data cleaning operations
df = pd.read_csv('/kaggle/input/datasets/sid321axn/malicious-urls-dataset/malicious_phish.csv')

print("Number of null values: ")
print(df.isnull().sum())

dupes = df.duplicated().sum()
print("Duplicates removed: ")
print(dupes)
df = df.drop_duplicates()

# rename values in second coloumn to benign or malicious
df['type'] = df['type'].apply(
    lambda x: 'benign' 
    if x == 'benign' 
    else 
    'malicious'
)
# print(df.head(10)) commented this line since the links are clickable on kaggle
print("Total number of entires: ")
print(df['url'].value_counts())

# prepare test/train split and embedding model since the url is a string list
from sklearn.model_selection import train_test_split
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('BAAI/bge-small-en-v1.5')

X = model.encode(df['url'].tolist()) # This will take a long time with the full data set
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=17, test_size=0.2)

# show test & train data table

# Prepare random forest model
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Score model
y_pred = rf.predict(X_test)
rf.score(X_test, y_test)

# Report
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))