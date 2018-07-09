# import unittest
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException

url = "http://devlife.gaditek-hrms.sg.plesk-server.com/"
Email = "mojiz.mehdi@gaditek.com"
password = "mojizmehdi1"


ids = {'EmailTxtBox': "employee_id",
       'passwordTxtBox': "password",
       'submitButton': "emp_login"}

mydriver = webdriver.Firefox()
mydriver.get(url)

mydriver.find_element_by_id(ids['EmailTxtBox']).clear()
mydriver.find_element_by_id(ids['EmailTxtBox']).send_keys(Email)
mydriver.find_element_by_id(ids['passwordTxtBox']).clear()
mydriver.find_element_by_id(ids['passwordTxtBox']).send_keys(password)
mydriver.find_element_by_id(ids['submitButton']).click()

# delay = 60  # seconds
# try:
#   myElem = WebDriverWait(mydriver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
#  print("Page is ready!")
# except TimeoutException:
#  print("Loading took too much time!")


# class Lunch(unittest.TestCase):
# def setUp(self):
# self.mydriver.navigate().to("http://devlife.gaditek-hrms.sg.plesk-server.com/lunch/menu")
lunch_order_option = "/html/body/aside/section/ul/li[13]/a/span[1]"
lunch_menu_option = "/html/body/aside/section/ul/li[13]/ul/li[1]/a"
order_table = "default-table table dataTable no-footer order-menu-list"
first_order_click = "/html/body/main/div/section/div[2]/div/div/div/table/tbody/tr[1]/td[7]/button"
place_order_button = "/html/body/main/div/section/div[1]/div[1]/div[2]/div[1]/input"
confirm_button_popup = "/html/body/main/div/section/div[5]/div/div/div[2]/div[2]/div[1]/form/input[4]"
history_option = "/html/body/aside/section/ul/li[13]/ul/li[2]/a"

# def lunch_order(self):
mydriver.find_element_by_xpath(lunch_order_option).click()
mydriver.find_element_by_xpath(lunch_menu_option).click()
# mydriver.find_element_by_class(order_table)
mydriver.find_element_by_xpath(first_order_click).click()
mydriver.find_element_by_xpath(place_order_button).click()
mydriver.find_element_by_xpath(confirm_button_popup).click()
mydriver.find_element_by_xpath(history_option).click()
remaining_balance = mydriver.find_element_by_xpath('/html/body/main/div/section/div/div[4]/div[4]/div[1]/strong').text
amount = mydriver.find_element_by_xpath('/html/body/main/div/section/div/div[4]/div[4]/div[2]').text
print(remaining_balance)
print(amount)


# def tearDown(self):
# self.mydriver.close()

