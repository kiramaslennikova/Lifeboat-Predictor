import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Path to data
DATA_PATH = "data/train.csv"
MODEL_PATH = "models/titanic_model.pkl"

# Loading data
data = pd.read_csv(DATA_PATH)

# Features and target variable
X = data[['Pclass', 'Sex', 'Age', 'Fare']]
y = data['Survived']

# Encoding categorical features
le = LabelEncoder()
X['Sex'] = le.fit_transform(X['Sex'])  # male=1, female=0

# Train the model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

# Save the model
joblib.dump(clf, MODEL_PATH)

print(f"Модель RandomForest успешно обучена и сохранена в {MODEL_PATH}")
