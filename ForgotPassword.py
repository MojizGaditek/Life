from selenium import webdriver

url = "http://devlife.gaditek-hrms.sg.plesk-server.com/"
Email = "zahid.friend123@gmail.com"

mydriver = webdriver.Firefox()
mydriver.get(url)

mydriver.find_element_by_xpath('/html/body/section/div/div/div/form/a').click()

mydriver.find_element_by_xpath("//*[@id='email']").clear()
mydriver.find_element_by_xpath("//*[@id='email']").send_keys(Email)
mydriver.find_element_by_xpath('//*[@id="emp_login"]').click()

assert mydriver.page_source.find("We have e-mailed your password reset link!")

mydriver.quit()
