import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

dogs_length = [
    34,
    38,
    38,
    41,
    30,
    37,
    41,
    35,
    65,
    67,
    76,
    76,
    69,
    63,
    63,
    78,
    31,
    50,
    80,
]
dogs_height = [
    22,
    25,
    19,
    30,
    21,
    24,
    28,
    18,
    50,
    50,
    50,
    48,
    50,
    50,
    45,
    51,
    40,
    52,
    70,
]

d = zip(dogs_length, dogs_height)
l = list(d)
data = [list(x) for x in l]

X = np.array(data)
km = KMeans(n_clusters=3)
km.fit(X)
y_km = km.labels_

data = ["길이 80, 높이 20", "길이 70, 높이 50"]
X1 = np.array([[80, 20], [70, 50]])
y_pred = km.predict(X1)

plt.scatter(
    X[y_km == 0, 0],
    X[y_km == 0, 1],
    s=50,
    c="lightgreen",
    marker="s",
    edgecolor="black",
    label="cluster 1",
)

plt.scatter(
    X[y_km == 1, 0],
    X[y_km == 1, 1],
    s=50,
    c="orange",
    marker="o",
    edgecolor="black",
    label="cluster 2",
)

plt.scatter(
    X[y_km == 2, 0],
    X[y_km == 2, 1],
    s=50,
    c="lightblue",
    marker="v",
    edgecolor="black",
    label="cluster 3",
)

plt.scatter(X1[:, 0], X1[:, 1], c=y_pred, cmap="rainbow", edgecolors="k", s=300)
for i in range(2):
    plt.text(X1[i, 0], X1[i, 1], data[i], color="green")
plt.grid()

plt.xlabel("강이지 길이")
plt.ylabel("강아지 높이")
plt.title("강아지 크기와 길이(클러스터링)")
plt.legend(loc="upper left")
plt.show()


# 4
X = np.array(
    [
        [150, 43],
        [160, 55],
        [164, 63],
        [165, 50],
        [170, 80],
        [175, 76],
        [180, 70],
        [150, 50],
        [180, 80],
    ]
)
km = KMeans(n_clusters=2)
km.fit(X)
y_km = km.labels_

X1 = np.array([[175, 70], [160, 50]])
y_pred = km.predict(X1)


plt.scatter(
    X[y_km == 0, 0],
    X[y_km == 0, 1],
    s=50,
    c="lightgreen",
    marker="s",
    edgecolor="black",
    label="lable 0",
)

plt.scatter(
    X[y_km == 1, 0],
    X[y_km == 1, 1],
    s=50,
    c="orange",
    marker="o",
    edgecolor="black",
    label="lable 1",
)

plt.scatter(
    X1[0, 0],
    X1[0, 1],
    s=100,
    c="purple",
    marker="o",
    edgecolors="black",
    label="new data",
)

plt.grid()
plt.xlabel("키")
plt.ylabel("몸무게")
plt.title("키와 몸무게를 이용한 클러스터링(k=2)", fontsize=20, c="purple")
plt.legend(loc="upper left")
plt.show()
