from bs4 import BeautifulSoup
from selenium import webdriver
import time

# query_txt = input('크롤링할키워드는 무엇입니까? : ')
query_txt = '코로나'
path = '/Users/woung/workspace/general/school-bigdata/chromedriver'
driver = webdriver.Chrome(path)

driver.get('https://www.naver.com')
driver.maximize_window()

element = driver.find_element_by_class_name('input_text')
element.send_keys(query_txt)

driver.find_element_by_class_name('btn_submit').click()

driver.find_element_by_link_text("뉴스").click()

full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')

content_list = soup.select('ul[class="list_news"] > li')
with open('Data/네이버_코로나.txt', 'w', encoding='UTF-8') as f:
    for i in content_list:
        title = i.find('a', 'news_tit').get_text()
        f.write(title + "\n")
        content_1 = i.find('a', 'api_txt_lines dsc_txt_wrap').get_text()
        f.write(content_1 + "\n")
        f.write("\n")

time.sleep(2)
