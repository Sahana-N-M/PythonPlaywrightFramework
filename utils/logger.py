import logging
import os

def get_logger():
    if not os.path.exists("reports"):
        os.makedirs("reports")

    logging.basicConfig(
        filename="reports/execution.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    return logging.getLogger()