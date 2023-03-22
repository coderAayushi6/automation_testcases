
import pytest, json
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from lib.utils.base_page_object import BasePage
from lib.utils.readProperties import ReadConfig
 
URL = "https://admin-demo.nopcommerce.com/login"
# SCREENSHOT_PATH = "screenshots"

def pytest_addoption(parser):
    parser.addoption("--browser", action= 'store')


@pytest.fixture    
def cli_browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def config(cli_browser):
    BROWSER = ["chrome", "fireFox"]

    with open('config.json') as config_files:
        config = json.load(config_files)

        browser = cli_browser

        if browser is not None:
            config['browser'] = browser

        assert config['browser'] in BROWSER
        return config

@pytest.fixture
def browser_assignment(config):    
    if config['browser'] == "chrome":
        browser =BasePage(Chrome(executable_path=ChromeDriverManager().install()))
        browser.visit_url(ReadConfig.get_applicationURL())

    else:
        raise Exception("Browser{} is not supported".format(config["browser"]))    
    
    yield browser
    browser.quit()
