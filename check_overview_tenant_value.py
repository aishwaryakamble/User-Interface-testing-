from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",chrome_options=options)
driver.get("https://15.206.126.82/login.php")

#######################################################################################
try:
	username = driver.find_element_by_id('username')
	username.click()
	username.send_keys('admin')

	password = driver.find_element_by_id('password')
	password.click()
	password.send_keys('Admin@123')

	login = driver.find_element_by_name('submitData')
	login.click()

#######################################################################################
	check = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div/div/div[2]/div/div/div[1]/div/div/div[2]').text
	check = str(check)
	check = list(check.split('\n'))
	overview_value = check[1]
	print overview_value

	driver.find_element_by_xpath('//*[@id="sidebarnav"]/li[2]/a/i').click()
	driver.find_element_by_xpath('//*[@id="viewtenant"]').click()
	output = driver.find_element_by_xpath('//*[@id="tenant_table"]/tbody/tr[1]/td[4]').text
	output = str(output)
	print output

	if overview_value == output:
		print "Router's value matches with Tenant's inventory value"
	else:
		print "Router's value  does not match with Tenant's inventory value"	
#######################################################################################
except Exception as e:
	print e

driver.close()

#######################################################################################
#//*[@id="main-wrapper"]/div/div/div[2]/div/div/div[1]/div/div/div[2]
#//*[@id="tenant_table"]/tbody/tr[1]/td[4]
#//*[@id="main-wrapper"]/div/div/div[2]/div/div/div[2]/div/div/div[2]
#//*[@id="tenant_table"]/tbody/tr[2]/td[4]
