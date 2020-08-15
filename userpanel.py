from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import (StaleElementReferenceException,ElementNotInteractableException,ElementClickInterceptedException)
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import time


wb = openpyxl.Workbook()
wb.create_sheet('testing',0)	
sheet = wb['testing']

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",chrome_options=options)
driver.get("https://15.206.126.82/login.php")


try:

	username = driver.find_element_by_id('username')
	username.click()
	username.send_keys('aishwarya')

	password = driver.find_element_by_id('password')
	password.click()
	password.send_keys('Test@123')

	login = driver.find_element_by_name('submitData').click()
	print('User Login')

	#######################################################################################
	c=25
	try:
		driver.find_element_by_xpath('//*[@id="sidebarnav"]/li[1]/a').click()
		dropdown = Select(driver.find_element_by_id('filter'))	
		time.sleep(3)
		dropdown.select_by_value('device_availability')
		time.sleep(3)
		dropdown.select_by_value('devicehealth')
		 
		print('Device dropdown')
		time.sleep(3)

	except Exception:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);",dropdown)
			
	sheet["A%d"%c].value = "Device dropdown button"	
	sheet["B%d"%c].value = "working properly"
	#######################################################################################
	c=26
	driver.find_element_by_xpath('//*[@id="sidebarnav"]/li[2]/a').click()
	time.sleep(3)

	credentials = driver.find_element_by_id('username')
	credentials.click()
	credentials.send_keys('test')
	password = driver.find_element_by_id('password')
	password.click()
	password.send_keys('Test@123')
	driver.find_element_by_id('addCredential').click()
	print('Add Credentials')

	sheet["A%d"%c].value = "Add Credentials button"	
	sheet["B%d"%c].value = "working properly"
	time.sleep(5)
	#######################################################################################	
	c=27
	driver.find_element_by_xpath('//*[@id="credential_table"]/tbody/tr[1]/td[2]/input').click()
	time.sleep(3)
	driver.find_element_by_xpath('//*[@id="deletCredential"]').click()
	time.sleep(3)
	print('Delete credentials')

	sheet["A%d"%c].value = "Delete Credentials button"	
	sheet["B%d"%c].value = "working properly"
	#######################################################################################
	c=28
	time.sleep(3)
	driver.find_element_by_xpath('//*[@id="credentialsTab"]/li[2]/a').click()
	subnet = driver.find_element_by_xpath('//*[@id="subnet"]')
	subnet.click()
	subnet.send_keys('127.0.0.1')
	netmask = driver.find_element_by_xpath('//*[@id="netmask"]')
	netmask.click()
	netmask.send_keys('24')
	time.sleep(3)
	driver.find_element_by_xpath('//*[@id="startDiscovery"]').click()
	print('Subnet Scan')

	sheet["A%d"%c].value = "Subnet Scan button"	
	sheet["B%d"%c].value = "working properly"
	#######################################################################################
	c=29
	#time.sleep(3)
	manual = driver.find_element_by_id('mgmtips')
	manual.click()
	manual.send_keys('192.168.0.33')
	time.sleep(3)
	driver.find_element_by_id('startmgmtip').click()
	time.sleep(3)
	print('Manual Scan')

	sheet["A%d"%c].value = "Manual Scan button"	
	sheet["B%d"%c].value = "working properly"

	#######################################################################################
	c=30
	try:
		driver.find_element_by_xpath('//*[@id="disctable"]').click()
		for i in range(1,4):
			driver.find_element_by_xpath('//*[@id="discovery_table"]/tbody/tr[' + str(i) + ']/td[2]/a').click()
			driver.find_element_by_xpath('//*[@id="alldevices"]').click()
			driver.find_element_by_xpath('//*[@id="addInventory"]').click()
			time.sleep(5)
		print('Add to inventory')
			
	except:
	 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	sheet["A%d"%c].value = "Add to inventory button"	
	sheet["B%d"%c].value = "working properly" 

	#######################################################################################
	c=31
	driver.find_element_by_xpath('//*[@id="sidebarnav"]/li[3]/a').click()
	driver.find_element_by_id('allcheckingchkb').click()
	print('All select options')
	sheet["A%d"%c].value = "All select button"	
	sheet["B%d"%c].value = "working properly"

	c=32
	driver.find_element_by_id('allcheckingchkb').click()
	time.sleep(3)
	driver.find_element_by_xpath('//*[@id="selectall"]').click()
	print('Select in search bar')
	sheet["A%d"%c].value = "select in search bar button"	
	sheet["B%d"%c].value = "working properly"
	time.sleep(3)
	
	#######################################################################################	
	c=33
	driver.find_element_by_name('deleteinvmon').click()
	time.sleep(3)
	print('Delete button')
	sheet["A%d"%c].value = "Delete button"	
	sheet["B%d"%c].value = "working properly"	

	#######################################################################################
	c=34
	e=-1 #this code not searching last value (on hold ,will get back at you soon)
	list1 = ['Online','192.168.0.1','Hostname','Serial no','Model no','OS version','Branch','Branch Code']
	try:
		for i in range(3,11):
			search = driver.find_element_by_xpath('//*[@id="inventory_table_wrapper"]/div[2]/div/div/div[1]/div/table/thead/tr[2]/th['+ str(i) +']/input')
			e=e+1
			#driver.execute_script("arguments[0].scrollIntoView();",search)
			search.send_keys(list1[e])
			search.send_keys(Keys.ARROW_UP)
			#print list1[e]
			time.sleep(3)
			search.clear()
			time.sleep(3)
			#driver.execute_script("arguments[0].scrollIntoView();",search) #will scroll till the elememt is found
			#driver.execute_script('scroll(3000,0);')
			#search.location_once_scrolled_into_view
	except ElementNotInteractableException as e:
		#driver.window_handles	
		#driver.execute_script("arguments[0].scrollIntoView();",search)
		#driver.execute_script("window.scrollBy(0, -150);")
		#driver.window_handles
		print e
	print('Search bar')	
	sheet["A%d"%c].value = "Search bar"	
	sheet["B%d"%c].value = "working properly"	
	#######################################################################################	
	c=35
	driver.find_element_by_xpath('//*[@id="sidebarnav"]/li[4]/a').click()
	dropdown = Select(driver.find_element_by_id('backupProfile'))
	
	#print select.select_by_index(1)
	#for x in select.selectByIndex():
		#print x

	#for j in options:
		#print j.get_attribute('value')
	
	#list1 = list(dropdown.options())
	#for i in list(dropdown.options()):
	#	print i
	print dropdown.first_selected_option.get_attribute("value")
	print 'aishwarya'

	print 'aishwarya'

#######################################################################################	
except Exception as e:
	print e	

wb.save('testing_front_end.xlsx')
driver.close() 	