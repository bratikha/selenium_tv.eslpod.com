# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pprint import pprint
import re

driver = webdriver.Firefox()
driver.get("https://sso.teachable.com/secure/147717/users/sign_in?clean_login=true&reset_purchase_session=1")
driver.find_element_by_id("user_email").clear()
driver.find_element_by_id("user_email").send_keys("eMAiL")
driver.find_element_by_id("user_password").clear()
driver.find_element_by_id("user_password").send_keys("PAssWoRd")
driver.find_element_by_name("commit").click()
driver.get("https://tv.eslpod.com/courses/enrolled/239512")
links = driver.find_elements_by_css_selector('.item')
link_list = []
for link in links:
	link_list.append(link.get_attribute('href'))
	
for link in link_list:	
	driver.get(link)
	out_L_file_name = str(driver.find_element_by_id('lecture_heading').text.encode('utf-8'))
	out_L_file_name = re.sub('[!@#$:?*.“”\/<>|""]', ' ', out_L_file_name) 
	out_L_file_name = out_L_file_name[2:] + ".txt"
	out_L_file = open(out_L_file_name,"w")
	out_L_file.writelines(driver.find_element_by_class_name('lecture-text-container').text.encode('utf-8'))
	out_L_file.close()
	out_A_file = open("Cultural English 501 - 603","a")
	out_A_file.write(driver.find_element_by_class_name('audioloader').get_attribute('data-audioloader-url') + '\n') 
	out_A_file.close()
	# break

driver.close


