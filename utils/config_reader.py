import os
from dotenv import load_dotenv

load_dotenv("config/config.env")


class ConfigReader:

    @staticmethod
    def get_base_url():
        return os.getenv("BASE_URL", "https://automationexercise.com")

    @staticmethod
    def get_browser():
        return os.getenv("BROWSER", "chromium")

    @staticmethod
    def is_headless():
        return os.getenv("HEADLESS", "false").lower() == "true"

    @staticmethod
    def get_slow_mo():
        return int(os.getenv("SLOW_MO", "0"))