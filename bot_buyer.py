from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://mercadolivre.com.br/'
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.52 Safari/537.36"

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument(f'user-agent={user_agent}')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


browser = webdriver.Chrome(options=options)

browser.get(url)

ac = ActionChains(browser)

# Aceita os cookies
print('Aceitando os cookies')
browser.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/button[1]').click()
# Passa o mouse sobre categorias
print('Interagindo com o menu Categorias')
cat = browser.find_element(By.XPATH, '/html/body/header/div/div[2]/ul/li[2]/a')
ac.move_to_element(cat).perform()
# Passa o mouse sobre a categoria tecnologia
print('Interagindo com a sub categoria Tecnologia')
tech_cat = browser.find_element(By.XPATH, '/html/body/header/div/div[2]/ul/li[2]/div/ul/li[2]/a')
ac.move_to_element(tech_cat).perform()
# Clica na categoria de Celulares e Telefones
print('Interagindo com a sub categoria Celulares e Telefones')
browser.find_element(By.XPATH, '/html/body/header/div/div[2]/ul/li[2]/div/div/div/div/div[1]/h2/a').click()
# Clica na marca Apple
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.find_element(By.XPATH, '/html/body/main/div/div[3]/div/section/div[2]/div/div[2]/a/div/div/div[1]/img').click()
# Scroll up na listagem de modelos
total_height = int(browser.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    browser.execute_script(f'window.scrollTo(0, {i});')
# Clicando no modelo desejado
browser.find_element(By.XPATH, '/html/body/main/div/div[2]/section/ol/li[11]/div/div/div[2]/div[1]/a').click()
