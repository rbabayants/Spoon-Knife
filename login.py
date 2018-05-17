# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class login(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_login(self):
        success = True
        wd = self.wd
        wd.get("https://portal.dev.influential.co/")
        # open site
        wd.find_element_by_css_selector("div.hero-image").click()
        #login
        wd.find_element_by_link_text("Login").click()
        wd.find_element_by_xpath("//label[@for='email']").click()
        # email address
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys("rbabayants@gmail.com")
        # Password
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("Test123456")
        wd.find_element_by_xpath("//form[@class='public-form-container']//button[.='Sign In']").click()
        wd.find_element_by_css_selector("i.fa.fa-cog").click()
        #logout
        wd.find_element_by_link_text("Logout").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
