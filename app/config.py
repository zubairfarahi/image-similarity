import os
import logging
import configparser
import sys
from datetime import datetime
import time

class AppConfig:
    def __init__(self):
        self.params = self.__read_config()
        
        self.host = os.getenv("HOST")
        if self.host is None:
            self.host = self.params["APP"]["Host"]
        self.port = os.getenv("PORT")
        if self.port is None:
            self.port = self.params["APP"]["Port"]
            
        self.server_startup = self.__set_startup_time()
   
    def __set_startup_time(self):
        server_time_format = datetime.fromtimestamp(time.time())
        return server_time_format.strftime("%Y-%m-%dT%H:%M:%S+02:00")

    def __read_config(self):
        config_file_path = os.getenv("CONFIG_FILE")
        if config_file_path is None:
            logging.error(
                "Config file path is not setted. Use CONFIG_FILE=path/to "
                "UVICORN_PORT=XXXX UVICORN_HOST=X.X.X.X uvicorn main:app to "
                "start the application."
            )
            logging.error("Process finished with exit code 0")
            sys.exit(0)
        else:
            
            logging.info("Read the config file from {0}".format(config_file_path))
            config = configparser.ConfigParser()
            config.read(config_file_path)
            return config

CONFIG = AppConfig()