from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import ElementClickInterceptedException
import time


options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')


driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",chrome_options=options)   
driver.get("https://15.206.126.82/login.php")

username = driver.find_element_by_id('username')
username.click()
username.send_keys('aishwarya')

password = driver.find_element_by_id('password')
password.click()
password.send_keys('Test@123')

login = driver.find_element_by_name('submitData')
login.click()
time.sleep(3)

discovery = driver.find_element_by_xpath('//*[@id="sidebarnav"]/li[2]/a').click()
discoveries = driver.find_element_by_xpath('//*[@id="disctable"]').click()


before_XPath = '//*[@id="discovery_table"]/tbody/tr['
after_XPath = ']/td[2]/a'
try:
	for i in range(1,11):
		FinalXPath = before_XPath + str(i) + after_XPath 
		output = driver.find_element_by_xpath(FinalXPath).text
		driver.find_element_by_xpath(FinalXPath).click()
		driver.find_element_by_xpath('//*[@id="alldevices"]').click()
		driver.find_element_by_xpath('//*[@id="addInventory"]').click()
		print output
		time.sleep(5)

except ElementClickInterceptedException:
 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.close() 

