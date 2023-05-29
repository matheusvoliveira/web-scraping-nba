from selenium.webdriver.common.by import By
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url = 'https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1'

#esse Options é um import do selenium que automatiza as coisas, nesse caso abre o navegador e acessa o site
option = Options()
option.headless = True
driver = webdriver.Edge()

driver.get(url)
time.sleep(5)
pop_up = driver.find_element(By.XPATH,
                             "//*[@id='onetrust-accept-btn-handler']").click()

#acha a planilha contendo todas as infos dos jogadores
element = driver.find_element(By.XPATH,
                              '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]')

html_content = element.get_attribute('outerHTML')

#transforma a table html em uma lista usando panda
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

#selecione oque voce quer usar na lista
df_full = pd.read_html(str(table))[0].head(10)
df = df_full[['Player', 'Team', 'PTS']]
print(df)

# transforme os dados em um dicionario
json_data = df.to_json(orient='records')
with open('data.json', 'w') as file:
    file.write(json_data)

driver.quit()
