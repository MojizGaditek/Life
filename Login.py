from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import unittest


class Myloginclass(unittest.TestCase):
    # @classmethod
    def test_TC_1_login_page(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://devlife.gaditek-hrms.sg.plesk-server.com/")
        self.driver.find_element_by_xpath("//*[@id='employee_id']").send_keys("mojiz.mehdi@gaditek.com")
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys("mojizmehdi1")
        self.driver.find_element_by_xpath("//*[@id='emp_login']").click()


if __name__ == '__main__':
    unittest.main(failfast=True, exit=False)

