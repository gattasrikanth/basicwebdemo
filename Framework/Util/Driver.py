'''
Configure Selenium Driver
'''

from selenium import webdriver
import logging as log
from Framework.Util.Constants import Browser as Browser
from Framework.Util import Constants as configs

class Driver():
  def __init__(self, browser=Browser.CHROME):
    if browser == Browser.CHROME:
      self.driver = webdriver.Chrome(configs.CHROME_DRIVER_PATH)
    elif browser == Browser.FIREFOX:
      self.driver = webdriver.Firefox()
    else:
      print("Invalid Browser Config")

  def getDriver(self):
    return self.driver