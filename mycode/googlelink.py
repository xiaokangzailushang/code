# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import re

start_url="https://www.google.com/ncr"
dT=10		#delay time 10s

def click_next_page(driver):
#find next page link and then click
#return 1 if next page exists
#return 0 if next page doesn't exist
	try:
		nextPage = driver.find_element_by_xpath('//span[text()="Next"]')
		if nextPage:
			nextPage.click()
			time.sleep(dT)
			return 1
		else:
			return 0
	finally:
		pass


def collect_links(driver):
#scrape the sub link and return as a list
#有两个element，一个是elementLinks，这个是标题的链接，可以点击；另外一个是links，这个是标题下面的链接地址，不可点击，大多数时候它显示的是
#实际可用的链接，但如果链接地址太长，就会用...代替，所以下面用正则表达式来匹配...，如果匹配成功，则点击上面标题的链接，用webdriver来返回实
#际的地址。
#bug 17/03/2016: 如果在子链接中出现...，同时这个链接是要打开一个dialog来下载文件的，好像那个seq不会自增，就又从0开始，循环往复。	
	linkList=[]
	#正则表达式。因为pattern.match（）是从字符串的开始处匹配，所以这里这里加上了.*
	pattern = re.compile(r".*\.\.\.")
	try:
		#子链接中的可点击标题
		elementLinks = driver.find_elements_by_xpath('//h3[@class="r"]/a')
		seq=0
		#子链接中的地址
		links = driver.find_elements_by_xpath('//cite[@class="_Rm"]')
		length = len(links)
		if length != 0:
			for seq in range(0,length):
				if pattern.match(links[seq].text):
					#需要调用webdriver来点击标题链接以获取实际的链接地址，加上time.sleep()，给程序以刷新网页的时间
					elementLinks[seq].click()
					time.sleep(dT)
					linkList.append(driver.current_url)
					#获取了实际的地址后，返回到原先的页面
					driver.back()
					time.sleep(dT)
					elementLinks = driver.find_elements_by_xpath('//h3[@class="r"]/a')
					links = driver.find_elements_by_xpath('//cite[@class="_Rm"]')
				else:
					linkList.append(links[seq].text)
	finally:
		return linkList

def search_keyword(driver,keyword):
#in google search the keyword
	driver.get(start_url)
	inputElement = driver.find_element_by_name("q")
	inputElement.send_keys(keyword)
	inputElement.submit()
	time.sleep(dT)


if __name__ == '__main__':
	try:
		driver = webdriver.Firefox()
		search_keyword(driver,"xianjun zheng")
		time.sleep(dT)
		print collect_links(driver)
		while click_next_page(driver):
			time.sleep(dT)
			print collect_links(driver)
	finally:
		driver.quit()
