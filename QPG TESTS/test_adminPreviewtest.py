# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAdminPreviewtest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_adminPreviewtest(self):
    # Test name: AdminPreview_test
    # Step # | name | target | value
    # 1 | open | http://localhost:3000/admin/dashboard | 
    self.driver.get("http://localhost:3000/admin/dashboard")
    # 2 | setWindowSize | 1552x880 | 
    self.driver.set_window_size(1552, 880)
    # 3 | click | linkText=Dashboard | 
    self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
    # 4 | click | linkText=Questions | 
    self.driver.find_element(By.LINK_TEXT, "Questions").click()
    # 5 | click | linkText=Users | 
    self.driver.find_element(By.LINK_TEXT, "Users").click()
    # 6 | mouseOver | css=#radix-\3Ar4\3A > .lucide | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#radix-\\3Ar4\\3A > .lucide")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 7 | mouseOut | css=#radix-\3Ar4\3A > .lucide | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 8 | click | css=html | 
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    # 9 | mouseDown | css=html | 
    element = self.driver.find_element(By.CSS_SELECTOR, "html")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 10 | mouseUp | css=.gap-6 | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".gap-6")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 11 | click | css=html | 
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    # 12 | click | linkText=Verification | 
    self.driver.find_element(By.LINK_TEXT, "Verification").click()
    # 13 | click | linkText=Users | 
    self.driver.find_element(By.LINK_TEXT, "Users").click()
    # 14 | close |  | 
    self.driver.close()
  