

from selenium.webdriver.common.by import By
from lib.utils.base_page_object import BasePage
from selenium.common.exceptions import NoSuchElementException

class LoginPage(BasePage):

    def __init__(self, browser):
        BasePage.__init__(self, browser)
        self.browser = browser

    locators_dictionary = {

        "usename_textbox": (By.ID, 'Email'),
        "password_textbox": (By.ID, 'Password'),
        "login_button": (By.XPATH, "//button[text() = 'Log in']"),

    }         
    
    def username_textbox(self):
        try:
            return self.browser.find_element_by_locator(LoginPage.locators_dictionary["usename_textbox"])
        except NoSuchElementException:
            return None

    def password_textbox(self):
        try:
            return self.browser.find_element_by_locator(LoginPage.locators_dictionary["password_textbox"])
        except NoSuchElementException:
            return None        
    
    def login_button(self):
        try:
            return self.browser.find_element_by_locator(LoginPage.locators_dictionary["login_button"])
        except NoSuchElementException:
            return None        
    