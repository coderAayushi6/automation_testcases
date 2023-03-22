"""
    This module is used to read the data from the config.ini file
"""
import configparser

config = configparser.RawConfigParser()
config.read("./configuration/config.ini")

class ReadConfig:
    @staticmethod
    def get_applicationURL():
        return config.get('common info', 'URL')

    @staticmethod
    def get_screenshot_path():
        return config.get('common info', 'SCREENSHOT_PATH')

    @staticmethod
    def get_username():
        return config.get('credentials', 'username')


    @staticmethod
    def get_password():
        return config.get('credentials', 'password')

                