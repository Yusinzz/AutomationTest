from selenium import webdriver
import selenium
import os 

desired_cap = {} #macos 需要把desired_cap 設為空值
# driver = webdriver.Chrome(executable_path= "/Users/zyusin/side_project/selenium/chromedriver")
driver = webdriver.Edge(executable_path="/Users/zyusin/side_project/selenium/msedgedriver", capabilities=desired_cap)

userid =""
password = ""
driver.get("https://www.gamer.com.tw/")

element = driver.find_element_by_xpath("//a[contains(@href,'login.php')]")  #find a href tag which contain login.php
element.click()                                                             #then click it 

elementid = driver.find_element_by_name("userid")                           #can find some element in common. I choose the name tag. 
elementpassword = driver.find_element_by_name("password")
elementlogin = driver.find_element_by_id("btn-login")

elementid.send_keys(userid)                                                 #input userid and password
elementpassword.send_keys(password)
elementlogin.click()                                                        #then click 


