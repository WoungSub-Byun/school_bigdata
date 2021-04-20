s = 'Hello world'
s.split(',')

s = 'welcome, to,  the,   python,    world'
s = [i.strip() for i in s.split(',')]

s = '010.1234.5678'
s = '-'.join(s.split('.'))
print(s)
s = '#####this is and example#####'
s = s.strip('#').capitalize()
print(s)

import string

src_str = string.ascii_uppercase
print('src_str=', src_str)
print(src_str[1:]+src_str[0])
import re
txt1 = 'Life is too short, you need python.'
txt2 = 'The best moment of my life'

print(re.search('Life', txt1))
print(re.search('Life', txt2))

txt3 = 'My Life My Choice'
print(re.search('^Life', txt2))

print(re.search('A..A','ABA'))
print(re.search('A..A','ABBA'))
print(re.search('A..A', 'ABBBA'))

print(re.search('AB*','A'))
print(re.search('AB*', 'AA'))
print(re.search('AB*', 'HOPE'))
print(re.search('AB*', 'X-MAN'))
print(re.search('AB*', 'CABBA'))
print(re.search('AB*', 'CABBBBBBA'))

print(re.search('AB?','A'))
print(re.search('AB?', 'AA'))
print(re.search('AB?', 'J-HOPE'))
print(re.search('AB?', 'X-MAN'))
print(re.search('AB?', 'CABBA'))
print(re.search('AB?', 'CABBBBBBA'))

print(re.search('AB+','A'))
print(re.search('AB+', 'AA'))
print(re.search('AB+', 'J-HOPE'))
print(re.search('AB+', 'X-MAN'))
print(re.search('AB+', 'CABBA'))
print(re.search('AB+', 'CABBBBBBA'))

txt_1 = 'My life my life my life in the sunshine'
print(re.findall('[Mm]y',txt_1))
text = """101 COM PythonProgramming
102 MAT LinearAlgebra
103 ENG ComputerEnglish
"""
print(re.findall('\d+', text))

f = open('Data/UNDHR.txt')

for line in f:
    if re.search('[(]\d+[)]', line):
        print(line)

txt = 'abc@facebook.com와 bbc@google.com에서 이메일이 도착하였습니다.'
output = re.findall('\w+@[a-z.]+', txt)
print('email:{}'.format(output))

output = re.findall('\w+@[a-z]+', txt)

for text in output:
    text_split = text.split('@')
    print('id:{} domain:{}'.format(text_split[0], text_split[1]))
asdf = '123...123..34....544'
asdf = re.sub('[.]+','.',asdf)
print('Wow',asdf)


import numpy as np
array_a = np.array([0,1,2,3,4,5,6,7,8,9])
print('array_a = ',array_a)
array_b = np.array(range(10))
print('array_b = ',array_b)

array_c = np.array(range(0,10,2))
print('array_c = ',array_c)
print('array_a의 shape:', array_a.shape)
print('array_a의 ndim:', array_a.ndim)
print('array_a의 dtype:', array_a.dtype)
print('array_a의 size:', array_a.size)
print('array_a의 itemsize:', array_a.itemsize)

y = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(y)

np_y = np.array(y)

print(np_y[0])
print(np_y[0:2,2:4])
print(np_y[1, 1:3])

print(np_y[::2, ::2])
print(np_y[::2][::2])

players = [[170, 76.4],
           [183, 86.2],
           [181, 78.5],
           [176, 90.1]]
np_players = np.array(players)
print('몸무게가 80이상인 선수정보')
print(np_players[np_players[:,1] >= 80])

x = [ i for i in range(10)]
y = [ i ** 2 for i in range(10)]
z = [ i for i in range(10, 0, -1)]

result = np.corrcoef( [x,y,z] )
print(result)

num_arr = np.arange(1,21)
print(num_arr)

print(num_arr[::-1])
print(num_arr.sum())
print(num_arr.mean())
print(np.median(num_arr))

num_arr = num_arr.reshape(5, 4)
print(num_arr)

x1 = [ i for i in range(10)]
x2 = [ np.random.randint(1, 10) for i in range(10)]
x3 = [ -i for i in range(10)]
x4 = [ i**2 for i in range(10)]

print(np.corrcoef([x1, x2, x3, x4]))
# x1과 상관관계가 가장 높은 리스트는 x4이다.
# x1과 가장 상관관계가 낮은 리스트는 x3이다.
