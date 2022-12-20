# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:45:34 2022

@author: 70060241
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path=r"C:\Users\70060241\Downloads\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(path)

driver.get("https://censusindia.gov.in/census.website/data/census-tables")
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "series_10"))
    )
    
except:
    print("No such element found")

element.click()

try:
    drop_down = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(("xpath","/html/body/div/div/div[4]/div/div/div/section/div/div/div/div/div/div/div/div[2]/div[4]/div[8]/div[2]/div[2]/div[1]/a/span/i"))
    )
    
except:
    print("No such drop_down found")
    
drop_down.click()
try:
    check = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(("xpath","//html/body/div/div/div[4]/div/div/div/section/div/div/div/div/div/div/div/div[2]/div[4]/div[8]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/span/a"))
    )
    
except:
    print("No such id found")


  
dis_len=641
for i in range(628,dis_len):
    dis=driver.find_element("xpath","/html/body/div/div/div[4]/div/div/div/section/div/div/div/div/div/div/div/div[2]/div[4]/div[8]/div[2]/div[2]/div[2]/div/table/tbody/tr[%d]/td[3]/span/a" % i)
    dis.click()    

time.sleep(80)

driver.quit()
