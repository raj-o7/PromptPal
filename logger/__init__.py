import logging
from datetime import datetime
import os

class CustomLogger:
    # Creating a custom logger class to handle the logging with timestamp and date
    def __init__(self):
        self.log_dir="logs"

        # Here we are creating a log directory if does not exist
        os.makedirs(self.log_dir,exist_ok=True)

        # Now we are adding a time stamp to our log file
        current_time_stamp=f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

        # Define the logfile name with the timestamp
        self.log_file_name=f"log_{current_time_stamp}.log"

        # Define complete path for the log file
        self.log_file_path=os.path.join(self.log_dir,self.log_file_name)

        # Now we will setup basic logging configuration
        logging.basicConfig(
            filename=self.log_file_path,
            filemode="a", #We can use w if everytime we want to overwrite the existing log details
            format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

        # Creating a logger instance
        self.logger=logging.getLogger(__name__)

    def get_logger(self):
        return self.logger

