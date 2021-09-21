#!/usr/bin/python3
# write custom logger that print DEBUG, INFO, and WARNING logs on console 
# but store error logs in a file
# referance url :  https://www.youtube.com/watch?v=8OpYQLl3yGw
import logging


class CustomLogger:
    def get_error_logger(self,name = __name__):
        logger_level = logging.ERROR
        # defining custom logger    
        logger  = logging.getLogger(name = name)
        logger.setLevel(logger_level)
        handler = logging.FileHandler("error.log")
        handler.setFormatter(logging.Formatter("%(name)s -  %(levelname)s - %(message)s"))
        logger.addHandler(handler)
        return logger


    def get_debug_logger(self,name = __name__):
        logger_level = logging.DEBUG
        # defining custom logger    
        logger  = logging.getLogger(name = name)
        logger.setLevel(logger_level)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(name)s -  %(levelname)s - %(message)s"))
        logger.addHandler(handler)
        return logger
c = CustomLogger()
debug = c.get_debug_logger(name = "debug")
error = c.get_error_logger(name = "error")
error.error("errors")
debug.debug("debug")
debug.info("info")
debug.warning("warnings")