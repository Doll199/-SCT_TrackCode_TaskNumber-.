import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# sample dataset
data = {
    "age": [25,30,35,40,45,50],
    "buy": [0,1,1,0,1,0]
}

df = pd.DataFrame(data)

x = df[['age']]
y = df['buy']

# split data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

print("Model Train Successfully ✅")