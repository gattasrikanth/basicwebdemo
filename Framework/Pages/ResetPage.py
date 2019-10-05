from Framework.Util.Driver import Driver
from Framework.Util import Constants as configs
from Framework.Util import Element

class ResetPage():
  def __init__(self, driver):
    # super().__init__(self)
    self.driver = driver#super().__init__()
    self.email_field = configs.RESET_PAGE_EMAIL_FIELD_ID
    self.continue_button = configs.RESET_PAGE_CONTINUE_BUTTON_ID
    self.element = Element.Element(self.driver)
    # return self.driver

  def click_continue(self):
    self.element.clickElementById(self.continue_button)

  def enter_email_address(self, email):
    self.element.sendKeys(self.email_field, email)

  def Reset(self, email):
    self.enter_email_address(email)
    self.click_continue()

  def Verify_Success_Screen(self):
    # Implement code here
    return True