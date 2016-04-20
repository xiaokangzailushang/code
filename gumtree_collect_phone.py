
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import wswp.disk_cache_no_pickle as disk_cache

import time
import pickle
import os
import random

d_T = 10

def open_new_tab_by_click(browser,element):
	"""
		open a new tab by clicking the elemnt plus control key down
		then switch the focus to the new tab
	"""	
	try:	
		ActionChains(browser).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
		browser.find_element_by_xpath('//body').send_keys(Keys.CONTROL+Keys.TAB)
	except:
		print "Error: def open_new_tab_by_click"

def close_current_tab(browser):
	"""
		close the current tab by sending ctrl+w
	"""
	browser.find_element_by_xpath('//body').send_keys(Keys.CONTROL+'w')

def open_new_tab(browser,link):
	browser.find_element_by_xpath('//body').send_keys(Keys.CONTROL+'t')
	browser.get(link)

def login_gumtree():
	try:
		fp=webdriver.FirefoxProfile(os.environ['HOME']+'/.mozilla/firefox/pow2rtqi.default')
		browser = webdriver.Firefox(fp)
		#browser = webdriver.Firefox('/home/jun/git/code/Gumtree/firefox/cookie.sqlite-wal')
		browser.get('http://www.gumtree.com.au/')
		"""
		sign_in = browser.find_element_by_xpath('//a[@class="sign-in"]')
		sign_in.click()
		time.sleep(1)
		login_email=browser.find_element_by_xpath('//input[@id="login-email"]')
		login_email.send_keys('wolff_zheng@hotmail.com')
		login_password=browser.find_element_by_xpath('//input[@id="login-password"]')
		login_password.send_keys('Wolff8341')
		time.sleep(5)
		login_password.submit()
		print "login success!"
		"""
		return browser
	except:	
		browser.quit()
		print "login failed!!!!!"
		return 0

def collect_number_from_single_page(browser,cache):
	
	current_url = browser.current_url
	links = browser.find_elements_by_xpath('//span[@itemprop="name"]')
	trys = 3
	if not links:
		print browser.current_url,"------ can't find span[@itemprop=name]"
		return 0
	else:
		for num in range(0,len(links)):
			links[num].click()
			time.sleep(2*d_T+random.randint(0,3*d_T))
			try:	
				show_number=browser.find_element_by_xpath('//span[@data-target=".ad-phone"]')
			except Exception,e:
				print "show_number caused exception.%s"%browser.current_url
			else:
				time.sleep(d_T+random.randint(0,6*d_T))
				show_number.click()
				time.sleep(d_T+random.randint(0,2*d_T))
				number=browser.find_element_by_xpath('//span[@class="ad-phone c-pull-left c-icon-phone"]')
				while '*' in number.text and trys != 0:
					time.sleep(d_T)
					number=browser.find_element_by_xpath('//span[@class="ad-phone c-pull-left c-icon-phone"]')
					trys = trys - 1
				print number.text
				trys = 3
				cache[browser.current_url]=browser.page_source
			finally:
				browser.get(current_url)
				time.sleep(d_T)
				links = browser.find_elements_by_xpath('//span[@itemprop="name"]')
		return 1

def go_to_next_link(browser):
	"""go to next link by clicking the link + ctrl key down
	"""	
	try:
		next_tag = browser.find_element_by_xpath('//span[@class="rs-text"]')
	except:
		print "Error in go_to_next_link: possible reach the end of search result!"
		return 0
	else:
		open_new_tab_by_click(browser=browser,element=next_tag)
		return 1


if __name__=='__main__':
	link = raw_input("Please input the address:")
	browser = login_gumtree()
	#browser.implicitly_wait(30)
	cache = disk_cache.DiskCache(check=False)
	if browser != 0 :
		#open_new_tab_by_click(browser=browser,element=home_garden)
		open_new_tab(browser,link)
		time.sleep(d_T+random.randint(0,3*d_T))
		#collect_number_from_single_page(browser=browser,cache=cache)
		while go_to_next_link(browser):
			time.sleep(d_T+random.randint(0,3*d_T))
			browser.find_element_by_xpath('//body').send_keys(Keys.CONTROL+Keys.TAB)
			browser.find_element_by_xpath('//body').send_keys(Keys.CONTROL+Keys.TAB)
			close_current_tab(browser)
			time.sleep(d_T+random.randint(0,3*d_T))
			collect_number_from_single_page(browser=browser,cache=cache)
			time.sleep(d_T+random.randint(0,3*d_T))
		browser.close()
	
	
	
