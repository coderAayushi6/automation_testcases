

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    __TIMEOUT = 30


    def __init__(self, browser):
        self.browser = browser
        self.browser_wait = WebDriverWait(self.browser, BasePage.__TIMEOUT)


    def visit_url(self, url):
        self.browser.get(url)
        self.browser.maximize_window()

    def find_element_by_locator(self,locator):
        return self.browser_wait.until(EC.visibility_of_element_located(locator))  
    

    def find_elements_by_locator(self,locator):
        return self.browser_wait.until(EC.visibility_of_elements_located(locator))  
    

    def quit(self):
        return self.browser.quit()
    
        
    def get_title(self):
        return self.browser.title
    
    def get_screenshot(self, path):
        return self.browser.save_screenshot(path)
