# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class start(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_start(self):
        success = True
        wd = self.wd
        wd.get("https://portal.dev.influential.co/")
        wd.find_element_by_link_text("GET STARTED").click()
        wd.find_element_by_xpath("//article[@id='product-selection']/section[2]/a").click()
        wd.find_element_by_id("name-first").click()
        wd.find_element_by_id("name-first").clear()
        wd.find_element_by_id("name-first").send_keys("Test")
        wd.find_element_by_xpath("//label[@for='name-last']").click()
        wd.find_element_by_id("name-last").click()
        wd.find_element_by_id("name-last").clear()
        wd.find_element_by_id("name-last").send_keys("Test")
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys("test@test.com")
        wd.find_element_by_xpath("//form[@class='public-form-container']//div[.='Company']").click()
        wd.find_element_by_id("company-name").click()
        wd.find_element_by_id("company-name").clear()
        wd.find_element_by_id("company-name").send_keys("Home")
        wd.find_element_by_xpath("//label[@for='username']").click()
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys("Newtest")
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("test1234567")
        wd.find_element_by_xpath("//label[@for='password-confirm']").click()
        wd.find_element_by_id("password-confirm").click()
        wd.find_element_by_id("password-confirm").clear()
        wd.find_element_by_id("password-confirm").send_keys("test1234567")
        wd.find_element_by_xpath("//form[@class='public-form-container']//button[.='Sign Up']").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
