from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
#from selenium.common.exceptions import * 
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
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
	username.send_keys('admin')

	password = driver.find_element_by_id('password')
	password.click()
	password.send_keys('Admin@123')

	login = driver.find_element_by_name('submitData')
	login.click()

	#######################################################################################
	c=1
	if driver.title == "Admin Overview":

		print("Admin overview")
		sheet["A%d"%c].value = "Login button"	
		sheet["B%d"%c].value = "working properly"
	else:
		print("Admin overview")
		sheet["A%d"%c].value = "Login button"	
		sheet["B%d"%c].value = "not working"

	#######################################################################################

	c= 2
	menu_button = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[1]/li/a/i')
	if menu_button:
		menu_button.click()
		print "Main Menu"
		sheet["A%d"%c].value = "Main button"	
		sheet["B%d"%c].value = "working properly"

	else:
		print("Main Menu")
		sheet["A%d"%c].value = "Main button"	
		sheet["B%d"%c].value = "not working"

	#######################################################################################
	c= 3
	overview_button = driver.find_element_by_xpath('//*[@id="sidebarnav"]/li[1]/a/i')
	if overview_button:
		overview_button.click()
		print("Overview")
		sheet["A%d"%c].value = "Overview button"	
		sheet["B%d"%c].value = "working properly"

	else:
		print("Overview")
		sheet["A%d"%c].value = "Overview button"	
		sheet["B%d"%c].value = "not working"

	#######################################################################################
	c= 4
	tenant_management_button = driver.find_element_by_xpath('//*[@id="sidebarnav"]/li[2]/a/i').click()
	if driver.title == "Tenant Management":
		print("Tenant Management")
		sheet["A%d"%c].value = "Tenant Management button"	
		sheet["B%d"%c].value = "working properly"

	else:
		print("Tenant Management")
		sheet["A%d"%c].value = "Tenant Management button"	
		sheet["B%d"%c].value = "not working"

	#######################################################################################
	c= 5

	tenant_name = driver.find_element_by_id('tenantname')
	tenant_name.click()
	tenant_name.send_keys("bandhan")

	tenant_acman = driver.find_element_by_id('tenantacman')
	tenant_acman.click()
	tenant_acman.send_keys("manager")

	tenant_contact_no = driver.find_element_by_id('tamcontno')
	tenant_contact_no.click()
	tenant_contact_no.send_keys("1234567892")

	tenant_email = driver.find_element_by_id('tamemail')
	tenant_email.click()
	tenant_email.send_keys("123@gmail.com")

	tenant_desc = driver.find_element_by_id('tenantdesc')
	tenant_desc.click()
	tenant_desc.send_keys("testing")

	tenant_created_button = driver.find_element_by_id('tenantCreate')
	tenant_created_button.click()
	print("Tenant Created")
	sheet["A%d"%c].value = "Tenant Created button"	
	sheet["B%d"%c].value = "working properly"
		
	#######################################################################################
	c=6
	view_tenant = driver.find_element_by_xpath('//*[@id="viewtenant"]/span').click()
	time.sleep(2)
	print("View Existing Tenant")
	time.sleep(3)
	sheet["A%d"%c].value = "View Existing Tenant button"	
	sheet["B%d"%c].value = "working properly"

	#######################################################################################
	c=7
	select_all = driver.find_element_by_xpath('//*[@id="selectAllTenant"]').click()
	time.sleep(3)
	driver.find_element_by_xpath('//*[@id="selectAllTenant"]').click()
	print('Tenant select all')


	sheet["A%d"%c].value = "Select all Tenant button"	
	sheet["B%d"%c].value = "working properly"
	#######################################################################################
	c=8
	for i in range(1,2):
		select_one = driver.find_element_by_xpath('//*[@id="tenant_table"]/tbody/tr[' + str(i) + ']/td[2]/input').click()
	print('Tenant select one ')	
	time.sleep(3)

	sheet["A%d"%c].value = "Select one Tenant button"	
	sheet["B%d"%c].value = "working properly"
	#######################################################################################
	c=9
	view_tenant_L1user = driver.find_element_by_xpath('//*[@id="tenant_table"]/tbody/tr[1]/td[5]/a').click()
	time.sleep(2)
	print("View Tenant L1 User")

	sheet["A%d"%c].value = "View Tenant L1 User button"	
	sheet["B%d"%c].value = "working properly"

	#######################################################################################
	c=10
	close_tenant_L1user = driver.find_element_by_xpath('//*[@id="l1UserModal"]/div/div/div[3]/button').click()
	time.sleep(2)
	print("Close Tenant L1 User")

	sheet["A%d"%c].value = "Close Tenant L1 User button"	
	sheet["B%d"%c].value = "working properly"

	#######################################################################################
	c=11
	view_tenant_L2user = driver.find_element_by_xpath('//*[@id="tenant_table"]/tbody/tr[1]/td[6]/a').click()
	time.sleep(2)
	print("View Tenant L2 User")

	sheet["A%d"%c].value = "View Tenant L2 User button"	
	sheet["B%d"%c].value = "working properly"


	#######################################################################################
	c=12
	close_tenant_L2user = driver.find_element_by_xpath('//*[@id="l2UserModal"]/div/div/div[3]/button').click()
	time.sleep(2)
	print("Close Tenant L2 User")

	sheet["A%d"%c].value = "Close Tenant L2 User button"	
	sheet["B%d"%c].value = "working properly"

	#######################################################################################
	c=13
	d = -1
	tenant = ['ban',1,0,1,1,0,1,'Tue']
	try:
		for i in range(3,11): 
			search = driver.find_element_by_xpath('//*[@id="tenant_table_wrapper"]/div[2]/div/div/div[1]/div/table/thead/tr[2]/th[' + str(i) + ']/input')
			d = d+1
			#print d
			#print tenant[d]
			#search.location_once_scrolled_into_view
			search.send_keys(tenant[d])
			time.sleep(3)
			search.clear()	
		
	except:
		driver.execute_script("return arguments[0].scrollIntoView();",search)
		#driver.implicitly_wait(5)
		
	print('All search bar')
	#//*[@id="tenant_table_wrapper"]/div[2]/div/div/div[1]/div/table/thead/tr[2]/th[3]/input
	sheet["A%d"%c].value = "All search bar"	
	sheet["B%d"%c].value = "working properly"
	#######################################################################################
	#c=11
	#select_tenant = driver.find_element_by_xpath('//*[@id="tenant_table"]/tbody/tr[1]/td[2]/input')
	#select_tenant.click()
	#time.sleep(3)
	#select_delete = driver.find_element_by_id('deleteTenants')
	#select_delete.click()

	#time.sleep(2)

	#delete = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[2]').click()
	#time.sleep(3)
	#try:
	#	final_delete = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[1]')
	#	time.sleep(2)
	#	final_delete.click()
	#	time.sleep(2)
	#except StaleElementReferenceException as e :
	#	print e

	#time.sleep(5)
	#print("Delete Tenant")

	#sheet["A%d"%c].value = "Delete Tenant button"	
	#sheet["B%d"%c].value = "working properly"

	#######################################################################################
	c = 14
	view_users = driver.find_element_by_xpath('//*[@id="sidebarnav"]/li[3]/a').click()
	time.sleep(3)
	print('User Management')

	sheet["A%d"%c].value = "User Management button"	
	sheet["B%d"%c].value = "working properly"
	#######################################################################################
	c=15
	select_all_users = driver.find_element_by_xpath('//*[@id="flowcheckall"]').click()
	print('User Management select all')
	driver.find_element_by_xpath('//*[@id="flowcheckall"]').click()
	time.sleep(3)
	#print('User Management select one')

	sheet["A%d"%c].value = "User Management select all button"	
	sheet["B%d"%c].value = "working properly"

	#######################################################################################
	c=16
	for i in range(1,2):
		select_one_user = driver.find_element_by_xpath('//*[@id="tenant_table"]/tbody/tr[' + str(i) + ']/td[2]/input').click()
		time.sleep(3)
	print('User Management select one')	

	sheet["A%d"%c].value = "User Management select one"	
	sheet["B%d"%c].value = "working properly"

	#######################################################################################
	c=17
	e = -1
	user = ['ais','test@123','L2','axis','2020-08']
	for i in range(3,8): 
		search = driver.find_element_by_xpath('//*[@id="tenant_table_wrapper"]/div[2]/div/div/div[1]/div/table/thead/tr[2]/th[' + str(i) + ']/input')
		e = e+1
		#print e
		#print user[e]
		search.send_keys(user[e])
		#time.sleep(5)
		search.clear()
		
		#//*[@id="tenant_table_wrapper"]/div[2]/div/div/div[1]/div/table/thead/tr[2]/th[3]/input
		#//*[@id="tenant_table_wrapper"]/div[2]/div/div/div[1]/div/table/thead/tr[2]/th[4]/input
	print('All search bar')

	sheet["A%d"%c].value = "All search bar"	
	sheet["B%d"%c].value = "working properly"

	#######################################################################################
	c = 18
	manage_users = driver.find_element_by_xpath('//*[@id="viewtenant"]').click()
	time.sleep(3)
	print('Manage Users')

	sheet["A%d"%c].value = "Manage Users button"	
	sheet["B%d"%c].value = "working properly"

	#######################################################################################
	c = 19
	licence_management = driver.find_element_by_xpath('//*[@id="sidebarnav"]/li[4]/a').click()
	time.sleep(3)
	print('Licence Management')

	sheet["A%d"%c].value = "Licence Management button"	
	sheet["B%d"%c].value = "working properly"

	#######################################################################################
	c = 20
	notification = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[2]/li[1]/a').click()
	time.sleep(3)
	print('Notification')

	sheet["A%d"%c].value = "Notification button"	
	sheet["B%d"%c].value = "working properly"
	#######################################################################################
	c = 21
	check_all_notification = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[2]/li[1]/div/ul/li[3]/a').click()
	time.sleep(3)
	print('Check all notifications')

	sheet["A%d"%c].value = "Check All Notification button"	
	sheet["B%d"%c].value = "working properly"

	#######################################################################################
	c = 22
	driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[2]/li[2]/a').click()
	logout = driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[2]/li[2]/div/a[2]').click()
	time.sleep(3)
	print('Logout from Admin')

	sheet["A%d"%c].value = "Logout button"	
	sheet["B%d"%c].value = "working properly"
	#######################################################################################
	c = 23
	username = driver.find_element_by_id('username')
	username.click()
	username.send_keys('aishwarya')

	password = driver.find_element_by_id('password')
	password.click()
	password.send_keys('Test@123')

	login = driver.find_element_by_name('submitData').click()
	print('User Login')

	sheet["A%d"%c].value = "User login button"	
	sheet["B%d"%c].value = "working properly"
	#######################################################################################
	c=24
	try:
		for i in range(1,12):
			output = driver.find_element_by_xpath('//*[@id="sidebarnav"]/li[' + str(i) + ']/a')
			driver.find_element_by_xpath('//*[@id="sidebarnav"]/li[' + str(i) + ']/a').click()
			time.sleep(3)
		if output:
			print('User Main Menu')

		sheet["A%d"%c].value = "User Main Menu buttons"	
		sheet["B%d"%c].value = "working properly"	

	except ElementClickInterceptedException:
 		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")		
		#discovery = driver.find_element_by_xpath('//*[@id="sidebarnav"]/li[2]/a').click()

	#######################################################################################
	c=25
	driver.find_element_by_xpath('//*[@id="sidebarnav"]/li[1]/a').click()
	dropdown = Select(driver.find_element_by_id('filter'))	
	#driver.find_element_by_name('device_availability').click()
	#driver.find_element_by_name('devicehealth').click()
	dropdown.select_by_index(0)
	print('Device dropdown button')
	time.sleep(3)
#######################################################################################
except Exception as e:
	print e	
wb.save('testing_front_end.xlsx')
driver.close() 	
