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

class TestAddsubject():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addsubject(self):
    # Test name: Add_subject
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:3000/admin/dashboard/")
    # 2 | setWindowSize | 1084x832 | 
    self.driver.set_window_size(1084, 832)
    # 3 | clickAt | xpath=//button[contains(.,'Subjects')] | 
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Subjects\')]").click()
    # 4 | click | xpath=//input | 
    self.driver.find_element(By.XPATH, "//input").click()
    # 5 | type | xpath=//input | Physics
    self.driver.find_element(By.XPATH, "//input").send_keys("Physics")
    # 6 | click | css=.bg-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".bg-primary").click()
    # 7 | close |  | 
    self.driver.close()
  