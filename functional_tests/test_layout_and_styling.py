from .base import FunctionalTest
import time


class LayoutAndStylingTest(FunctionalTest):

    def test_lady_and_styling(self):
        #伊迪丝访问首页
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)
        #她看到输入框完美的居中显示
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x']+inputbox.size['width']/2,512,delta=10)
        # 她新建了一个清单，看到输入框仍完美地居中显示
        inputbox.send_keys('testing\n')
        time.sleep(1)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x']+inputbox.size['width']/2,512,delta=10)
