from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

cookies = pickle.load(open('newCookie.pkl','rb'))
browser = webdriver.Firefox()
browser.get('http://www.gumtree.com.au/')
for cookie in cookies:
	if cookie['domain']=='.gumtree.com.au':
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
browser.find_element_by_xpath('//body').send_keys(Keys.CONTROL+'t')
browser.get('http://www.gumtree.com.au/s-appliances/act/c20088l3008838')
links = browser.find_elements_by_xpath('//span[@itemprop="name"]')
links[0].click()
time.sleep(10)
show_number=browser.find_element_by_xpath('//span[@data-target=".ad-phone"]')
show_number.click()

import selenium.webdriver.support.ui as ui
wait=ui.WebDriverWait(browser,10)
xxx.click()
wait.until(lambda browser:browser.title.lower().startswith('washing machine general'))
print "it is good"
