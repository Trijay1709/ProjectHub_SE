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

class TestUserPreviewtest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_userPreviewtest(self):
    # Test name: UserPreview_test
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:3000/admin/dashboard/")
    # 2 | setWindowSize | 1084x832 | 
    self.driver.set_window_size(1084, 832)
    # 3 | click | xpath=//button[contains(.,'Add a Question')] | 
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Add a Question\')]").click()
    # 4 | click | xpath=//button[contains(.,'Subjects')] | 
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Subjects\')]").click()
    # 5 | click | xpath=//button[contains(.,'Your Questions')] | 
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Your Questions\')]").click()
    # 6 | click | xpath=//button[contains(.,'Community Question')] | 
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Community Question\')]").click()
    # 7 | click | xpath=//button[contains(.,'Verification Portal')] | 
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Verification Portal\')]").click()
    # 8 | click | xpath=//button[contains(.,'Apply')] | 
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Apply\')]").click()
    # 9 | open | http://localhost:3000/admin/dashboard | 
    self.driver.get("http://localhost:3000/admin/dashboard")
    # 10 | click | xpath=//a[contains(.,'Users')] | 
    self.driver.find_element(By.XPATH, "//a[contains(.,\'Users\')]").click()
    # 11 | click | xpath=//*[@id="radix-:r4:"] | 
    self.driver.find_element(By.XPATH, "//*[@id=\"radix-:r4:\"]").click()
    # 12 | close |  | 
    self.driver.close()
  