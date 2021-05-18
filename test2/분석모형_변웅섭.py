import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
import pandas as pd
# 3-2-1
fm.get_fontconfig_fonts()
font_location = '/Users/woung/Downloads/kakao_fonts/KakaoBold.ttf'
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

font0 = {
    'family': 'font_name',
    'color': 'red',
    'weight': 'normal',
    'size': 13
}

months = ['1', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', '10m', '11m', '12m']


weather = pd.read_csv('Data/weather.csv', encoding='cp949')
weather['month'] = pd.DatetimeIndex(weather['일시']).month

result = weather.groupby('month').min()
res = result['평균기온(°C)']
plt.plot(res, 'blue', marker='o')
plt.title("Lowest temperature mean by month", fontsize=15)
plt.xticks(range(len(months)), months)
print(result)

for i in range(1, len(result)):
    plt.text(i, res[i], round(res[i], 2), fontdict=font0)

plt.show()
data = pd.DataFrame(columns=['name', 'hp', 'weight', 'efficiency'],
                    data=[['Aa', 230, 1.9, 16.3],
                           ['Bb', 250, 2.6, 10.2],
                           ['Cc', 190, 2.2, 11.1],
                            ['Hh', 300, 2.9, 7.1 ],
                            ['Tt', 210, 2.4, 12.1],
                            ['Kk', 220, 2.3, 13.2],
                            ['Ww', 270, 2.2, 14.2]])
print(data)
#3-2-2
data['performance'] = data['hp'] * data['efficiency']
print(data[data['performance'] == min(data['performance'])])
