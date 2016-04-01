
from selenium import webdriver

import time
import pickle
def login_gumtree():
	cookies = pickle.load(open('gumtree_cookie.pkl','rb')) 
	try:
		browser = webdriver.Firefox()
		#browser = webdriver.Firefox('/home/jun/git/code/Gumtree/firefox/cookie.sqlite-wal')
		browser.get('http://www.gumtree.com.au/')
		for cookie in cookies:
			browser.add_cookie(cookie)
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
		return browser
	except:	
		browser.quit()
		print "login failed!!!!!"
		return 0

def collect_number_from_single_page(browser):
	
	current_url = browser.current_url
	links = browser.find_elements_by_xpath('//span[@itemprop="name"]')
	if not links:
		print browser.current_url,"------ can't find span[@itemprop=name]"
		return 0
	else:
		for num in range(0,len(links)):
			links[num].click()
			time.sleep(10)
			try:	
				show_number=browser.find_element_by_xpath('//span[@data-target=".ad-phone"]')
			except Exception,e:
				print "show_number caused exception.%s"%browser.current_url
			else:
				show_number.click()
				time.sleep(5)
				number=browser.find_element_by_xpath('//span[@class="ad-phone c-pull-left c-icon-phone"]')
				print number.text
			finally:
				browser.get(current_url)
				time.sleep(10)
				links = browser.find_elements_by_xpath('//span[@itemprop="name"]')
		return 1
	

if __name__=='__main__':
	ff = login_gumtree()
	if ff != 0 :
		ff.get('http://www.gumtree.com.au/s-appliances/act/c20088l3008838')
		time.sleep(10)
		collect_number_from_single_page(ff)
	
	
	
