import pandas as pd

# Load the original train_raw.csv
train_raw = pd.read_csv("train_raw.csv")
# Select the required columns
train_data = train_raw[['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age', 'Fare']]

# Processing gaps
train_data['Age'] = train_data['Age'].fillna(train_data['Age'].median())
train_data['Fare'] = train_data['Fare'].fillna(train_data['Fare'].median())

train_data.to_csv("train.csv", index=False)
