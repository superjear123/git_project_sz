from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class FirstNetworkPage(BaseAction):
    def __init__(self,driver):
        self.driver = driver


    network_2g_button = By.XPATH, "//*[@text='2G']"

    network_3g_button = By.XPATH, "//*[@text='3G']"
    cancel_button = By.XPATH, "//*[@text='取消']"

    def click_network_2g(self):
        # self.driver.find_element(By.XPATH, "//*[@text='2G']")
        self.click(self.network_2g_button)

    def click_network_3g(self):
        self.click(self.network_3g_button)

    def click_cancel(self):
        self.click(self.cancel_button)

