from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path = '/home/sillos/geckodriver')
driver.get("https://app.tecnofit.com.br/ng/login")

assert "Python" in driver.title
elem = driver.find_element_by_name("q")

elem = driver.find_element(By.XPATH, '//button[text()="Acessar"]')
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
driver.close()
