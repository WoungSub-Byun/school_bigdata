import re

txt = 'abc@facebook.com와 bbc@google.com에서 이메일이 도착하였습니다.'

output = re.findall( '\S+@[a-z.]+' , txt)
for text in output:
    text_split = text.split('@')
    print('추출된 아이디: {}, 이메일 도메인: {}'.format(text_split[0], text_split[-1]))

import matplotlib.pyplot as plt

x = [x for x in range(-10, 10)]
y1 = [2*t for t in x]
y2 = [t**2 for t in x]
y3 = [-t**2 -5 for t in x]

plt.plot
