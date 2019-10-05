'''
All Constants related to app
'''
from enum import Enum
from pathlib import Path
import os

class Browser(Enum):
  CHROME = "CHROME"
  FIREFOX = "FIREFOX"
s = os.getcwd()
CURR_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
CURR_DIR = Path(CURR_DIR_PATH)
ROOT_DIR = Path(Path(CURR_DIR.parent).parent)
CHROME_DRIVER_PATH = os.path.join(ROOT_DIR, 'Drivers/chromedriver')

WEB_APP_BASE_URL = "https://www.creditkarma.com/"

#Reset Page Related Elements
RESET_PAGE_URL = WEB_APP_BASE_URL + "auth/resetpw"
RESET_PAGE_EMAIL_FIELD_ID = 'email'
RESET_PAGE_CONTINUE_BUTTON_ID = 'continueBtnBig'