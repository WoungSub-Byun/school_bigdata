from konlpy.tag import *
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc

from wordcloud import WordCloud
from collections import Counter

okt = Okt()
kkma = Kkma()


data1 = open("data/1.txt").read()
print(data1)


print("Kkma: ", kkma.nouns('나는 사과 얼룩말 사자 호랑이 과자'))
print("Okt:", okt.nouns('나는 사과 얼룩말 사자 호랑이 과자'))
