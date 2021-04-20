from konlpy.tag import *
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import numpy as np
from PIL import Image
from wordcloud import ImageColorGenerator

korea = np.array(Image.open('./Data/korea.jpeg'))
save_image = ("./Data/corona_korea.jpeg")

okt = Okt()

t1 = open('Data/코로나.csv', encoding='utf-8').read()
print('\n')
t2 = okt.nouns(t1)

t3 = []
for a in t2:
    if a == "제목":
        t3.append(a.replace('제목', '이대훈'))
    else:
        t3.append(a)

with open('Data/코로나불용어.txt', encoding='utf-8') as f:
    sword = f.read()

t4 = [word for word in t3 if word not in sword and 2 <= len(word) <= 6]

t5 = Counter(t4).most_common(50)

word = dict(t5)

wc = WordCloud(font_path='/Users/danny/Downloads/나눔손글씨 암스테르담.ttf',
                      relative_scaling=0.3, mask=korea,
                      background_color='white'
                      ).generate_from_frequencies(word)
plt.figure(figsize=(10, 10))
plt.imshow(wc)
plt.axis('off')
plt.title('corona-ejy')

plt.savefig(save_image)
plt.show()