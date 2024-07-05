from common_locators import CommonLocators


class CommonFunctions(CommonLocators):
    default_browser = 'firefox'

    def open_browser(self, which_browser):
        which_browser = which_browser if which_browser else self.default_browser
        if which_browser == 'firefox':
            pass




