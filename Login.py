from selenium import webdriver

url = "http://devlife.gaditek-hrms.sg.plesk-server.com/"
Email = "mojiz.mehdi@gaditek.com"
password = "mojizmehdi1"


xpaths = {'EmailTxtBox': "//*[@id='employee_id']",
          'passwordTxtBox': "//*[@id='password']",
          'submitButton':   "//*[@id='emp_login']"}

mydriver = webdriver.Firefox()
mydriver.get(url)

mydriver.find_element_by_xpath(xpaths['EmailTxtBox']).clear()
mydriver.find_element_by_xpath(xpaths['EmailTxtBox']).send_keys(Email)
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)
mydriver.find_element_by_xpath(xpaths['submitButton']).click()

mydriver.quit()
