"""

    This module is used to handle generations of framework logging.
"""
import logging

class LogGenerator:
    @staticmethod
    def loggen():
        print("Inside the logging")

        logging.basicConfig(filename=".\\logs\\automationlogs.log",
            format= '%(asctime)s:%(levelname)s:%(message)s' , datefmt= '%d/%m/%Y %I:%M:%S %p',
            force=True


        )                    

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger