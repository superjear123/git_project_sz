from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):
    more_button = By.XPATH, "//*[@text='更多']"

    def click_more(self):
        self.click(self.more_button)
