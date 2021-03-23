from bs4 import BeautifulSoup
from selenium import webdriver
query_text = "인공지능"

path = "./chromedriver"

driver = webdriver.Chrome(path)

driver.get("https://www.naver.com/")
driver.maximize_window()

'''
try:
    driver.find_element_by_xpath('//*[@id="search_btn"]').click()
except:
    print("didnot work")'''

element = driver.find_element_by_xpath('//*[@id="query"]')

element.send_keys(query_text)

element.send_keys("\n")

#driver.find_element_by_xpath('//*[@id="search_btn"]').click()

driver.find_element_by_link_text("뉴스").click()

full_html = driver.page_source
soup = BeautifulSoup(full_html,'html.parser')

content_list = soup.select('ul[class="list_news"] > li')

for i in content_list:
    print(i.get_text())
    print()

f_name = './data/인공지능1.txt'

f = open(f_name,'w',encoding='utf-8')


for idx, i in enumerate(content_list):
    title = i.find('a', 'news_tit').get_text()
    f.write(idx+'번')
    f.write(title+"\n")
    f.write("\n")

    contents_1 = i.find('a', 'api_txt_lines dsc_txt_wrap').get_text()
    f.write(contents_1+"\n")
    f.write("\n")

    f.write("\n")

news_list = soup.find('ul', 'list_news').find_all('li')

f.close()
