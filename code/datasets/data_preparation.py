import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the original train_raw.csv
train_raw = pd.read_csv(os.path.join(BASE_DIR, "../../data/train_raw.csv"))
# Select the required columns
train_data = train_raw[['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age', 'Fare']].copy()

# Processing missing values
train_data['Age'] = train_data['Age'].fillna(train_data['Age'].median())
train_data['Fare'] = train_data['Fare'].fillna(train_data['Fare'].median())

# Save the cleaned file
train_data.to_csv(os.path.join(BASE_DIR, "../../data/train.csv"), index=False)

