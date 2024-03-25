import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.get("https://www.atvrom.ro/")

time.sleep(2)

driver.find_element(By.ID, "cookiescript_accept").click()


time.sleep(2)


category = driver.find_element(By.LINK_TEXT, "FII ORANGE")
category.click()

time.sleep(2)


ktm_890 = driver.find_element(By.LINK_TEXT, "KTM 890 ADVENTURE '21")
driver.execute_script("arguments[0].scrollIntoView();", ktm_890)
for _ in range(2):
    try:
        ktm_890.click()
        break
    except:
        time.sleep(1)

driver.implicitly_wait(10)

compare = driver.find_element(By.CLASS_NAME, "compare-checkbox")
compare.click()

time.sleep(2)

driver.back()

ktm_1290 = driver.find_element(By.LINK_TEXT, "KTM 1290 SUPER ADVENTURE R '23")
driver.execute_script("arguments[0].scrollIntoView();", ktm_1290)

for _ in range(2):
    try:
        ktm_1290.click()
        break
    except:
        time.sleep(1)
