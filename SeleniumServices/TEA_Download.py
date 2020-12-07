from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
prefs = {'download.default_directory': 'C:\Downloads'}
options.add_experimental_option('prefs', prefs)
driver=webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

#Donload district rates
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
time.sleep(50)
#Donload district rates

#Donload district rates
driver.get("https://rptsvr1.tea.texas.gov/perfreport/account/2019/download.html")
time.sleep(2)
driver.find_element_by_css_selector("input[type='radio'][value='C']").click()
#WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "body > div > div.container.pt-5.flex-grow-1.flex-shrink-0.d-flex.flex-column > div.row.mt-auto.text-center.text-sm-left > div > p > a")
driver.find_element_by_css_selector("input[type='submit'][value='Continue']").click()
time.sleep(2)
driver.find_element_by_name("selall").click()
time.sleep(2)
driver.find_element_by_css_selector("input[type='submit'][value='Download']").click()
time.sleep(100)
driver.quit()



