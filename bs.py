l = ['sky', 'sun', 'wind', 'spring']

l.insert(1, 'summer')

if 'sky' in l:
    print('yes')
else:
    print('no')

sorted(l)
l.reverse()

import os
print(os.getcwd())

from bs4 import BeautifulSoup

with open('./data/ex.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')
    print(soup.find('title'))
    print(soup.find('p'))
    print(soup.find('img'))
    print()
    print(soup.find_all('p', align='right'))
    print(soup.find_all('p')[1])
    print(soup.find_all(['p', 'img']))

    list_1 = soup.find_all('p')
    for i in list_1:
        print(i)
    for i in list_1:
        print(i.string)
        print(i.get_text())
    print(soup.find_all('p'))


with open('./data/bs.html','r',encoding='utf-8') as f:
    soup2 = BeautifulSoup(f, 'html.parser')
    print(soup2.select('.name1 > span'))
    print(soup2.select('.name1 > span.store'))

with open('./data/span.txt', 'w', encoding='utf-8') as fr:
    [fr.write(str(i)) for i in soup2.find_all('span')]

with open('./data/bs2.html','r', encoding='cp949') as f:
    soup = BeautifulSoup(f, 'html.parser')
    cnt = 0
    # find 사용
    c=soup.find('div', 'flex_grid credits search_results').find_all('img')
    print(len(c))
    # select 사용
    d = soup.select('#content > div.media_list > div:nth-of-type(3) > div > div.flex_grid.credits.search_results > div > a > img')
    print(len(d))

with open('data/2017.txt', 'w', encoding='utf-8') as f1:
    f2 = open('data/2018.txt', 'w', encoding='utf-8')
    cnt1 = 0
    cnt2 = 0
    cat_num = 0
    for i in d:
        if '2017' in i['src']:
            f1.write(str(i))
            cnt1+=1
        elif '2018' in i['src']:
            f2.write(str(i))
            cnt2+=1
    for i in d:
        if 'cat' in i['src']:
            cat_num+=1
    print("2017:{}, 2018:{}, cat:{}".format(cnt1, cnt2, cat_num))





