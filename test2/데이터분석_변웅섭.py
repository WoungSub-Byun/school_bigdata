import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
fm.get_fontconfig_fonts()
font_location = '/Users/woung/Downloads/kakao_fonts/KakaoBold.ttf'
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

font0 = {
    'family': 'font_name',
    'color': 'purple',
    'weight': 'bold',
    'size': 16
}
y = [456, 492, 578, 599, 670, 854]
x = ['7월', '8월', '9월', '10월', '11월', '12월']
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()


import seaborn as sns
colors = sns.color_palette('Set3', 6)

bars = plt.bar(range(len(x)), y, color=colors)
for i, b in enumerate(bars):
    ax.text(b.get_x() + b.get_width() * (1/2), b.get_height() * (1/2), y[i], ha='center', fontdict=font0)
plt.title('new Applyer', fontsize=25)
plt.ylabel('Applyer nums', fontsize=15)
plt.xlabel('month', fontsize=15)
plt.xticks(range(len(x)), x, fontsize=15, color='green')
plt.show()

# 2-2
import pandas as pd

countries = pd.read_csv('Data/countries.csv', encoding='cp949', index_col=0)
countries['population'].plot(kind='bar', color='blue')
plt.legend()
plt.show()
