import time
from common_functions import COMMON_FUNCTIONS
from locators import Locators
from login import LOGIN


class SEARCH:
    def search(self):
        lg = LOGIN()
        common = lg.login()
        common.input_text_with_css_selector(Locators.search_text_box,"Halter Dress")
        common.click_with_css_selector(Locators.search_icon)


srch = SEARCH()
srch.search()