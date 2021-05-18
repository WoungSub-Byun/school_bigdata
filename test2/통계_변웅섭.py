import numpy as np
# 1-1
players = [[190, 76.4],
           [185, 86.2],
           [181, 78.5],
           [190, 88.5],
           [186, 70.1]]
players_np = np.array(players)
print('less 80kg')
print(players_np[players_np[:,1] <= 80.0])
print('less 180cm')
print(players_np[players_np[:,0] <= 180.0])


# 1-2
num_1 = np.arange(1, 51)
print(num_1)
num_2 = num_1 + 5
print(num_2.mean())
print(np.median(num_2))

result = np.corrcoef([num_1, num_2])
print(result)
n_arr = num_2.reshape(5, 10)
print(n_arr)


# 1-3
import pandas as pd


weather = pd.read_csv('Data/weather.csv', encoding='cp949')
print('평균 분석 ----------------')
res_mean = pd.DataFrame([['평균기온(°C)', weather['평균기온(°C)'].mean()],
              ['최대 풍속(m/s)', weather['최대 풍속(m/s)'].mean()],
              ['평균 풍속(m/s)', weather['평균 풍속(m/s)'].mean()]], )
print(res_mean)
print('최소값 분석 ----------------')
res_min = pd.DataFrame([['평균기온(°C)', weather['평균기온(°C)'].min()],
              ['최대 풍속(m/s)', weather['최대 풍속(m/s)'].min()],
              ['평균 풍속(m/s)', weather['평균 풍속(m/s)'].min()]])
print(res_min)
