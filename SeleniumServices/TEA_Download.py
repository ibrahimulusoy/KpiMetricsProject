from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rptsvr1.tea.texas.gov/perfreport/account/2019/download.html")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(2)
#WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "body > div > div.container.pt-5.flex-grow-1.flex-shrink-0.d-flex.flex-column > div.row.mt-auto.text-center.text-sm-left > div > p > a")
driver.find_element_by_css_selector("input[type='submit'][value='Continue']").click()
time.sleep(2)
driver.find_element_by_name("selall").click()
time.sleep(2)
driver.find_element_by_css_selector("input[type='submit'][value='Download']").click()




