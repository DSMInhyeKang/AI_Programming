import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


data = load_iris()
print(data['feature_names'])
print(data['data'])

print(data['target_names'])
print(data['target'])

kn = KNeighborsClassifier()

df = pd.DataFrame(data.data, columns=data.feature_names)
df['class'] = data.target
print(df)


train_input, test_input, train_target, test_target = train_test_split(data.data, data.target, random_state=42)
# train_input, test_input, train_target, test_target = train_test_split(data.data, data.target, stratify=data.target, random_state=42)


kn.fit(train_input, train_target)
print(kn.score(train_input, train_target))
print(kn.score(test_input, test_target))

print(kn.predict([[7, 2, 7, 3]]))