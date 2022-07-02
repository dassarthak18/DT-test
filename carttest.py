import graphviz
import numpy as np
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz

data = read_csv("test.csv")
data.drop_duplicates(inplace=True)
X = []
temp = data[f'Input'].tolist()
X.append(temp)
Y = data['Output'].tolist()

X_encoded = np.array(X)
Y_encoded = np.array(Y)
print(len(Y))

X1_encoded = []
n = len(X_encoded[0])
for i in range(n):
  arr = []
  for j in range(len(X_encoded)):
    arr.append(X_encoded[j][i])
  X1_encoded.append(arr)
X_train, X_test, Y_train, Y_test = train_test_split(X1_encoded, Y_encoded, test_size=0.2, random_state=42)
Tree = DecisionTreeClassifier(criterion='entropy')
Tree.fit(X_train, Y_train)

data = export_graphviz(Tree,filled=True,impurity=False)
graph = graphviz.Source(data, format="png")
graph.render(filename='results/cart')