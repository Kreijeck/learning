#########################################
# author: Thomas Strehler
# created: 25.02.2021
#######################################

import logging
import os

def printit():
    print("import geht endlich1!!!")
class MyLogger:
    """
    Usage:
    Import Class My Logger
    Add optional loglevels for stream and file-Hander
    loglevel: "debug", "info", "warning", "error"

    Add Loggers:  add_logger(stream_handler=True, file_handler=True, folder='log', filename='log.log')
    Use that logger
    """
    def __init__(self, name, loglevel_stream="debug", loglevel_file="debug"):
        # set loglevel
        self.loglevel_stream = self.__loglevel(loglevel_stream)
        self.loglevel_file = self.__loglevel(loglevel_file)

        # set formatter
        self.formatter = logging.Formatter('%(asctime)s: %(name)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")

        # set logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

    @staticmethod
    def __loglevel(level):
        if level == "debug":
            return logging.DEBUG
        elif level == "info":
            return logging.INFO
        elif level == "warning":
            return logging.WARNING
        elif level == "error":
            return logging.ERROR
        else:
            raise KeyError(f"Loglevel {level} not allowed!")

    def add_stream_logger(self):
        lh = logging.StreamHandler()
        lh.setLevel(self.loglevel_stream)
        lh.setFormatter(self.formatter)

        self.logger.addHandler(lh)

    def add_file_logger(self, folder, file):
        # create folder
        if not os.path.exists(folder):
            os.makedirs(folder)

        save = os.path.join(folder, file)

        lh = logging.FileHandler(save)
        lh.setLevel(self.loglevel_file)
        lh.setFormatter(self.formatter)

        self.logger.addHandler(lh)

    def add_logger(self, stream_handler=True, file_handler=True, folder='log', filename='log.log'):
        """
        Add wishend logger
        :param stream_handler: bool, add StreamHandler
        :param file_handler: bool, add FileHandler
        :param folder: folder from Working Dir
        :param filename: filename, inkl. ending
        :return: get a logger for messages
        """
        if stream_handler:
            self.add_stream_logger()
        if file_handler:
            self.add_file_logger(folder=folder, file=filename)

        return self.logger

