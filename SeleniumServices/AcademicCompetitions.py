import datetime
import os
import time
from selenium import webdriver
from BaseServices import Bases

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': r'{}'.format(Bases.BaseKPI.source_files_path)}
chrome_options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(r'C:\chromedriver', options=chrome_options)

browser.get('https://skyward.harmonytx.org/ws/reports/')
time.sleep(5)
txtUserName = browser.find_element_by_id('UserName')
txtUserName.send_keys('Esra.AtaKahraman')
time.sleep(2)
txtPassword = browser.find_element_by_id('Password')
txtPassword.send_keys('E1985a**')
time.sleep(2)
btnSignIn = browser.find_element_by_class_name('formContainer__submitButton')
btnSignIn.click()
time.sleep(12)
browser.get('https://skyward.harmonytx.org/ws/reports/report/107')
time.sleep(20)
btnExcel = browser.find_element_by_link_text('EXPORT TO EXCEL')
btnExcel.click()
time.sleep(20)
browser.quit()

CurrentDate = datetime.datetime.today().strftime('%d-%b-%Y')
os.rename(r'{}\Export.xlsx'.format(Bases.BaseKPI.source_files_path), r'{}\AcademicCompetitions_{}.xlsx'.format(Bases.BaseKPI.source_files_path, CurrentDate))
