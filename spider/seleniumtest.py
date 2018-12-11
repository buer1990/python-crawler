# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         seleniumtest
# Description:  
# Author:       buer1990
# Date:         2018/11/28
#-------------------------------------------------------------------------------
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html")
time.sleep(3)
ActionChains(driver).move_to_element("继续阅读").perform()
continue_elemet=driver.find_element_by_xpath("..//div[@class='continue-to-read']/div[@class='banner-more-btn']")
continue_elemet.click()


