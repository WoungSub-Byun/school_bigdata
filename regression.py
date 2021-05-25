import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()
print('diabetes의 키\n{}'.format(diabetes.keys()))

#Input data
print('Input data')
print(diabetes.data)
print('Shape of diabetes.data: {}'.format(diabetes.data.shape))

# feature 확인
print('Features of Input data')
print('data can affect for diabetes')
print(diabetes.feature_names)
print('diabetes feature names \n{}'.format(diabetes.feature_names))

#target Data
print('Target data')
print(diabetes.target)
print('target data y:', diabetes.target.shape)

# DESCR
print('diabetes DESCR \n{}'.format(diabetes['DESCR']))

# 1. 가설 세우기
# BMI가 높은 사람은 당뇨 수치가 높을 가능성이 없다.

print('10가지의 특성 중에서 체질량 지수에 해당되는 세번째 항목만 추출')
print('BMI')
bmi = diabetes.data[:, 2]
print(bmi)
print(bmi.shape)

# 가설 증명 1
tar = diabetes.target
print(tar.shape)

import seaborn as sns
import pandas as pd

df = pd.DataFrame({
    'bmi': bmi,
    'target': tar,
})

print(df.corr())
#sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")
#plt.show()

from sklearn.model_selection import train_test_split
x_train, X_test, y_train, Y_test = train_test_split(diabetes.data[:, np.newaxis, 2],
                                                    diabetes.target, test_size=0.2)
print('x_train의 크기 : {}'.format(x_train.shape))
print('x_test의 크기 : {}'.format(X_test.shape))
print('y_train의 크기 : {}'.format(y_train.shape))
print('y_test의 크기 : {}'.format(Y_test.shape))

# 학습 후 linear regression 모델생성
regr = LinearRegression()
regr.fit(x_train, y_train)
coef = regr.coef_
intercept = regr.intercept_

print('당뇨수치 =', coef, "* 체질량 지수 + ", intercept)

# 적합도 계산
print('훈련 데이터만 가지고 적합도 계산')
print('계수와 기울기 값들이 bmi가 당뇨수치를 예측하는데 얼마나 적합하는가')

score = regr.score(x_train, y_train)
print('The score of this line for the train data: ', score)

print('테스트 데이터만 가지고 적합도 계산')
score = regr.score(X_test, Y_test)
print('The score of this line for the test data: ', score)

# plot으로 표현
plt.scatter(x_train, y_train, color='green', marker='*')

y_pred = regr.predict(x_train)
plt.scatter(x_train, y_pred, color='red')

plt.plot(x_train, y_pred, color='yellow', linewidth=3)

plt.title('Linear Regression of bmi and biabetes values')
plt.show()

regr.fit(x_train, y_train)
coef = regr.coef_
intercept = regr.intercept_

y_pred = regr.predict(X_test)
plt.scatter(y_pred, Y_test, color='red')

x = np.linspace(0, 330, 100)

plt.plot(x, x, linewidth=3, color='blue')
plt.show()
