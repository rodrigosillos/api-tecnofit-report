from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://app.tecnofit.com.br/ng/login")

campo_email = driver.find_element(By.NAME, "email")
campo_email.send_keys("contato@superforcecrossfit.com")

campo_senha = driver.find_element(By.NAME, "password")
campo_senha.send_keys("Superforce380*")

botao_acessar = driver.find_element(By.XPATH, '//button[text()="Acessar"]')
botao_acessar.send_keys(Keys.RETURN)

driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//a[text()="Relatórios"]'))
driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//a[text()="Clientes por Status"]'))

driver.close()
