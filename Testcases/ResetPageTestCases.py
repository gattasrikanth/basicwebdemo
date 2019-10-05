from Framework.Pages.ResetPage import ResetPage
from Framework.Util import Constants as configs
from Framework.Util.Constants import Browser
from Framework.Util.Driver import Driver
from selenium import webdriver
import unittest
import time

class ResePageTestCases(unittest.TestCase):
  '''
  Sample Testcase#1
  Enter valid email address and hit Continue button
  '''
  baseURL = configs.RESET_PAGE_URL
  driver = Driver().getDriver()
  reset_page = ResetPage(driver)

  def test_reset_valid_email_scenario(self):
    self.driver.get(self.baseURL)
    username = 'example@gmail.com'
    time.sleep(5)
    self.reset_page.Reset(username)
    time.sleep(5)
    result = self.reset_page.Verify_Success_Screen()
    time.sleep(5)
    assert result == True
    self.driver.quit()
