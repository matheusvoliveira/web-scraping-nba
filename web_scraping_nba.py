import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

import json

url = 'https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1'

#esse Options é um import do selenium que automatiza as coisas, nesse caso abre o navegador e acessa o site
option = Options()
option.headless = True
driver = webdriver.Edge()

driver.get(url)
time.sleep(5)

element = driver.find_element(By.XPATH,
    '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/thead/tr/th[9]')
element.click()
# //div[@class='Crom_container__C45Ti crom-container'//table//thead//tr//th[@data-field='PTS']

