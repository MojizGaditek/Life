import requests
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Firefox()
driver.get('http://devlife.gaditek-hrms.sg.plesk-server.com/')

Email = "mojiz.mehdi@gaditek.com"
password = "mojizmehdi1"


ids = {'EmailTxtBox': "employee_id",
       'passwordTxtBox': "password",
       'submitButton': "emp_login"}

driver.find_element_by_id(ids['EmailTxtBox']).clear()
driver.find_element_by_id(ids['EmailTxtBox']).send_keys(Email)
driver.find_element_by_id(ids['passwordTxtBox']).clear()
driver.find_element_by_id(ids['passwordTxtBox']).send_keys(password)
driver.find_element_by_id(ids['submitButton']).click()

links = driver.find_elements_by_css_selector("a")
for link in links:
    if hasattr(link, "href") and link.get_attribute('href') not in 'javascript:void':
        r = requests.head(link.get_attribute('href'))
        print(link.get_attribute('href'), r.status_code)
    else:
        print(link.get_attribute('href'), "200")

# code for fetching all links in a URL
# elems = driver.find_elements_by_xpath("//a[@href]")
# for elem in elems:
# print(elem.get_attribute("href"))
