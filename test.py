import numpy as np

num_1 = np.arange(1, 31)
print(num_1)

print(num_1[::-1])

print(num_1.sum())
print(num_1.mean())
print(np.median(num_1))

num_2 = num_1 + 5
result = np.corrcoef([num_1, num_2])
print(result)

num_1= num_1.reshape(6, 5)
print(num_1)

import matplotlib
import matplotlib.font_manager as fm
fm.get_fontconfig_fonts()



import matplotlib.pyplot as plt

x = [x for x in range(7,13)]
y = [456,492,578,599,670,854]

plt.plot(x,y,marker = 'o',color = 'orange')
plt.xlabel('month')
plt.ylabel('user')
plt.title('신규사용자')
plt.show()




import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('data/weather.csv',encoding='cp949')
monthly = [0 for x in range(12)]
monthly_wind = [0 for x in range(12)]

weather['month'] = pd.DatetimeIndex(weather['일시']).month

means = weather.groupby('month').mean()
print(means.head())
month = [str(i+1)+'월' for i in range(12)]

plt.title('평균기온',fontsize =25)
plt.plot(means['평균기온(°C)'],'blue',marker='o')
plt.xticks(range(len(month)),month)

font0 = {
    'family':'font_name',
    'color':'purple',
    'weight':'normal',
    'size':16
}

for i in range(1,13):
    plt.text(i,means['평균기온(°C)'][i],round(means['평균기온(°C)'][i],2),fontdict=font0)

plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# read_csv
countries_df['population'].plot(kind='bar', color=('b', 'darkorange', 'g', 'r', 'm'))
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

weather_df['평균 풍속(m/s)'].plot(kind='hist', bins=33, color='yellowgreen')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv()

monthly = [ 0 for _ in range(12)]
monthly_wind = [ 0 for _ in range(12)]

weather['month'] = pd.DatetimeIndex(weather['일시']).month
for i in range(12):
    monthly[i] = weather[weather['month'] == i+1]
    monthly_wind = monthly[i]