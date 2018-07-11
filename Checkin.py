from selenium import webdriver
import unittest

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

checkin_option = '/html/body/aside/section/ul/li[7]/a'
search_employee_field_id = 'employees'
checkin_type_good = '//*[@id="checkin-create-form"]/div/div[1]/div[2]/div[1]/label'
checkin_type_bad = '//*[@id="checkin-create-form"]/div/div[1]/div[2]/div[2]/label'
checkin_reason_proactive = '//*[@id="checkin-create-form"]/div/div[3]/div[1]/div[1]/label'
checkin_description_field = 'description'
checkin_button = 'form_submit'
checkin_name_suggestion = 'dropdown-item'


class Checkin(unittest.TestCase):
    def test_tc_4_checkin_good(self):
        self.driver = driver
        self.driver.find_element_by_xpath(checkin_option).click()
        self.driver.find_element_by_id(search_employee_field_id).send_keys("zahid")
        self.driver.find_element_by_class_name(checkin_name_suggestion).click()
        self.driver.find_element_by_xpath(checkin_type_good).click()
        self.driver.find_element_by_xpath(checkin_reason_proactive).click()
        self.driver.find_element_by_id(checkin_description_field).send_keys("Test checkin - Good ")
        self.driver.find_element_by_id(checkin_button).click()
        success_message = self.driver.find_element_by_xpath('//*[@id="checkin-create-form"]/div/div[5]/div/div[3]').text
        print("Good ", success_message)

    def test_tc_5_checkin_bad(self):
        self.driver = driver
        self.driver.find_element_by_id(search_employee_field_id).send_keys("zahid")
        self.driver.find_element_by_class_name(checkin_name_suggestion).click()
        self.driver.find_element_by_xpath(checkin_type_bad).click()
        self.driver.find_element_by_xpath(checkin_reason_proactive).click()
        self.driver.find_element_by_id(checkin_description_field).send_keys("Test checkin - bad ")
        self.driver.find_element_by_id(checkin_button).click()
        success_message = self.driver.find_element_by_xpath('//*[@id="checkin-create-form"]/div/div[5]/div/div[3]').text
        print("Bad ", success_message)


if __name__ == '__main__':
    unittest.main(failfast=True, exit=False)
