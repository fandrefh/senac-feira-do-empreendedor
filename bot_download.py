from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://ri.magazineluiza.com.br/'

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')

browser = webdriver.Chrome(options=options)
browser.get(url)
browser.find_element(By.XPATH, '/html/body/form/main/div[1]/div/div/div[2]/div/div/div/div/div/div/a').click()
browser.find_element(By.XPATH, '//*[@id="ContentInternal_ContentPlaceHolderConteudo_rptResultados_linkArq_Apresentacao2T_0"]/img').click()
