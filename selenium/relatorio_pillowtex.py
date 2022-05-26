from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("headless")
# options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("http://localhost:8000/login")

campo_email = driver.find_element(By.NAME, "email")
campo_email.send_keys("rodrigosillos@gmail.com")

campo_senha = driver.find_element(By.NAME, "password")
campo_senha.send_keys("123mudar")

botao_entrar = driver.find_element(By.XPATH, '//button[text()="Entrar"]')
botao_entrar.send_keys(Keys.RETURN)

driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//a[text()="Faturamento"]'))
driver.find_element(By.ID, "frmFaturamento").submit()
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "invoicecheck"))
driver.find_element(By.ID, "frmExcelFaturamento").submit()

driver.close()
