'''
Element Related actions
'''
import logging as log

class Element:
  def __init__(self, driver):
    self.driver = driver

  def sendKeys(self, locator, text):
    try:
      element = self.getElementById(locator)
      element.send_keys(text)
    except:
      log.info("Unable to enter text")

  def getElementById(self, locator):
    element = None
    try:
      element = self.driver.find_element_by_id(locator)
    except Exception as e:
      log.info("Unable to find element" + locator + e)
      raise e
    return element

  def clickElementById(self, id):
    try:
      element = self.getElementById(id)
      element.click()
    except:
      log.info("Cannot click on the element")

  def isElementVisible(self, locator):
    try:
      element = self.getElementById(locator)
    except:
      return False
    return True