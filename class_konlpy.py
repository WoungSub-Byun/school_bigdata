!pip install konlpy

from konlpy.tag import *
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc

from wordcloud import WordCloud
from collections import Counter

okt = Okt()
kkma = Kkma()


data1 = open("data/1.txt", encoding='cp949').read()
print(data1)


print("Kkma: ", kkma.nouns('나는 사과 얼룩말 사자 호랑이 과자'))
print("Okt:", okt.nouns('나는 사과 얼룩말 사자 호랑이 과자'))

!pip install -r requirements.txt

data2 = okt.nouns(data1)
print("1.추출된 키워드",data2)
print()
data3 = Counter(data2)
print("2.단어별 빈도수:",data3)


sword = open('data/2.txt', encoding='cp949').read()

data4 = [ each_word for each_word in data2 if each_word not in sword]

print(data4)

data5 = []
for i in data4:
    if len(i) >= 2 | len(i) <= 10:
        data5.append(i)
print(data5)

data6 = Counter(data5)
print(data6)

data7 = data6.most_common(10)
print(data7)

data8 = dict(data7)

print(data8)

wordcloud = WordCloud(font_path='./ㅡㅁ겨ㅠ.ttf', relative_scaling=0.5,
                      background_color="skyblue",).generate_from_frequencies(data8)
plt.figure(figsize=(8,4))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

!pip install matplotlib

!pip install matplotlib==3.1.3

data = open("data/3.txt", encoding='utf-8').read()

words = [_ for _ in okt.nouns(data)]
words = Counter(words)
words = words.most_common(30)
words = dict(words)

wordcloud = WordCloud(font_path='./MaruBuri-Regular.ttf', relative_scaling=0.5, background_color="skyblue").generate_from_frequencies(words)
plt.figure(figsize=(8,4))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

