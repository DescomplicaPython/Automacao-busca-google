from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time

def busca_google(consulta):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com")
    wait = WebDriverWait(driver, 10)
    barra_busca = wait.until(EC.visibility_of_element_located((By.NAME, 'q')))
    barra_busca.send_keys(consulta)
    barra_busca.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.quit()

busca_google("Automatização com Python")
