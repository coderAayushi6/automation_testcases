
import pytest
from lib.sitePageFactory.admin_login_page import LoginPage
# from .conftest import SCREENSHOT_PATH
from lib.utils.readProperties import ReadConfig
from lib.utils.customLogger import LogGenerator

class Test_Login:
      logger = LogGenerator.loggen()

      
      def test_loginPageTitle(self, browser_assignment):

            self.logger.info('************** test_loginPageTitle **************')
            self.logger.info('************** started with the verification **************')


            fetched_title = browser_assignment.get_title()
            print("fetched Title is", fetched_title)

            if fetched_title == 'Your store. Login':
                  assert True
                  self.logger.info('************** test_loginPageTitle -Passed **************')

            else:
                  browser_assignment.get_screenshot(ReadConfig.screenshot_path() + "/test_loginPageTitle.png")
                  assert False      
                  self.logger.info('************** test_loginPageTitle -Failed **************')



      def test_login(self, browser_assignment):

          self.logger.info('************** test_login **************')
          self.logger.info('************** started with the verification **************')

          LoginPage(browser_assignment).username_textbox().clear()
          LoginPage(browser_assignment).password_textbox().clear()

          LoginPage(browser_assignment).username_textbox().send_keys(ReadConfig.get_username())
          LoginPage(browser_assignment).password_textbox().send_keys(ReadConfig.get_password())

          LoginPage(browser_assignment).login_button().click()

          fetched_title = browser_assignment.get_title()

          if fetched_title == 'Dashboard / nopCommerce administration':
              assert True
              self.logger.info('************** test_login -Passed **************')


          else:
                browser_assignment.get_screenshot(ReadConfig.get_screenshot_path() + "test_login.png")
                assert False
                self.logger.info('************** test_login -Failed **************')
  

          