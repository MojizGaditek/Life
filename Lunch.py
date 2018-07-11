import unittest
from selenium import webdriver

url = "http://devlife.gaditek-hrms.sg.plesk-server.com/"
Email = "mojiz.mehdi@gaditek.com"
password = "mojizmehdi1"


ids = {'EmailTxtBox': "employee_id",
       'passwordTxtBox': "password",
       'submitButton': "emp_login"}

driver = webdriver.Firefox()
driver.get(url)

driver.find_element_by_id(ids['EmailTxtBox']).clear()
driver.find_element_by_id(ids['EmailTxtBox']).send_keys(Email)
driver.find_element_by_id(ids['passwordTxtBox']).clear()
driver.find_element_by_id(ids['passwordTxtBox']).send_keys(password)
driver.find_element_by_id(ids['submitButton']).click()


class Lunch(unittest.TestCase):
    def test_tc_3_lunch(self):
        lunch_order_option = "/html/body/aside/section/ul/li[13]/a/span[1]"
        lunch_menu_option = "/html/body/aside/section/ul/li[13]/ul/li[1]/a"
        first_order_click = "/html/body/main/div/section/div[2]/div/div/div/table/tbody/tr[1]/td[7]/button"
        place_order_button = "/html/body/main/div/section/div[1]/div[1]/div[2]/div[1]/input"
        confirm_button_popup = "/html/body/main/div/section/div[5]/div/div/div[2]/div[2]/div[1]/form/input[4]"
        history_option = "/html/body/aside/section/ul/li[13]/ul/li[2]/a"
        self.driver = driver
        self.driver.find_element_by_xpath(lunch_order_option).click()
        self.driver.find_element_by_xpath(lunch_menu_option).click()
        self.driver.find_element_by_xpath(first_order_click).click()
        self.driver.find_element_by_xpath(place_order_button).click()
        self.driver.find_element_by_xpath(confirm_button_popup).click()
        self.driver.find_element_by_xpath(history_option).click()
        rb = self.driver.find_element_by_xpath('/html/body/main/div/section/div/div[4]/div[4]/div[1]/strong').text
        amount = self.driver.find_element_by_xpath('/html/body/main/div/section/div/div[4]/div[4]/div[2]').text
        print(rb)
        print(amount)


if __name__ == '__main__':
    unittest.main(failfast=True, exit=False)
