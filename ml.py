# k-NN: 분류

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# supervised learning: 지도 학습
# train_data와 target_data vlfdy
# Iris features
iris = load_iris()

print('iris의 keys \n{}'.format(iris.keys()))

# Size of Data
print(type(iris.data))
print('size of iris data\n{}'.format(iris['data'].shape))
print(iris.data[:3, :])

print('feature_names')
print(iris.feature_names)

print('iris target data')
print('iris target names \n{}'.format(iris.target_names))
print('0 = setosa, 1=versicolor, 2=virginica')

print('iris의 target의 크기 \n{}'.format(iris.target.shape))
print(type(iris.target))
print(iris.target[:5])

#DESCR
print('iris DESCR \n{}'.format(iris['DESCR']))


iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(iris_df.head())

iris_df2 = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                        columns=iris['feature_names'] + ['target'])
print(iris_df2.head())

X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'])

print("X_train의 크기 : {}".format(X_train))
print("X_test의 크기 : {}".format(X_test))
print("y_train의 크기 : {}".format(y_train))
print("y_test의 크기 : {}".format(y_test))

print('picture 2')
sns.pairplot(iris_df2,
             diag_kind='kde',
             hue='target',
             palette='colorblind')
plt.show()

# K-NN Algorithm

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

num_neigh = 1
knn = KNeighborsClassifier(n_neighbors= num_neigh)
knn.fit(X_train, y_train)

print('테스트 데이터를 이용하여 예측')
y_pred = knn.predict(X_test)

scores = metrics.accuracy_score(y_test, y_pred)

print('n_neighbors가 {0:d}일때 정확도: {1:.3f}'.format(num_neigh, scores))

for i in range(1, 11):
    num_neigh = i
    knn = KNeighborsClassifier(n_neighbors=num_neigh)
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)
    scores = metrics.accuracy_score(y_test, y_pred)

    print('n_neighbors가 {0:d}일때 정확도: {1:.3f}'.format(num_neigh, scores))

print('iris의 target names \n{}'.format(iris.target_names))
print('0 = setosa, 1=versicolor, 2=virginica')

print('새로운 데이터 1')
X_new = [[5,2,9,1,0,2]]

prediction = knn.predict(X_new)
print("예측한 target의 이름: {}".format(iris['target_names'][prediction]))


iris = load_iris()
num_neigh = 5

knn = KNeighborsClassifier(n_neighbors=num_neigh)
knn.fit(iris.data, iris.target)

y_pred_all = knn.predict(iris.data)
scores = metrics.accuracy_score(iris.target, y_pred_all)
print('n_neighbors가 {0:d}일때 정확도: {1:.3f}'.format(num_neigh, scores))

from sklearn.metrics import confusion_matrix

conf_mat = confusion_matrix(iris.target, y_pred_all)
print(conf_mat)
plt.matshow(conf_mat)
plt.show()

dachshund_length = [77, 78, 85, 83, 73, 77, 73, 80]
