import unittest
from selenium import webdriver


class Forgotpassword(unittest.TestCase):
    @classmethod
    def test_TC_2_Forgot_password(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://devlife.gaditek-hrms.sg.plesk-server.com/")
        cls.driver.find_element_by_xpath('/html/body/section/div/div/div/form/a').click()
        cls.driver.find_element_by_xpath("//*[@id='email']").send_keys("zahid.friend123@gmail.com")
        cls.driver.find_element_by_xpath('//*[@id="emp_login"]').click()
        sucess_message = cls.driver.find_element_by_xpath('/html/body/section/div/div/div/div/div/div').text
        print(sucess_message)


if __name__ == '__main__':
    unittest.main(failfast=True, exit=False)
