""" Logging for CloudFlare API"""
import logging

DEBUG = 0
INFO = 1

class Logger(object):
    """ Logging for CloudFlare API"""

    def __init__(self, level):
        """ Logging for CloudFlare API"""
        self.logger_level = self._get_logging_level(level)
        #logging.basicConfig(level=self.logger_level)
        request_logger = logging.getLogger("requests.packages.urllib3")
        request_logger.setLevel(self.logger_level)
        request_logger.propagate = level

    def getLogger(self):
        """ Logging for CloudFlare API"""
        # create logger
        logger = logging.getLogger('Python CloudFlare API v4')
        logger.setLevel(self.logger_level)

        ch = logging.StreamHandler()
        ch.setLevel(self.logger_level)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        return logger

    def _get_logging_level(self, level):
        """ Logging for CloudFlare API"""
        if level is True:
            return logging.DEBUG
        else:
            return logging.INFO
