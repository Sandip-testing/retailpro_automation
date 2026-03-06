# import logging
# import os
#
# def get_logger():
#     log_dir = "logs"
#     os.makedirs(log_dir, exist_ok=True)
#
#     logger = logging.getLogger()
#     logger.setLevel(logging.INFO)
#
#     file_handler = logging.FileHandler(os.path.join(log_dir, "test.log"))
#     formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
#     file_handler.setFormatter(formatter)
#
#     if not logger.handlers:
#         logger.addHandler(file_handler)
#
#     return logger


import logging
import os
from datetime import datetime


def get_logger(test_name=None):
    os.makedirs("logs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"logs/{test_name}_{timestamp}.log" if test_name else f"logs/test_{timestamp}.log"

    logger = logging.getLogger(test_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger