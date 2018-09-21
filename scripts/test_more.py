from base.base_driver import init_driver
from page.page import Page


class TestMore:

    def test_2g(self):
        assert 1

    def test_3g(self):
        assert 0


    #
    # def setup(self):
    #     self.driver = init_driver()
    #     self.page = Page(self.driver)
    #     self.driver.find_element()
    #
    # def test_2g(self):
    #     self.page.setting.click_more()
    #     self.page.more.click_mobile_network()
    #     self.page.mobile_network.click_first_network()
    #     self.page.first_network.click_network_2g()






