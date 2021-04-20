import csv
from bs4 import BeautifulSoup
from selenium import webdriver

query_txt = '코로나'
f_name = 'data/코로나.csv'

path = '/Users/woung/Downloads/chromedriver'

driver = webdriver.Chrome(path)
driver.get('https://www.naver.com')
driver.maximize_window()

element = driver.find_element_by_id("query")
element.send_keys(query_txt)
element.submit()

driver.find_element_by_link_text("뉴스").click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

content_list = soup.find('ul', 'list_news').find_all('li', 'bx')
title = []
content = []

for i in content_list:
    try:
        t = i.find('a', 'news_tit').get_text()
        title.append(t)
        c = i.find('a', 'api_txt_lines dsc_txt_wrap')
        content.append(c
    except:
        pass

f = open(f_name, 'w', encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(("번호", "제목", "내용"))

for i, j in zip(title, content):
    idx = title.index(i) + 1
    csv_writer.writerow((idx, i, j))
f.close()