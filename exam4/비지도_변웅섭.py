import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

X = np.array(
    [
        [15, 11],
        [6, 3],
        [11, 15],
        [17, 12],
        [24, 10],
        [20, 25],
        [17, 15],
        [85, 70],
        [71, 81],
        [60, 79],
        [56, 52],
        [81, 91],
        [50, 50],
        [60, 60],
        [70, 70],
    ]
)

kmeans = KMeans(n_clusters=2).fit(X)
y = kmeans.labels_
centers = kmeans.cluster_centers_

new = np.array([[10, 10], [60, 65]])
y_pred = kmeans.predict(new)

new_data = ["(10,10)", "(60, 50)"]

plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors="orange", cmap="rainbow", s=50)
plt.scatter(
    centers[:, 0], centers[:, 1], c="yellow", edgecolors="orange", s=200, alpha=0.5
)

center = "중심"

for i in range(2):
    plt.text(centers[i, 0], centers[i, 1], center, color="purple")

plt.scatter(new[:, 0], new[:, 1], c=y_pred, s=400, alpha=0.5, cmap="rainbow")
for i in range(2):
    plt.text(new[i, 0], new[i, 1], center, color="green")

plt.title("k=3 클러스터링", fontsize=20)
plt.show()




# iris
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
X = X_test[:, 2:]


km = KMeans(n_clusters=3)
km.fit(X)

labels = km.labels_
centers = km.cluster_centers_

X1 = np.array([[6.0, 2.5], [6.3, 3.7]])
y_pred = km.predict(X1)

data = ["길이 6.0, 너비 2.5", "길이 6.3, 너비 3.7"]

plt.scatter(
    X[:, 0], X[:, 1], c=labels, cmap="gist_rainbow", edgecolors="k", s=30, label="iris"
)

plt.scatter(
    km.cluster_centers_[:, 0],
    km.cluster_centers_[:, 1],
    s=250,
    c="yellow",
    edgecolors="black",
    marker="*",
    label="centroids",
)
plt.scatter(
    X1[:, 0],
    X1[:, 1],
    c=y_pred,
    s=400,
    edgecolors="k",
    alpha=0.5,
    cmap="gist_rainbow",
    label="new data",
)

for i in range(2):
    plt.text(X1[i, 0], X1[i, 1], data[i], color="darkorange")

plt.xlabel("꽃받침의 길이", fontsize=10, c="orange")
plt.ylabel("꽃받침의 너비", fontsize=10, c="green")
plt.title("꽃받침의 길이와 너비의 클러스터링", fontsize=15, c="purple")
plt.legend(loc="upper left")
plt.show()
